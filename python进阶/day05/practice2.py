"""
通过TCP客户端发送消息：真牛!通过TCP服务器端接收消息，并打印出来。
"""

import socket
#创建服务端对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#定义端口号，ip地址
client_socket.connect(('127.0.0.1', 8080))
#将接受的消息进行转码
client_socket.send('真好'.encode())
#释放资源
client_socket.close()

















