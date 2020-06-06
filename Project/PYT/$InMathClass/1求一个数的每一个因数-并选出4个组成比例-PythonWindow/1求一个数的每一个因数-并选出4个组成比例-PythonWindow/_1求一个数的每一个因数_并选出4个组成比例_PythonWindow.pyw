#!/usr/bin/env python3
#coding=utf-8
from tkinter import *
import math
from datetime import datetime as dtdt

root = Tk()
root.geometry("200x80")

def method():
    note = TextEdit.get()
    num = int(note)
    '''
    for i in range(1, num + 1):
        print(i)
    '''

    nums = []
    primes = []
    for i in range(1, num + 1):
        if num % i == 0:
            nums.append(i)
    pass

inputFrame = Frame(root)
tiptop = Label(inputFrame, text="下方输入要分解的数字", bg="#FFCC99", fg="#99CC99", anchor=CENTER)
#直接拍出标签
tiptop.pack(anchor=N, side="top")

TextEdit = Entry(inputFrame, width=10, bg="lightyellow")
TextEdit.pack(anchor=CENTER, side="top")

okBtn = Button(inputFrame, width=5, text="确定", bg="blue", fg="white", command=method)
okBtn.pack(anchor=SE, side="right")

inputFrame.pack(anchor=NW, side=LEFT)

root.mainloop()
