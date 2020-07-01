'''
@Author: your name
@Date: 2020-04-23 21:16:19
@LastEditTime: 2020-06-25 21:30:44
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \Coding-Notes\Project\PYT\Editor\Editor.pyw
'''
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
import re

from tkinter.font import Font
# 查找、替换
# 游戏
# 数据可视化


# wxPython  PyQt

def new():
    text.delete(1.0, END)
    root.title("Untitled")

def clear():
    text.delete(1.0, END)
    root.title("Simple Editor")
    
def load():
    filename = askopenfilename()
    if filename == "":
        return None
    
    with open(filename, 'r') as file:
        text.delete('1.0', END)
        text.insert(INSERT, file.read())
    root.title(filename)
 

def save():
    filename = asksaveasfilename(defaultextension=".txt")
    if filename == "":
        return None
    with open(filename, 'w') as file:
        file.write(text.get('1.0', END))
 
 
root = Tk()
root.title("Simple Editor")
root.geometry('800x600')
root.iconbitmap("BITMAP.ico")
 
#contents = ScrolledText()
#contents.pack(side=BOTTOM, expand=True, fill=BOTH)
bf = Frame(root)
bf.pack(side=TOP, fill=X)
Button(bf, text='New', command=new, bg="orange", width=15,
       relief=RAISED).pack(anchor=N, side=LEFT, padx=5, pady=6)
Button(bf, text='Open', command=load, bg="lightgreen", width=15, relief=RAISED).pack(anchor=N, side=LEFT, pady=6, padx=5)
Button(bf, text='Save', command=save, bg="lightblue", width=15, relief=RAISED).pack(anchor=N, side=LEFT, padx=5, pady=6)
Button(bf, text='Clear', command=clear, bg="pink", width=15,
       relief=RAISED).pack(anchor=N, side=LEFT, padx=5, pady=6)


def OpChange(self):
    ftmp = Font(size=var.get(), family=Ffamily.get())
    text.config(font=ftmp)


# 字号设置
Label(bf, text="字号", font=('Hack', 10, "normal")).pack(side=LEFT)
var = IntVar(bf)
options = [x for x in range(10, 40, 4)]
var.set(options[0])
opm = OptionMenu(bf, var, *options, command=OpChange)
opm.pack(side=LEFT)

def Count():
    ans = re.findall(regexin.get(), text.get(1.0, END))
    ret = "有：" + str(len(ans)) + "个"
    answer.config(text=ret)


def Count_fun(self):
    Count()

def cnt():
    global answer
    global regexin
    cntroot = Tk()
    cntroot.geometry("300x180")
    cntroot.title("Regex Count")
    lbf = LabelFrame(cntroot, text="正则表达式统计")
    lbf.pack()
    regexin = Entry(lbf)
    regexin.pack(side=LEFT)
    btn = Button(lbf, text="确定", command=Count)
    btn.pack(side=LEFT)
    regexin.bind("<Return>", Count_fun)
    answer = Label(lbf)
    answer.pack()
    cntroot.mainloop()


menubar = Menu(root)
menu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="Regex", menu=menu)
menu.add_command(label="Count", command=cnt)
root.config(menu=menubar)

def fontFamilyChange(self):
    fmp = Font(family=Ffamily.get(), size=var.get())
    text.config(font=fmp)


# 字体设置
Label(bf, text="字体：", font=('Hack', 10, "normal")).pack(side=LEFT)
Ffamily = Entry(bf, width=20)
Ffamily.insert(0, "Consolas")
Ffamily.pack(side=LEFT)
Ffamily.bind("<Return>", fontFamilyChange)


ffont = Font(family="Consolas", size=var.get(), weight="bold")
# Font(family:str, size:int, weight=("bold" or "normal"):str, underline:bool, ...)

text = Text(root, undo=True, font=ffont)
text.pack(side=TOP, fill=BOTH, expand=True, padx=30, pady=30)

 
root.mainloop()
