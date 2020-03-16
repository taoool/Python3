def parse_request(recv_data, ip_port):
    """解析请求的报文，返回客户端请求的资源路径"""
    # 根据客户端浏览器请求的资源路径，返回请求资源
    # 1）把请求协议解码，得到请求报文的字符串
    request_text = recv_data.decode()
    # 2）得到请求行
    #   （1） 查找 第一个、人\r\n 出现的位置
    loc = request_text.find("\r\n")
    #   （2） 截取字符串，从开头截取到 第一个\r\n 出现的位置
    request_line = request_text[:loc]
    # 把请求行，按照空格拆分，得到列表
    request_line_text = request_line.split(" ")
    print(request_line_text)
    # 得到请求资源路径
    file_path = request_line_text[1]
    print(f"[{str(ip_port)}]正在请求{file_path}")

    # 设置默认首页
    if file_path == "/":
        file_path = "/a/index.html"

    return file_path

def appllication(current_dir, recv_data, ip_port):

    #调用  parse_request函数，解析请求协议，返回请求的资源路径
    file_path = parse_request(recv_data, ip_port)

    resource_path = current_dir + file_path
    # 9，拼接响应的报文
    # 响应行
    response_line = "HTTP/1.1 200 OK\r\n"
    # 响应头
    response_header = "server:pythonwb/3.4\r\n"
    # 响应空行
    response_blank = "\r\n"
    try:
        # 读取文件内容
        with open(resource_path, "rb") as file:
            # 返回给客户端
            response_body = file.read()
    except Exception as e:
        # 重新修改响应行为 404
        response_line = "HTTP/1.1 404 Not Found\r\n"
        # 响应内容为错误
        response_body = "Error!(%s)" % (str(e))
        # 把内容转换为字节码
        response_body = response_body.encode()
    # 拼接响应报文
    response_data = (response_line + response_header + response_blank).encode() + response_body
    return response_data
