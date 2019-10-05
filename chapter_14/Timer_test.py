from threading import Timer
import time


# 定义总共需要输出几次
count = 0


def print_time():
    print("当前事件： %s" % time.ctime())
    global t, count
    count += 1
    # 如果count小于10.开始下一次调度
    if count < 10:
        t = Timer(1, print_time)
        t.start()


# 指定1s后执行hello函数
t = Timer(1, print_time)
t.start()