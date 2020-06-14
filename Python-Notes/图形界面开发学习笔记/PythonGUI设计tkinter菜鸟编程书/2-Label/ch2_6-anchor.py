# coding: UTF-8
from tkinter import *

root = Tk()
root.title("ch2_6")
root.geometry('100x100')
label = Label(root, text="I likt Tkinter", fg='blue',
              bg='yellow', height=3, width=15, anchor='se')
#anchor参数调整文字在标签内的位置，分九个位置

label.grid()
root.mainloop()
