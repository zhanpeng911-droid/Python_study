"""
扩展：长连接和短链接


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

while True:
    # 5 接收客户端发过来的回执信息，记得转成字符串，并打印
    #1024表示一次性接收客户端的长度，超出则无法接收
    recv_data_bytes = accept_socket.recv(1024)
    recv_data = recv_data_bytes.decode(encoding='utf-8')    #把二进制字符转成字符串
    print(f'recv_data: {recv_data}')
    print(f'服务器端收到{client_info}的回执信息：{recv_data}')

    #6.如果接收到的消息是886，就结束程序
    if recv_data == '886':
        # 7 释放资源，关闭accept_socket
        accept_socket.close()






















