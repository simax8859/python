import socket
import threading

# 定义保存所有socket的列表
socket_list = []
# 创建socket对象
ss = socket.socket()
# 将socket绑定到本机IP地址和端口
ss.bind(('192.168.56.1', 30000))
# 服务端开始监听来自客户端的连接
ss.listen()


def read_from_client(s):
    try:
        return s.recv(2048).decode('utf-8')
    # 如果捕获到异常，则表明该socket对应的客户端已经关闭
    except Exception:
        print("进入到删除socket")
        # 删除该socket
        socket_list.remove(s)


def server_target(s):
    try:
        # 采用循环不断地从socket中读取客户端发送过来的数据
        while True:
            content = read_from_client(s)
            if content is None:
                break
            print(content)
            for client_s in socket_list:
                client_s.send(content.encode('utf-8'))
    except Exception as e:
        print(e.strerror)


while True:
    # 此行代码会被阻塞，将一直等待别人的连接
    s, addr = ss.accept()
    socket_list.append(s)
    # 每当客户端连接后，都会启动一个线程为该客户端服务
    threading.Thread(target=server_target, args=(s,)).start()
