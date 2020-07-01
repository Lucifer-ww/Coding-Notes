'''
@Author: your name
@Date: 2020-06-26 14:21:48
@LastEditTime: 2020-06-26 14:33:11
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \Coding-Notes\Python-Notes\例程\TK_禁用最小化和还原test\main.pyw
'''
from tkinter import *

root = Tk()
root.state("zoomed")

Label(root, text='*******').pack()

def nnn():
    pass

def pad():
    Label(root, text="-------").pack()

root.protocol("WM_DELETE_WINDOW", nnn)
root.protocol("WM_TAKE_FOCUS", pad)
root.mainloop()