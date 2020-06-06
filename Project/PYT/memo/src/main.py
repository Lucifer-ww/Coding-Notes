#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from tkinter import *
import csv
from PIL import Image, ImageTk
from tkinter import scrolledtext


def newPage():
    pass


def deletePage():
    pass

def testHide():
    buttonframe.pack_forget()
def testShow():
    buttonframe.pack(anchor=SE, side=RIGHT)

root = Tk()
root.state("zoomed")
# 滚动条或其他cursor参数，可使用arrow箭头，或target的眼睛形状指针
path_log1 = r"E:\ProgramThomas\Coding-Notes\Project\PYT\memo\log\Label_nr.log"
# 记录log-每一个便签的内容路径记录

log = open(path_log1, 'a+')

# 设置新建 和 删除按钮
# 加入框架放入按钮
buttonframe = Frame(root)
NewImg = PhotoImage(
    file="E:/ProgramThomas/Coding-Notes/Project/PYT/memo/img/xj.png")
New = Button(buttonframe, image=NewImg, relief=RIDGE, fg="white", bg="orange", command=newPage)
deleteImg = PhotoImage(file="E:/ProgramThomas/Coding-Notes/Project/PYT/memo/img/sc.png")
Delete = Button(buttonframe, image=deleteImg, relief=RIDGE, fg="white", bg="lightblue", command=deletePage)
buttonframe.pack(anchor=NW)
New.pack(side=LEFT, padx=10, pady=10)
Delete.pack(side=LEFT, pady=10)

testButtonFrame = Frame(root)
testButton1 = Button(testButtonFrame, text="test colse", bg="lightgreen", command=testHide)
testButton1.pack(anchor=SE, side=RIGHT)
testButton2 = Button(testButtonFrame, text="test show", bg="#FF6633", command=testShow)
testButton2.pack(anchor=SE, side=RIGHT)
testButtonFrame.pack(anchor=SE, side=RIGHT)


root.mainloop()
