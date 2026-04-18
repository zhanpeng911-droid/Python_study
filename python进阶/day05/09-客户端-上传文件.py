"""
案例：演示TCP入门，即：服务器端给客户端发送1句话，客户端收到后，给出回执信息。

流程：
    1.  客户端  =>  服务器端，上传一个文件
    2.  服务器端收到后，保存到服务器的某个路径下    例如./data/这里

    客户端，实现步骤：
    1. 创建客户端的Socket对象.
    2. 连接服务器端的 Ip地址 和 端口号.
    # 3. 通过 open()函数，关联：数据源文件的路径.
    # 4. (循环)读取文件中的内容，并将其写给服务器端.
    # 5. 如果读取完毕，就结束读取，即：break
    6. 关闭客户端即可.

"""

import socket

# 1 创建服务器端的socket对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2 连接服务器端的ip地址，端口号
client_socket.connect(('127.0.0.1', 12306))

# 3. 通过 open()函数，关联：数据源文件的路径.
with open(r'd:\aaa.txt', 'rb') as f:
    # 4. (循环)读取文件中的内容，并将其写给服务器端.
    while True:
        data = f.read(1024)
        # 5. 如果读取完毕，就结束读取，即：break
        if not data:
            break
        #将其写给服务器端
        client_socket.send(data)

# 6 释放资源，关闭accept_socket
client_socket.close()




















