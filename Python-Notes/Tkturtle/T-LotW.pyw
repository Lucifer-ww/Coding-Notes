'''
@Author: your name
@Date: 2020-06-22 18:14:16
@LastEditTime: 2020-06-22 19:55:49
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \Coding-Notes\Python-Notes\Tkturtle\T-LotW.pyw
'''
from tkinter import *


def newTk():
    root2 = Tk()
    root2.geometry("150x90")
    root2.mainloop()

root = Tk()
root.geometry("300x180")
Button(root, text="New", command=newTk).pack()

root.mainloop()