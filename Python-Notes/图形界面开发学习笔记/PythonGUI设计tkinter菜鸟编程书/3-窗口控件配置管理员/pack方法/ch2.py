#coding:UTF-8

from tkinter import *

root = Tk()
root.title("普通设置控件")

Label(root, text="Tkinter", bg="lightyellow", width=15).pack(side=BOTTOM)
#第一个标签
#这些标签不需要保存在变量中，设置好直接布局
Label(root, text="wxPython", bg="lightgreen", width=15).pack(side=BOTTOM)

Label(root, text="PyQt", bg="lightblue", width=15).pack(side=BOTTOM)

root.mainloop()
