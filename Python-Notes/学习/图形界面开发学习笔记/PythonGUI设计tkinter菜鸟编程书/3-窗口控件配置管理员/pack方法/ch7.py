#coding: UTF-8
#ch7.py anchor
from tkinter import *
root = Tk()
root.title("ch7.py")
root.geometry("300x180")
okbtn = Button(root, text="OK",
                font="Times 20 bold",
                fg="white", bg="blue")
okbtn.pack(anchor=S, side=RIGHT,
            padx=10, pady=10)
root.mainloop()