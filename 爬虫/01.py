# from socket import *
#
# udp_Socket = socket(AF_INET, SOCK_DGRAM)
# #需要发送的信息
# send_data = 'i love you'
# #发送的地址
# udp_addr = ('192.168.3.100', 8080)
# #执行发送
# #gbk:windows一般的解码格式
# udp_Socket.sendto(send_data.encode('utf-8'), udp_addr)
# #关闭套接字
# udp_Socket.close()

# """udp接收数据"""
# from socket import *
# # 创建udp套接字对象
# udp_socket = socket(AF_INET, SOCK_DGRAM)
# # 定义接收方(接收数据)的地址
# udp_addr = ('192.168.3.100', 8080)
# # 定义发送的消息
# data = '你那边今天天气怎么样？'.encode('gbk')
# # 执行发送
# udp_socket.sendto(data, udp_addr)
# #接收对方发送的消息（接受服务器的消息）
# recv_data = udp_socket.recvfrom(1024)
# #本次接收的最大字节数
# print(recv_data)
# print(recv_data[0].decode('gbk'))
# print(recv_data[1])
# udp_socket.close()

# #绑定端口发送信息
# from socket import *
# # 创建套按字对象
# udp_docket = socket(AF_INET, SOCK_DGRAM)
# # 绑定套接字本地端口
# udp_docket.bind(('', 9999))
# # ip地址一般不用写，表示本机的任何一个IP
# data = '么么哒'
# udp_addr = ('192.168.3.100', 8080)
# udp_docket.sendto(data.encode('gbk'), udp_addr)
# recv_data = udp_docket.recvfrom(1024)
#
# print(recv_data)


# from socket import *
# # 创建tcp_socket对象
# tcp_socket = socket(AF_INET, SOCK_STREAM)
# # 建立和服务器的连接
# # 需求：IP地址，端口号
# ip_port = ('192.168.3.101', 8080)
# #与udp客户端程序的区别在于建立连接
# tcp_client_socket = tcp_socket.connect(ip_port)
# """将数据从客户端发送给服务器"""
# for i in range(4):
#     data = '我喜欢你！'
#     # 将需要传输的数据转换成二进制类型
#     data_bytes = data.encode('gbk')
#     # 将数据发送给服务器
#     tcp_socket.send(data_bytes)
# """接收服务器传递过来的数据"""
# recv_data = tcp_socket.recv(1024)
# # 接收服务器发送过来的数据，最大接收1024个字节
# print(f"接收到服务器发送过来的数据：{recv_data.decode('gbk')}")
# # 关闭套接字
# tcp_socket.close()

# from socket import *
#
# tcp_socket = socket(AF_INET, SOCK_STREAM)
# # 设置端口号复用，程序退出，端口号立即释放
# tcp_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# # 绑定IP地址和端口
# ip_port = ('', 60010)
# tcp_socket.bind(ip_port)
# # 设置监听：128最大等待连接数
# tcp_socket.listen(128)
#
# try:
#     # 若有新的客户端来链接这个服务端，那么就产生一个新的套接字专门为这个客户端服务
#     client_socket, client_addt = tcp_socket.accept()
#     print(f"接受到来自{client_addt}的连接")
#
#     # 修正：使用client_socket接收数据
#     recv_data = client_socket.recv(1024)
#     print(f"客户端发来：{recv_data.decode('gbk')}")
#
#     # 关闭客户端套接字
#     client_socket.close()
# finally:
#     # 关闭主监听套接字
#     tcp_socket.close()

# import requests
# url = 'https://www.baidu.com'
# response = requests.get(url)
# # print(response.content.decode())
# #
# # print(response.text)
# #获取响应的url地址
# print(response.url)
# #获取响应状态码
# print(response.status_code)
# #获取响应对应的请求头
# print(response.request.headers)
# #获取响应头
# print(response.headers)

# """发送带参数的请求"""
#


#user_agent:浏览器的身份，目的：欺骗服务器
#Cookie：用户的缓存，缓存的用户信息或者是浏览记录信息
#Host：服务器域名
#referer：来源，目的，告诉对方服务器这个请求的来源

"""无痕窗口"""
# 无痕模式下的对地址访问成功，代表该地址的headers只需要一个ua一个键值对
# 通过无痕模式来判断地址的访问需要那些headers的键值对

#非无痕模式下
#打开一个新的浏览器窗口访问地址，能够访问，说明header中，需要ua，cookie即可

#除了上述操作，地址不能够访问，需要携带referer字段































