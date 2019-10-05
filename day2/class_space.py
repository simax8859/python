global_fn = lambda p:print('执行全局空间lambda表达式，p参数', p)
class Category:
	cate_fn = lambda p:print('执行类命名空间lambda表达式，p参数', p)

# 调用全局空间内的global_fn，为参数p传入参数值
global_fn("test")
c = Category()
# 调用类命名空间内的cate_fn,Python自动绑定第一个参数
c.cate_fn()