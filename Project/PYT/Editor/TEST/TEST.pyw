from tkinter import *


class app:
    def processEvent(event):
        print(event)
    def __init__(self):
        root = Tk()
        label = Label(root, text="test")
    def m(self):
        label.pack()
        root.bind("<Key>", processEvent)
        

pywt = app()
pywt.m()
root.mainloop()
