import threading


class Account:
    def __init__(self, account_no, balance):
        # 封装账户编号和账户余额两个成员变量
        self.account_no = account_no
        self._balance = balance
        self.lock = threading.Lock
        self.event = threading.Event

    def getBalance(self):
        return self._balance

    def drwa(self, draw_amount):
        # 加锁
        self.lock.acquire()
        if self.event.is_set():
            # 执行取操作
            print(threading.current_thread().name + "取钱" + str(draw_amount))
            self._balance -= draw_amount
            print("账户余额为：" + str(self._balance))
            # 将Event的内部旗标设置为False
            self.event.clear()
            # 释放锁
            self.lock.release()
            # 阻塞当前线程
            self.event.wait()
        else:
            # 释放锁
            self.lock.release()
            # 阻塞当前线程
            self.event.wait()

    def deposit(self, deposit_amount):
        # 加锁
        self.lock.acquire()
        # 如果Event的内部旗标为False，则表明账户中还没有人存钱进去
        if not self.event.is_set():
            # 执行存款操作
            print(threading.current_thread().name + "存钱" + str(deposit_amount))
            self._balance -= deposit_amount
            print("账户余额为：" + str(self._balance))
            # 将Event的内部旗标设置为True
            self.event.set()
            # 释放锁
            self.lock.release()
            # 阻塞当前线程
            self.event.wait()
        else:
            # 释放锁
            self.lock.release()
            # 阻塞当前线程
            self.event.wait()