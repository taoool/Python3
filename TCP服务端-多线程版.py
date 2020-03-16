"""
1，导入模块
2，创建套接字
3，设置地址重用
4，绑定端口
5，设置监听，套接字由主动设置为被动
6，接受客户端连接
7，接受客户端发送的信息
8，解码数据并且进行输出
9，关闭和当前客户端连接

"""
import socket
import threading


def recv_msg(new_client_socket, ip_port):
    while True:
        # 7，接受客户端发送的信息
        recv_data = new_client_socket.recv(1024)
        if not recv_data:
            print("客户端已断开")
            break
        # 8，解码数据并且进行输出
        recv_text = recv_data.decode("gbk")
        print(f"收到客户端{str(ip_port)}的信息:{recv_text}")
    # 9，关闭和当前客户端连接
    new_client_socket.close()

# 1，导入模块
# 2，创建套接字
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3，设置地址重用
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# 4，绑定端口
tcp_server_socket.bind(("", 8081))
# 5，设置监听，套接字由主动设置为被动
tcp_server_socket.listen(128)

while True:
    # 6，接受客户端连接
    new_client_socket, ip_port = tcp_server_socket.accept()
    print("欢迎新用户上线:" + str(ip_port))
    # recv_msg(new_client_socket, ip_port)

    # 创建线程
    t1 = threading.Thread(target=recv_msg, args=(new_client_socket, ip_port))
    # 设置线程守护
    t1.setDaemon(True)
    # 启动线程
    t1.start()

# 服务器基本不用关闭
# tcp_server_socket.close()
