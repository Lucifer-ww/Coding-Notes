#coding:UTF-8
#ch9.py fill
from tkinter import *

root = Tk()
root.title("expand")

Label(root, text="Tkinter", bg="lightyellow").pack(side=LEFT, fill=Y)
#第一个标签
#这些标签不需要保存在变量中，设置好直接布局
Label(root, text="wxPython", bg="lightgreen").pack(fill=X)

Label(root, text="PyQt", bg="lightblue").pack(fill=BOTH, expand=True) #设置可以变化

root.mainloop()
