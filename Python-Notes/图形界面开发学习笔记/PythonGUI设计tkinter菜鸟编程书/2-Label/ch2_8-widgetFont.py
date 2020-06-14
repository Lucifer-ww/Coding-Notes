# coding: UTF-8
from tkinter import *
root = Tk()
root.title("ch2_4")
label = Label(root, text="I Like tkinter", fg="blue",
              bg="yellow", height=3, width=15,
              font="Helvetic 20 bold")
#font参数设置字体为Helvetic，字号20，粗体，也可以换成别的，一共三个参数，也可以用一个元组包裹在一起
label.pack()
root.mainloop()
