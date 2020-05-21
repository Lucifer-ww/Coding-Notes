# -*- coding: utf-8 -*-

from tkinter import *

def calc():
    s = et.get()
    out.configure(text='Answer:' + str(eval(s)))

root = Tk()
root.title('使用eval函数计算表达式')
root.geometry('300x100')
lb = Label(root, text='Input')
lb.pack()
et = Entry(root, width = 25, bg = 'azure')
et.pack()
out = Label(root)
out.pack()
btn = Button(root,width=10, text='calc', bg='lightyellow', command=calc)
btn.pack(pady=5)

root.mainloop()