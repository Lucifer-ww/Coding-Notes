'''
@Author: Wyh
@Date: 2020-06-18 14:58:02
@LastEditTime: 2020-06-18 15:05:32
@LastEditors: Please set LastEditors
@Description: Notepad using Tkinter SEL
@FilePath: \Coding-Notes\Python-Notes\图形界面开发学习笔记\PythonGUI设计tkinter菜鸟编程书\Text调整部分-模拟记事本.pyw
'''
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *


def sizeSelected(event):
    f = Font(size=sizeVar.get())
    text.tag_config(SEL, font=f)


root = Tk()
root.title("Notepad using Tkinter Text SEL change")
root.geometry("300x180")

# 建立工具栏
toolbar = Frame(root, relief=RAISED, borderwidth=1)
toolbar.pack(side=TOP, fill=X, padx=2, pady=1)\


# 建立font size Combobox
sizeVar = IntVar()
size = Combobox(toolbar, textvariable=sizeVar)
sizeFamily = [x for x in range(8, 30)]
size["value"] = sizeFamily
size.current(4)
size.bind("<<ComboboxSelected>>", sizeSelected)
size.pack()

# 建立Text
text = Text(root)
text.pack(fill=BOTH, expand=True, padx=3, pady=2)
text.focus_set()

root.mainloop()
