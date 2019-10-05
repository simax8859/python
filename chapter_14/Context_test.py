import multiprocessing
import os


def foo(q):
    print('被启动的新进程：（%s）' % os.getpid())
    q.put('Python')


if __name__ == '__main__':
    # 设置使用fork的方式启动进程，并获取Context对象
    ctx = multiprocessing.get_context('fork')
    # 接下来就可以使用Context对象来代替multiprocessing模块
    q = ctx.Queue()
    # 创建进程
    mp = ctx.Process(target=foo, args=(q,))
    mp.start()
    # 获取队列中的消息
    print(q.get())
    mp.join()
    