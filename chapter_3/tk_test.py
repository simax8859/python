from tkinter import *


# # 创建TK对象，TK 代表窗口
# root = Tk()
#
# # 设置窗口标题
# root.title("嘻嘻嘻嘻")
#
# # 创建Label对象，第一个参数指定将该Label放入root内
# w = Label(root, text="Hello TKinter!")
#
# # 调用pack进行布局
# w.pack()
#
# # 启动主窗口
# root.mainloop()

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        # 调用initWidgets()方法初始化界面
        self.initWidgets()

    def initWidgets(self):
        # 创建Label 对象，第一个参数指定将该Label放入root内
        w = Label(self)
        # 创建一个位图
        bm = PhotoImage(file='serial.png')
        # 必须用一个不会被释放的变量引用该图片，否则该图片会被回收
        w.x = bm
        # 设置显示的图片是bm
        w['image'] = bm
        w.pack()
        # 创建Button对象， 第一个参数指定将该Button放入root内
        okButton = Button(self, text='确定')
        okButton['background'] = 'yellow'
        # okButton.configure(backgroud='yellow') # 与上面代码作用相同
        okButton.pack()


# 创建Application对象
app = Application()


# Frame有一个默认的master属性，该属性值是TK对象（窗口）
print(type(app.master))
# 通过master属性来设置窗口标题
app.master.title('窗口标题')
# 启动主窗口的消息循环
app.mainloop()
