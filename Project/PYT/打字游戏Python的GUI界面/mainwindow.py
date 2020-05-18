# coding: UTF-8
#!/usr/bin/python3

from tkinter import *

root = Tk()
root.title("打字游戏GUI")
root.iconbitmap("iconbitmap.ico")
root.geometry("500x400")  # 779*655
lb = Label(root, text="tkinter",
           fg="blue", bg="yellow",
           anchor=CENTER, font=("Helvetic", 20, "bold"))
lb.pack()
root.mainloop()
