#!/usr/bin/env python3
# -*- cooding: utf-8 -*-

from tkinter import *



def bindsButtons():
    pass
def setButtons():
    btn1img = PhotoImage(file="IMG/numbers1.png")
    btn1 = Button(root, text=" 1 ", image=btn1img)
    btn1.pack()


root = Tk()
root.geometry("200x100")
setButtons()





root.mainloop()