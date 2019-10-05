"""Pack布局管理器"""
import tkinter
from tkinter import *

# 创建窗口并设置窗口标题
root = Tk()
help(tkinter.Label.pack)
# 设置窗口标题
root.title('Pack布局')
for i in range(3):
    lab = Label(root, text="第%d个Label" % (i + 1), bg='#eeeeee')
    # 调用pack进行布局
    lab.pack()
# 启动主窗口的消息循环
root.mainloop()
