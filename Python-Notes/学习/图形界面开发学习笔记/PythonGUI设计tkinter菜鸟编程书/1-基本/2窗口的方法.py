# -*- coding: UTF-8 -*-
import tkinter

root = tkinter.Tk()
root.title("TEST tk window") #标题方法，更改标题，字符串类型
root.geometry("300x160") #设置窗口大小
root.maxsize(400, 400) #最大窗口大小，设置拖拽的最大值
root.minsize(100, 100) #最小窗口大小，设置拖拽的最小值
root.configure(bg="yellow") #背景颜色方法，更改背景颜色

root.resizable(True, True) #设置可不可以更改窗口大小，第一个参数是宽，第二个是高，True就是可拖拽
root.mainloop()
