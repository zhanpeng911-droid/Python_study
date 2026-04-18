"""
案例：演示TCP入门，即：服务器端给客户端发送1句话，客户端收到后，给出回执信息。

流程：
    1.  客户端  =>  服务器端，上传一个文件
    2.  服务器端收到后，保存到服务器的某个路径下    例如./data/这里

    服务器端，实现步骤：
    1. 创建客户端的Socket对象.
    2. 连接服务器端的 Ip地址 和 端口号.
    # 3. 通过 open()函数，关联：数据源文件的路径.
    # 4. (循环)接收文件中的内容，并将其写给服务器端.
    # 5. 如果接收完毕，就结束读取，即：break
    6. 关闭客户端即可.

"""

#案例：演示 长连接，即：客户端不断地给服务器发送消息，服务器端接收消息并打印，客户端发送886结束发送

import socket

# 1 创建服务器端的socket对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2 绑定ip地址，端口号
server_socket.bind(('127.0.0.1', 12306))
# 3 设置最大监听数
server_socket.listen(5)

# 4 具体监听动作，接收客户端请求，并获取1个socket对象，负责和该客户端的交互
#accept_socket:负责客户端交互的socket对象
#client_socket:客户的ip信息
accept_socket,client_info = server_socket.accept()

#5 通过open函数，关联：目的地文件的路径
with open('./data/hg.txt','wb') as f:
    #6. (循环)接收文件中的内容，并将其写给服务器端.
    while True:
        #接收客户端写过来的数据
        data = accept_socket.recv(1024)

        if len(data) <= 0:
            break
# 8 释放资源，关闭accept_socket
accept_socket.close()






















