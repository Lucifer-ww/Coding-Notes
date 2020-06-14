# -*- coding: UTF-8

from tkinter import *


#变量类别-最常用的字符串类别StringVar()

def changetxt():
	txt.set("hello world")



root = Tk()
root.geometry("200x150")




txt = StringVar()
txt.set("")
lt = Label(root, textvariable=txt, width=50, bg="azure", anchor=CENTER)

lt.pack(anchor=CENTER, side=TOP)



btn = Button(root, text="accept", command=changetxt)

btn.pack(anchor=CENTER, side=TOP)

root.mainloop()