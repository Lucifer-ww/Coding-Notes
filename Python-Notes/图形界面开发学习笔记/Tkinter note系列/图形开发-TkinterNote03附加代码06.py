#-*- coding: UTF-8 -*-
__author__ = '007'
__date__ = '2016/4/7'

from Tkinter import *
root = Tk()
root.title("listbox-test")
root.geometry()
def print_item(event):
    print lb.get(lb.curselection())
var = StringVar()
lb = Listbox(root, listvariable = var)
list_item = [1,2,3,4]
for item in list_item:
    lb.insert(END,item)
lb.delete(2,4)
var.set(('a','b','c','d'))
print var.get()
lb.bind('<ButtonRelease-1>',print_item)
lb.pack()
root.mainloop()
