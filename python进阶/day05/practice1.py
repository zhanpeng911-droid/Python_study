"""
通过TCP客户端发送消息：真牛!通过TCP服务器端接收消息，并打印出来。
"""

import socket
#创建服务端对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#定义端口号，ip地址
server_socket.bind(('127.0.0.1', 8080))
#定义监听数
server_socket.listen(5)
#接收来自客户端的消息
accept_socket, client_socket = server_socket.accept()
#将客户端来的消息限定长度为1024
recv_data_socket = accept_socket.recv(1024)
#将接受的消息进行转码
recv_data = recv_data_socket.decode()
#接收打印消息
print(f'recv_data: {recv_data}')
#释放资源
server_socket.close()














