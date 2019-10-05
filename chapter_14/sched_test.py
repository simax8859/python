import sched, time
import threading

# 定义线程调度器
s = sched.scheduler()


# 定义被调度的函数
def print_time(name='default'):
    print("%s 的时间： %s" % (name, time.ctime()))


print('主线程：', time.ctime())
# 指定10s后开始执行那个函数
s.enter(10, 1, print_time)
s.enter(5, 2, print_time, argument=('位置参数',))
s.enter(5, 1, print_time, kwargs={'name': '关键字参数'})

# 执行调度的任务
s.run()
print('主线程：', time.ctime())
