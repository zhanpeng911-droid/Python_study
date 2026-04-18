"""
案例：演示TCP入门，即：服务器端给客户端发送1句话，客户端收到后，给出回执信息。

流程：
    1.  服务器端  =>  客户端发送，'Welcome to study socket!'
    2.  客户端接收到消息后，打印，并给出回执信息。 '消息已收到，So Easy!'
    3.服务端收到客户端的回执信息，打印即可

    服务器端，实现步骤：
        # 1 创建服务器端的socket对象
        # 2 连接服务器端的ip地址，端口号
        # 3 接收服务器端发过来的回执信息，记得转成字符串，并打印
        # 4 给服务器端发送一句话，二进制形式
        # 5 释放资源，关闭accept_socket

"""

import socket

# 1 创建服务器端的socket对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2 连接服务器端的ip地址，端口号
client_socket.connect(('127.0.0.1', 12306))
# 3 给服务器端发送一句话，二进制形式
while True:
    data = input('请输入要发送给服务器端的内容')
    client_socket.send(data.encode())
    #判断是否为886
    if data == '886':
        # 4 释放资源，关闭accept_socket
        client_socket.close()

















