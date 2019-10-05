import os
'''在window系统下不支持使用os.fork()这个方法'''
print('父进程(%s) 开始执行' % os.getpid())

# 开始fork一个子进程
# 从这行代码开始，下面的代码都会被两个进程执行

pid = os.fork()
print('进程进入： %s' % os.getpid())

# 如果pid为0 ，则表明是子进程
if pid == 0 :
    print('子进程，其ID是（%s），父进程ID为（%s）' % (os.getpid(), os.getppid()))
else:
    print('我 （%s）创建的子进程ID为（%s）.' % (os.getpid(),pid))

print('进程结束： %s' % os.getpid())