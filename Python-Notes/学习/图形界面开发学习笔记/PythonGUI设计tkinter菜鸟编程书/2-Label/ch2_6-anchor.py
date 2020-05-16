# coding: UTF-8
from tkinter import *

root = Tk()
root.title("ch2_6")
label = Label(root, text="I likt Tkinter", fg='blue',
              bg='yellow', height=3, width=15, anchor='se')

label.pack()
root.mainloop()
