# 导入模块
import socket
# 创建套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 设置广播权限(套接字默认不允许发送广播，需要开启相关权限)
# udp_socket.setsockopt(套接字，属性，属性值)
# socket.SOL_SOCKET  当前套接字
# socket.SO_BROADCAST  广播属性
udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
# 发送数据
udp_socket.sendto("哈哈，打不过我把".encode("gbk"), ("192.168.217.255", 8080))
# udp_socket.sendto("哈哈，打不过我把".encode("gbk"), ("255.255.255.255", 8080))
# 关闭套接字
udp_socket.close()




