import socket

PORT = 30000
# 定义每个数据报的大小最大为4KB
DATA_LEN = 4096

# 定义一个字符串数组，服务器端发送该数组的元素
books = ("疯狂Python讲义", "疯狂Swift讲义", "疯狂Java讲义", "疯狂哈哈哈")

# 通过type属性指定创建基于UDP协议的socket
s = socket.socket(type=socket.SOCK_DGRAM)
# 将该socket绑定到本机的指定IP地址和端口
s.bind(('192.168.56.1', PORT))
# 采用循环接收数据
for i in range(1000):
    # 读取s中的数据的发送地址
    data, addr = s.recvfrom(DATA_LEN)
    # 将接收到的内容转换成字符串后输出
    print(data.decode("utf-8"))
    # 从字符串数组中取出一个元素作为发送数据
    send_data = books[i % 4].encode('utf-8')
    # 将数据报发送给addr地址
    s.sendto(send_data, addr)
s.close()