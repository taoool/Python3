import socket


def send_msg(udp_socket):
    """发送信息的函数"""
    # 定义变量
    udp_ip = input("请输入接收方IP地址:\n")
    # 判断是否需要默认
    if len(udp_ip) == 0:
        udp_ip = "127.0.0.1"
        print("默认为本机ip:%s" % udp_ip)
    udp_den = input("请输入接收方端口号:\n")
    if len(udp_den) == 0:
        udp_den = 8082
        print("默认为本机端口:%s" % udp_den)
    udp_con = input("请输入要发送内容:\n")
    # 使用socket的sendto()发送信息
    udp_socket.sendto(udp_con.encode("gbk"), (udp_ip, int(udp_den)))


def recv_msg(udp_socket):
    """接受信息的函数"""
    # 使用socket接收数据
    recv_data, ip_port = udp_socket.recvfrom(1024)
    # 解码数据
    recv_text = recv_data.decode()
    # 输出显示
    print("接收到[%s]的信息：%s" % (str(ip_port), recv_text))

    
def main():
      """程序主入口"""
      # 1.创建套接字
      udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      # 2.绑定端口
      udp_socket.bind(('', 8082))
      # 3.打印菜单（循环）
      while True:
          print("\n\n********************")
          print("**** 1.发送信息 ****")
          print("**** 2.接受信息 ****")
          print("**** 3.退出系统 ****")
          print("********************")
          # 4.接受用户输入的选项
          sel_num = int(input("请输入选项：\n"))
          # 5.判断用户的选择并且调用对应的函数
          if sel_num == 1:
              send_msg(udp_socket)
          elif sel_num == 2:
              recv_msg(udp_socket)
          elif sel_num == 3:
              break
          else:
              print("请重新输入")
      # 6.关闭套接字
      udp_socket.close()


if __name__ == '__main__':
    main()




