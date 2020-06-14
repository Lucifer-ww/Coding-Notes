# -*- coding: UTF-8

from tkinter import *
#变量类别-最常用的字符串类别StringVar()
def changetxt():
	tmp = txt.get()
	if tmp == "":
		txt.set("Hello World")
	else:
		txt.set("")
root = Tk()
root.geometry("200x150")
txt = StringVar()
txt.set("")
lt = Label(root, textvariable=txt, width=50, height=3, relief=RAISED, bg="azure", anchor=CENTER)
lt.pack(anchor="center", side=TOP)
btn = Button(root, text="accept", command=changetxt)
btn.pack(anchor="center", side=TOP)
root.mainloop()