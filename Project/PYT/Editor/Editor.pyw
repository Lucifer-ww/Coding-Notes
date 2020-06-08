from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
 


def new():
    text.delete(1.0, END)
    root.title("Untitled")

def clear():
    text.delete(1.0, END)
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
bf.pack(side=LEFT)
Button(bf, text='New', command=new, bg="lightyellow", width=15, relief=RAISED).pack(anchor=N, side=TOP, padx=5, pady=6)
Button(bf, text='Open', command=load, bg="lightgreen", width=15, relief=RAISED).pack(anchor=N, side=TOP, pady=6, padx=5)
Button(bf, text='Save', command=save, bg="lightblue", width=15, relief=RAISED).pack(anchor=N, side=TOP, padx=5, pady=6)
tips = StringVar()
sstr = """快捷键提示：\n1:Ctrl+s——save\n2:Ctrl+o——open\n3:Ctrl+n——new page\n4:Ctrl+c——clear text"""
tips.set(sstr)
tip = Label(bf, textvariable=tips, relief=RIDGE)
tip.pack()

text = Text(root, undo=True)
text.pack(side=LEFT, fill=BOTH, expand=True)

root.bind("<KeyPress-KP_0>", save)
text.bind("111", load)
text.bind("<Control-n>", new)
text.bind("<Control-c>", clear)
 
root.mainloop()
