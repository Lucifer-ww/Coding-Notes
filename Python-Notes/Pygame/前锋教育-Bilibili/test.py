from tkinter import *

def doit():
    if lbtxt.get() == "Hel"
    lbtxt.set(2)

root = Tk()
root.geometry("50x40")
lbtxt=StringVar()
lbtxt.set("Hello")
lb = Label(root, textvariable=lbtxt, font=("Microsoft Yahei", 13), anchor=CENTER)
lb.pack(side=LEFT)

btn= Button(root, text="change", command=doit)

btn.pack(padx=5, side=LEFT)

root.mainloop()