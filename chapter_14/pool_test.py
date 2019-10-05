import multiprocessing
import time
import os


def action(name='default'):
    print('(%s)进程正在执行，参数为： %s' % (os.getpid(), name))
    time.sleep(3)


if __name__ == '__main__':
    # 创建包含4个进程的进程池
    pool = multiprocessing.Pool(processes=4)
    # 将action分3次提交给进程池
    pool.apply_async(action)
    pool.apply_async(action, args=('位置参数',))
    pool.apply_async(action,  kwds={'name': '位置参数'})
    pool.close()
    pool.join()