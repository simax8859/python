from concurrent.futures import ThreadPoolExecutor
import threading
import time


# 定义一个准备作为线程任务的函数
def action(max):
    my_sum = 0
    for i in range(max):
        print(threading.current_thread().name + '   ' + str(i))
        my_sum += i
    return my_sum


# 创建一个包含两个线程的线程池
pool = ThreadPoolExecutor(max_workers=2)
# 向线程池中提交一个任务，50会作为action()函数的参数
future1 = pool.submit(action, 50)
# 向线程池中提交一个任务，100会作为action()函数的参数
future2 = pool.submit(action, 100)
# 判断future1代表的任务是否结束
print(future1.done())
time.sleep(3)
# 判断future2代表的任务是否结束
print(future2.done())
# 查看future1代表的任务返回的结果
print(future1.result())
# 查看future2代表的任务返回的结果
print(future2.result())
# 关闭线程池
pool.shutdown()


# 使用map来启动线程并收集线程的执行结果，不仅具有代码简单的有点，而且虽然程序会以并发方式来执行action()函数，但最后收集的action()
# 函数的执行结果，依然与传入参数的结果保持一致。