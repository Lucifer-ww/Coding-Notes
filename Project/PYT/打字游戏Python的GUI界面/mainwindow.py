# coding: UTF-8
#!/usr/bin/python3

from tkinter import *
import random
import time
import os
ft = r"E:\ProgramThomas\Coding-Notes\Project\PYT\打字游戏Python的GUI界面\resource\loggerstr.log"
'''
def msgShow():
    label["text"] = 'I Love Python'
    label["bg"] = 'orangerad'
'''
def getStr(ent):
    #返回Entry的值
    return ent.get()

root = Tk()
root.title("打字游戏GUI")
root.iconbitmap("iconbitmap.ico")
root.geometry("500x400")  # 779*655
lb = Label(root, bitmap="hourglass",
           compound="left",
           cursor="target",
           text="AC打字通",
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

#print(characters)
chstr = ""
for i in characters:
    chstr += i

print(chstr)
fff=open(ft, 'a+')
fff.write('\n'+chstr)
lbtip = Label(root, bitmap="info",
              compound="left",
              text="样例" + chstr,
              fg ="green", bg="#cccccc",
              font=("simsun", 12), underline=True)
# Entry cursor circle

INframe=Frame(root, width=70) #定义输入框架
intxtL = Label(INframe, text="输入> ")

intxt = Entry(INframe, width=50)

lb.grid()
lb2.grid()
lbtip.grid()
INframe.grid()
intxtL.grid(row=3, column=0, sticky=W)  # 输入>Label
intxt.grid(row=3, column=1) #输入框Entry th

instr=getStr(intxt)
print(instr)
fff.write("\n"+instr)
# textTip = Text(root)
# textTip.pack(fill=BOTH, expand=True, padx=3, pady=2)
# textTip.insert(END, chstr)
root.mainloop()
