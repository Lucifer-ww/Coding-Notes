import tkinter
from tkinter import ttk

root = tkinter.Tk()
root.geometry("300x180")
b1 = tkinter.Button(root, text='xxx')
b1.pack()
b2 = ttk.Button(root, text='yyy')
b2.pack()
root.mainloop()
