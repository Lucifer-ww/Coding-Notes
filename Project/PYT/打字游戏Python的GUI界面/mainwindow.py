# coding: UTF-8
#!/usr/bin/python3

from tkinter import *

root = Tk()
root.title("打字游戏GUI")
root.iconbitmap("iconbitmap.ico")
root.geometry("500x400")  # 779*655
lb = Label(root, bitmap="hourglass",
           compound="left",
           cursor="target",
           text="tkinter",
           fg="blue", bg="yellow",
           anchor=CENTER, font=("Helvetic", 20, "bold")
           )
# r"E:\ProgramThomas\Coding-Notes\Project\PYT\打字游戏Python的GUI界面\resource\BITMAP_TITLE.ico"

lb.pack()
root.mainloop()
