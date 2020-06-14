#-*- coding: UTF-8 -*-
__author__ = '007'
__date__ = '2016/4/7'

from Tkinter import *
root = Tk() # 初始化Tk()
root.title("frame-test")    # 设置窗口标题
root.geometry("300x200")    # 设置窗口大小 注意：是x 不是*
root.resizable(width=True, height=False) # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True
Label(root, text="frame", bg="red", font=("Arial",15)).pack()
frm = Frame(root)
#left
frm_L = Frame(frm)
Label(frm_L, text="左上", bg="pink", font=("Arial",12)).pack(side=TOP)
Label(frm_L, text="左下", bg="green", font=("Arial",12)).pack(side=TOP)
frm_L.pack(side=LEFT)
#right
frm_R = Frame(frm)
Label(frm_R, text="右上", bg="yellow", font=("Arial",12)).pack(side=TOP)
Label(frm_R, text="右下", bg="purple", font=("Arial",12)).pack(side=TOP)
frm_R.pack(side=RIGHT)
frm.pack()   # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
root.mainloop() # 进入消息循环
