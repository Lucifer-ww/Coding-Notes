# coding: UTF-8
from tkinter import *

root = Tk()
root.title("ch2_6")
label = Label(root, text="I likt Tkinter", fg='blue',
              bg='yellow', height=3, width=15, anchor='se', wraplength=40)
#wraplength参数是在多少个像素后换行，单位是像素
label.pack()
root.mainloop()
