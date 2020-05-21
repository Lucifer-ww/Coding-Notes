# coding: utf-8
from tkinter import *

root = Tk()

def calc():
    for i in s:
        if i == 'c':
            lbmark['bg'] = 'green'
        else:
            lbmark['bg'] = 'red'

s = 'abcdef'
lbmark = Label(root, text=s, bg='azure')

calc()

lbmark.grid()
root.mainloop()