import socket

# 2. 创建socket对象.
# 参1：Address Family，地址族，即：表示用何种IP规则来解析，例如：IPv4，IPv6...    AF_INET 代表 IPV4
# 参2：表示传输方式，Stream(流)的意思，表示用：字节流(二进制形式)传输数据.

cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # client(客户端)

#3.打印socket对象，看是否创建成功
print(cli_socket)

#释放资源
cli_socket.close()



























