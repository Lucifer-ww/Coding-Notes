#-*- coding: UTF-8 -*-
__author__ = '007'
__date__ = '2016/4/7'

from Tkinter import *
root = Tk() # 初始化Tk()
root.title("text-test")    # 设置窗口标题
root.geometry("300x200")    # 设置窗口大小 注意：是x 不是*
root.resizable(width=True, height=False) # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True
t = Text(root)
t.insert('1.0',"text1\n")   # 插入
t.insert(END,"text2\n") # END:这个Textbuffer的最后一个字符
t.insert('1.0',"text3\n")
#t.delete('1.0','2.0')   # 删除
t.pack()   # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
root.mainloop() # 进入消息循环
