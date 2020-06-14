# coding: UTF-8
from tkinter import *
root = Tk()
root.title("ch2_4")
label = Label(root, text="I Like tkinter", fg="blue",
              bg="yellow", height=3, width=15)
# 新加入的height和width参数分别是高和宽
label.pack()
root.mainloop()
