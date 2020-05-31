#coding:UTF-8

from tkinter import *

root = Tk()
root.title("compound")
root.state("zoomed")
GText = """GitHub 是一个面向开源及私有软件项目的托管平台，\n
因为只支持 Git 作为唯一的版本库格式进行托管，\n
故名 GitHub。"""

G_gif = PhotoImage(file='Github.jpg')

label = Label(root, text=GText, image = G_gif, bg='lightyellow',
            compound="left", font=("simsun", 20))

label.pack()

root.mainloop()
