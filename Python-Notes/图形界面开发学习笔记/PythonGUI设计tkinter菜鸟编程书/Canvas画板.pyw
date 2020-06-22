'''
@Author: Wyh
@Date: 2020-06-18 15:08:01
@LastEditTime: 2020-06-19 17:28:42
@LastEditors: Please set LastEditors
@Description: Canvas
@FilePath: \Coding-Notes\Python-Notes\图形界面开发学习笔记\PythonGUI设计tkinter菜鸟编程书\Canvas画板.pyw


@Version:
@1.0.0: 基础构建绘图面板
@1.1.0: 加入颜色
    @1.1.1: 可设置十六进制颜色
    @1.1.2: 可设置RGB
    @1.1.3: 可设置颜色名
@1.2.0: 可设置画笔宽度
@1.3.0: 绘制图形
'''


from tkinter import *
from tkinter.colorchooser import *

dercnt = 0


def showoutput(LS):
    for i in LS:
        print(i)
    print(type(LS))
    print(type(LS[0]))


def usingAsk():
    global choosecolor
    myColor = askcolor()
    choosecolor = myColor[1]
    showLab.config(bg=choosecolor)
    getc.delete(0, END)
    getc.insert(0, myColor[1])


choosecolor = "black"


def sure():
    global choosecolor
    choosecolor = getc.get()
    showLab.config(bg=choosecolor)


def sure_fun(self):
    sure()


tmpcolor: str


def erase():
    global dercnt
    global choosecolor
    global tmpcolor
    if dercnt == 0:
        eraser.config(relief=RAISED)
        tmpcolor = choosecolor
        choosecolor = "#F0F0F0"
        dercnt += 1
    else:
        eraser.config(relief=FLAT)
        choosecolor = tmpcolor
        dercnt -= 1


def paint(event):
    YourChooseSize = sizevar.get()
    x1, y1 = (event.x, event.y)
    x2, y2 = (event.x+YourChooseSize, event.y+YourChooseSize)
    canvas.create_oval(x1, y1, x2, y2, fill=choosecolor, outline=choosecolor)


def cls():
    global choosecolor
    getc.delete(0, END)
    showLab.config(bg="white")
    choosecolor = "black"
    canvas.delete("all")


tk = Tk()
tk.title("Canvas Paint 1.1.3")
lab = Label(tk, text="拖拽鼠标绘图，下面是更改画笔颜色")
lab.pack()

# 询问颜色部分
cco = Frame(tk, relief=SUNKEN)
cco.pack(pady=5)
# 需要一个展示框，一个文本框
tmplb1 = Label(cco, text="展示:")
showLab = Label(cco, width=15, relief=GROOVE, bg="white")
tmplb1.pack(side=LEFT)
showLab.pack(padx=10, side=LEFT)
tmplb2 = Label(cco, text="可输入[#十六进制]和[颜色名] : string")
tmplb2.pack(side=LEFT)
getc = Entry(cco, width=30)
getc.pack(side=LEFT)
cokbtn = Button(cco, text="确认", command=sure)
getc.bind("<Return>", sure_fun)
cokbtn.pack(side=LEFT, ipadx=3, ipady=3)
askbtn = Button(cco, text="使用Ask", command=usingAsk)
askbtn.pack(side=RIGHT, ipadx=3, ipady=3)

# optionMenu
Omf = Frame(tk)
Omf.pack()
tmplb3 = Label(Omf, text="选择画笔宽度")
tmplb3.pack(side=LEFT)
sizevar = IntVar()
SizeList = [x for x in range(20, 90, 6)]
showoutput(SizeList)
sizevar.set(SizeList[0])
ShowOption = OptionMenu(Omf, sizevar, *SizeList)
ShowOption.pack(side=LEFT)
eraser = Button(Omf, text="橡皮", relief=FLAT, command=erase)
eraser.pack(side=LEFT, ipadx=20, padx=50)

canvas = Canvas(tk, width=640, height=300, relief=SUNKEN)
canvas.pack(expand=True, fill=BOTH)

btn = Button(tk, text="清除所有", command=cls)
btn.pack(pady=5)

canvas.bind("<B1-Motion>", paint)

canvas.mainloop()
