import threading
from concurrent.futures import ThreadPoolExecutor

# 定义线程局部变量
example = threading.local()


# 定义准备作为线程执行体使用的函数
def action(max):
    for i in range(max):
        try:
            example.x += i
        except:
            example.x = i
        # 访问example的x的值
        print('%s mydata.x 的值为：%d' % (threading.current_thread().name, example.x))


with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(action, 10)
    pool.submit(action, 10)
