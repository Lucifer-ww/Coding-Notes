'''
@Author: your name
@Date: 2020-06-23 19:40:31
@LastEditTime: 2020-06-23 20:04:24
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \Coding-Notes\Python-Notes\图形界面开发学习笔记\PythonGUI设计tkinter菜鸟编程书\TkCanvasPro\mainwindow.pyw
'''

from tkinter import *
from random import *

import time

class Ball:
    def def __init__(self, canvas, color, winW, winH, racket):
        # 初始化
        self.canvas = canvas # 画布
        self.racket = racket
        self.id = canvas.creat_oval(0, 0, 30, 30, fill=color) # 创建球对象
        self.canvas.move(self.id, winW/2, winH/2) # 设计球最初位置
        startPos = [-4, -3, -2, -1, 1, 2, 3, 4] # 球最初x轴位移的随机数列表
        shuffle(startPos) # 随机打乱
        self.x = startPos[0] # 球最初水平移动单位
        self.y = -step # 球先往上垂直移动单位
        self.notTouchBottom = True # 未接触画布底端