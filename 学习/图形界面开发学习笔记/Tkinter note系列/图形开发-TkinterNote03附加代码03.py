#-*- coding: UTF-8 -*-
__author__ = '007'
__date__ = '2016/4/7'

from Tkinter import *
root = Tk() # 初始化Tk()
root.title("entry-test")    # 设置窗口标题
root.geometry("300x200")    # 设置窗口大小 注意：是x 不是*
root.resizable(width=True, height=False) # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True
var = Variable()
e = Entry(root, textvariable=var)
var.set("entry") # 设置文本框中的值
e.pack()   # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
root.mainloop() # 进入消息循环
