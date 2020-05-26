# -*- coding: UTF-8 -*-
#!/usr/bin/python3
'''
目的：创建一个由tkinter制作的窗口中显示一个标签
'''
from tkinter import *

root = Tk() 
root.title("ch2_1") #设置标题
label = Label(root, text="I LIKE TKINTER") #text参数是设置文本，将这个标签存储在label变量中
label.pack()  # 包装与定位组件
print(type(label))  # 传回Label数据类型

root.mainloop()
