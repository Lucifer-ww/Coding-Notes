'''
@Author: your name
@Date: 2020-06-24 16:38:40
@LastEditTime: 2020-06-24 16:51:26
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \Coding-Notes\Project\PYT\Editor\TEST\LLL.pyw
'''
from tkinter import *
from tkinter.ttk import Frame, Style

root = Tk()
root.geometry("600x300")
style=Style()
style.theme_use("alt")
labelframe=Frame(root, width=300, height=180, relief="solid")
labelframe.pack()
Button(labelframe, text="存款").pack(anchor=W)
root.mainloop()
