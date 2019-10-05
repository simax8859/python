import selectors, socket

# 创建默认的selectors对象
sel = selectors.DefaultSelector()


# 负责舰艇“有数据可读”事件的函数
def read(skt, mask):
    try:
        # 读取数据
        data = skt.recv(1024)
        if data:
            # 将所读取的数据采用循环向每个socket发送一次
            for s in socket_list:
                s.send(data)    # Hope it won't block
        else:
            # 如果该socket已被对方关闭，则关闭该socket
            # 并将其从socket_list列表中删除
            print('关闭', skt)
            sel.unregister(skt)
            skt.close()
            socket_list.remove(skt)
    except Exception:
        print('关闭', skt)
        sel.unregister(skt)
        skt.close()
        socket_list.remove(skt)


socket_list = []


# 负责监听“有客户端连接进来”事件的函数
def accept(sock, mask):
    conn, addr = sock.accept()
    # 使用socket_list保存代表客户端的socket
    socket_list.append(conn)
    conn.setblocking(False)
    # 使用sel为conn的EVENT_READ事件注册read监听函数
    sel.register(conn, selectors.EVENT_READ, read)


sock = socket.socket()
sock.bind(('192.168.56.1', 30000))
sock.listen()
# 设置该socket是非阻塞的
sock.setblocking(False)
# 使用sel为sock的EVENT_READ事件注册accept监听函数
sel.register(sock, selectors.EVENT_READ, accept)
# 采用死循环不断提取sel事件
while True:
    events = sel.select()
    for key, mask in events:
        # 使用key的data属性获取为该事件注册的监听函数
        callback = key.data
        # 调用监听函数，使用key的fileobj属性获取被监听的socket对象
        callback(key.fileobj, mask)