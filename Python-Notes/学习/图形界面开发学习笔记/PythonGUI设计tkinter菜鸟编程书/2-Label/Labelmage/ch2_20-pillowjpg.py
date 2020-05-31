#coding: UTF-8

from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("使用pillow模块插入jpg")
root.state("zoomed") #全屏

image = Image.open("Python.jpg")
pyt = ImageTk.PhotoImage(image)
label = Label(root, image=pyt)
label.pack()

root.mainloop()