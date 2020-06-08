#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 十六进制颜色选择器，使用滚动条Scale

from tkinter import *
from tkinter.colorchooser import *

def Hexstr2Int(colors: str) -> int:
    ret = 0
    pt = list(colors) #用列表一个字符一个字符存贮
    pt.reverse() #翻转列表
    idx = 0

    for i in pt:
        if i == 'A' or i == 'a':
            ret += int(i) * pow(16, idx)
        elif i == 'B' or i == 'b':
            ret += int(i) * pow(16, idx)
        elif i == 'C' or i == 'c':
            ret += int(i) * pow(16, idx)
        elif i == 'D' or i == 'd':
            ret += int(i) * pow(16, idx)
        elif i == 'E' or i == 'e':
            ret += int(i) * pow(16, idx)
        elif i == 'F' or i == 'f':
            ret += int(i) * pow(16, idx)
        else:
            ret += int(i) * pow(16, idx)
        idx += 1
    return ret

def bgUpdate(source):
    '''更改窗口颜色'''
    red = rSlider.get() #获取数据
    green = gSlider.get()
    blue = bSlider.get()

    myColor = "#%02x%02x%02x" % (red, green, blue) # 十六进制化

    root.config(bg=myColor) #更改界面背景色

def askcc():
    myColor = askcolor()
    print(myColor)
    tmps = myColor[1]
    tmps = tmps[1:] #将后面的颜色值取出

    redc = Hexstr2Int(tmps[0:2]) # 设置红色int
    greenc = Hexstr2Int(tmps[2:4]) # 设置绿色int
    bluec = Hexstr2Int(tmps[4:6]) # 设置蓝色int

    rSlider.set(redc) #重设
    gSlider.set(greenc)
    bSlider.set(bluec)
    
    root.config(bg=myColor[1]) # 重设

root = Tk()

root.title("Color Chooser")
root.geometry("360x240")

cc = Frame(root)
cc.pack(side=LEFT, anchor=NW)
rSlider = Scale(cc, from_=0, to=255, troughcolor="pink", command=bgUpdate)
gSlider = Scale(cc, from_=0, to=255, troughcolor="lightgreen", command=bgUpdate)
bSlider = Scale(cc, from_=0, to=255, troughcolor="lightblue", command=bgUpdate)
askBtn = Button(root, text="Using\nAskcolor", relief=SOLID, fg="royalblue",
                font=("Microsoft Yahei", 8, "normal"), command=askcc)

rSlider.pack(side=LEFT)
gSlider.pack(side=LEFT)
bSlider.pack(side=LEFT)
askBtn.pack(side=RIGHT,anchor=SE, fill=Y)

root.mainloop()
