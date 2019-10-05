from tkinter import *

import random


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        # 定义字符串元组
        books = ('疯狂Python讲义', '疯狂Swift讲义', '疯狂kotlin讲义', '疯狂Java讲义', '疯狂Ruby讲义')
        for i in range(len(books)):
            # 生成三个随机数
            ct = [random.randrange(256) for x in range(3)]
            grayness = int(round(0.299 * ct[0] + 0.587 * ct[1] + 0.114 * ct[2]))
            # 将元组中的三个随机数格式化成十六进制数，转换成颜色格式
            bg_color = "#%02x%02x%02x" % tuple(ct)
            # 创建Label 设置背景色和前景色
            lb = Label(root,
                       text=books[i],
                       fg='White' if grayness < 125 else 'Black',
                       bg=bg_color)
            lb.place(x=20, y=36 + i * 36, width=180, height=30)


root = Tk()
root.title("Place布局")
# 设置窗口的大小和位置
# width x height + x_offset + y_offset
root.geometry("250x250+30+30")
App(root)
root.mainloop()
