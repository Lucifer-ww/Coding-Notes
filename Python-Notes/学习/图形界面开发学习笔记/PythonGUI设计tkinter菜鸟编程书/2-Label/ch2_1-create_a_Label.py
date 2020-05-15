# -*- coding: UTF-8 -*-
#!/usr/bin/python3

from tkinter import *

root = Tk()
root.title("ch2_1")
label = Label(root, text="I LIKE TKINTER")
label.pack()  # 包装与定位组件
print(type(label))  # 传回Label数据类型

root.mainloop()
