#coding: UTF-8
#ch8.py anchor + NO BTN
from tkinter import *
root = Tk()
root.title("ch7.py")
root.geometry("300x180")
okbtn = Button(root, text="OK",
               font="Times 20 bold",
               fg="white", bg="blue")
okbtn.pack(anchor=S, side=RIGHT,
           padx=10, pady=10)
nobtn = Button(root, text = "NO",
                font="Times 20 bold",
                fg="white", bg="red")
nobtn.pack(anchor=S, side=RIGHT,
            pady=10)
root.mainloop()
