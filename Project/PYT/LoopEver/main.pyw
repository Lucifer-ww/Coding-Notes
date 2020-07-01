'''
@Author: your name
@Date: 2020-06-24 09:16:11
@LastEditTime: 2020-06-24 09:50:01
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \Coding-Notes\Project\PYT\LoopEver\main.pyw
'''
from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("XXX")
root.geometry("300x180")

lb = Label(root, text="", font=("Microsoft yahei", 18, "bold"), bg="azure", fg="#333333", wraplength=300)
lb.pack()

def closeWindow():
    pass


def clw():
    tkinter.messagebox.showerror(title='别嘛',message='嘿嘿，关不掉！🤪')


btn = Button(root, text="关闭窗口", command=clw)
btn.pack()
root.protocol('WM_DELETE_WINDOW', closeWindow)
root.mainloop()
