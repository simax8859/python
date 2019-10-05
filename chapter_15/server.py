# 导入socket模块
import socket

# 创建socket对象
s = socket.socket()

# socket绑定到本机IP地址和端口
s.bind(('192.168.56.1', 30000))
# 服务器端开始舰艇来自客户端的连接
s.listen()

while True:
    # 每当接收到客户端socket的请求时，该方法就返回对应的socket和远程地址
    c, addr = s.accept()
    print(c)
    print('连接地址：', addr)
    c.send('您好，您收到了服务器的新年祝福！'.encode('utf-8'))
    # 关闭连接
    c.close()