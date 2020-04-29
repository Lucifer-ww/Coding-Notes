#-*- coding: UTF-8 -*-
__author__ = '007'
__date__ = '2016/4/7'

from Tkinter import *
root = Tk() # 初始化Tk()
root.title("button-test")    # 设置窗口标题
root.geometry()    # 设置窗口大小 注意：是x 不是*

def printhello():
    t.insert(END,"hello\n")
t = Text()
t.pack()   # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
Button(root, text="press", command=printhello).pack()
root.mainloop() # 进入消息循环
