# coding: UTF-8
#!/usr/bin/python3

from tkinter import *
import random
import time

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
lb2 = Label(root, bitmap = "question",
            compound = "left",
            text="提示：打字游戏，点击 开始 按钮即开始计时，最后点击 提交 按钮即可",
            fg = "#FF0000", bg = "lightyellow",
            )
characters = [] #0~26
for i in range(0, 50):
    tmp = random.randint(0, 25)
    characters.append(chr(ord('a') + tmp))

print(characters)
chstr = ""
for i in characters:
    chstr += i

print(chstr)
lb.pack()
lb2.pack()
root.mainloop()
