#!usr/bin/env python3
# -*- coding: UTF-8 -*-

from tkinter import *

window = Tk()
window.title("添加gif")

html_gif = PhotoImage(file="小埋.gif")
label = Label(window, image = html_gif)
label.pack()

window.mainloop()