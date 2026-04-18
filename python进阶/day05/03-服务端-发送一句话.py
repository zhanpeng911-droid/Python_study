"""
案例：演示TCP入门，即：服务器端给客户端发送1句话，客户端收到后，给出回执信息。

流程：
    1.  服务器端  =>  客户端发送，'Welcome to study socket!'
    2.  客户端接收到消息后，打印，并给出回执信息。 '消息已收到，So Easy!'
    3.服务端收到客户端的回执信息，打印即可

    服务器端，实现步骤：
        # 1 创建服务器端的socket对象
        # 2 绑定ip地址，端口号
        # 3 设置最大监听数
        # 4 具体监听动作，接收客户端请求，并获取1个socket对象，负责和该客户端的交互
        # 5 给客户端发送一句话，二进制形式
        # 6 接收客户端发过来的回执信息，记得转成字符串，并打印
        # 7 释放资源，关闭accept_socket

"""

import socket

# 1 创建服务器端的socket对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2 绑定ip地址，端口号
server_socket.bind(('127.0.0.1', 12303))
# 3 设置最大监听数
server_socket.listen(5)
# 4 具体监听动作，接收客户端请求，并获取1个socket对象，负责和该客户端的交互
#accept_socket:负责客户端交互的socket对象
#client_socket:客户的ip信息
accept_socket,client_socket = server_socket.accept()

# 5 给客户端发送一句话，二进制形式
accept_socket.send(b'Hello, client!')
# 6 接收客户端发过来的回执信息，记得转成字符串，并打印
#1024表示一次性接收客户端的长度，超出则无法接收
recv_data_bytes = accept_socket.recv(1024)
recv_data = recv_data_bytes.decode(encoding='utf-8')    #把二进制字符转成字符串
print(f'recv_data: {recv_data}')

# 7 释放资源，关闭accept_socket
accept_socket.close()
















