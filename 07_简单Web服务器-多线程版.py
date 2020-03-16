"""
TCP服务端
1，导入模块
2，创建套接字
3，设置地址重用
4，绑定端口
5，设置监听，让套接字由主动变为被动接收
6，接受客户端连接 定义函数 request_handler()
7，接收客户端游览器发送的请求协议
8，判断协议是否为空
9，拼接响应的报文
10，发送发送响应报文
11，关闭操作

"""

import socket
from application import app_基础框架2
import sys
import threading

"""
1，在类的初始化方法中配置当前的项目
{"2048":"./2048", "植物大战僵尸v1":"./zwdzjs-v1", ...}
2， 在类增加一个初始化项目配置的方法 init_project()
2.1 显示所有可以发布的游戏 菜单
2.2 接收用户的选择
2.3 根据用户的选择发布指定的项目 (保存用户选择的游戏对应的本地目录)
3， 更改Web服务器打开的文件目录
"""


class WebServer(object):
    # 初始化方法
    def __init__(self, port):
        # 1，导入模块
        # 2，创建套接字
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 3，设置地址重用
        #                               当前套接字         地址重用         值True
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 4，绑定端口
        tcp_server_socket.bind(("", port))
        # 5，设置监听，让套接字由主动变为被动接收
        tcp_server_socket.listen(128)
        # 定义实例属性，保存套接字
        self.tcp_server_socket = tcp_server_socket

        # 定义类的实例属性，project_dict 初始化为空
        self.projects_dict = dict()
        # 定义实例属性，保存要发布的路径
        self.current_dir = ""

        self.projects_dict['植物大战僵尸-普通版'] = "zwdzjs-v1"
        self.projects_dict['植物大战僵尸-外挂板'] = "zwdzjs-v2"
        self.projects_dict['保卫萝卜'] = "tafang"
        self.projects_dict['2048'] = "2048"
        self.projects_dict['读心术'] = "dxs"

        # print(self.projects_dict)

        # 调用初始化游戏项目的方法
        self.init_project()


    # 添加一个初始化项目的方法
    def init_project(self):
        # 2.1 显示所有可以发布的游戏 菜单
        # list(self.projects_dict.keys()) 取出字典的key 并且转换为列表
        keys_list = list(self.projects_dict.keys())
        # 遍历显示所有的key
        # enumerate(keys_list)
        # {(0, '植物大战僵尸v1'), (1, '植物大战僵尸v2') ...}
        for index, game_name in enumerate(keys_list):
            print("%d.%s" % (index, game_name))
        # 2.2 接收用户的选择
        sel_no = input("请选择要发布的游戏序号:\n")
        # 2.3 根据用户的选择发布指定的项目(保存用户选择的游戏对应的本地目录)
        # 根据用户的选择，得到游戏的名称(字典的ke)
        key = keys_list[int(sel_no)]
        # 根据字典的key 得到项目的具体路径
        self.current_dir = self.projects_dict[key]


    def start(self):
        """启动web服务器"""
        while True:
            # 6，接受客户端连接 定义函数 request_handler()
            new_client_socket, ip_port = self.tcp_server_socket.accept()
            # 调用功能函数处理请求并且响应
            # self.request_handler(new_client_socket, ip_port)

            # 创建一个线程
            t1 = threading.Thread(target=self.request_handler, args=(new_client_socket, ip_port))
            # 设置线程守护
            t1.setDaemon(True)
            # 启动线程
            t1.start()

            
    def request_handler(self, new_client_socket, ip_port):
        """接受信息，并且做出响应"""
        # 7，接收客户端游览器发送的请求协议
        recv_data = new_client_socket.recv(1024)
        # 8，判断协议是否为空
        if not recv_data:
            print(f"{ip_port}客户端已下线！")
            new_client_socket.close()
            return

        # 使用 application 文件夹 app 模块的 application() 函数处理
        response_data = app_基础框架2.appllication(self.current_dir, recv_data, ip_port)

        # 10，发送发送响应报文
        new_client_socket.send(response_data)
        # 11，关闭当前连接
        new_client_socket.close()


def main():
    """主函数"""

    """
    1，导入sys 模块
    2，判断参数格式是否正确
    4，判断端口号是否是一个数字
    5，获取端口号
    6，在启动Web服务器的时候，使用指定的端口
    """
    # print(sys.argv)
    # 2，判断参数格式是否正确
    if len(sys.argv) != 2:
        print("启动失败，参数格式错误！正确格式：python xxx.py 端口号")
        return
    # 4，判断端口号是否是一个数字
    if not sys.argv[1].isdigit():
        print("启动失败，端口号不是一个纯数字!")
        return
    # 5，获取端口号
    port = int(sys.argv[1])
    # 6，在启动Web服务器的时候，使用指定的端口

    # 创建WebServer类的对象
    ws = WebServer(port)
    # 对象.start() 启动web服务器
    ws.start()


if __name__ == '__main__':
    main()

