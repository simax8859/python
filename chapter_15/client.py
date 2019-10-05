# 导入socket模块
import socket

# 创建socket对象
s = socket.socket()
# 连接远程服务器
s.connect(('192.168.56.1', 30000))

print('---%s---' % s.recv(1024).decode('utf-8'))
s.close()