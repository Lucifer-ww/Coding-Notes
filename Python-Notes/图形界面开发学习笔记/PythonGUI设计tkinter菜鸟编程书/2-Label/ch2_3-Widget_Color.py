# coding: UTF-8
#使用Label标签显示 'I Like Tkinter'，并使用前景色和背景色
from tkinter import *

root = Tk()
root.title("ch2_3")
label = Label(root, text="I Like Tkinter",
                fg ="blue", bg = "yellow")
# fg参数是前景色，bg是背景色
label.pack()

root.mainloop()