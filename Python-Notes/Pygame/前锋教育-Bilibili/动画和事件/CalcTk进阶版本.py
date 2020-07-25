from tkinter import *
from tkinter.font import Font


root = Tk()
# root.geometry("400x600")
root.title("CC")

ft = Font(family="Consolas", size=20)
equ = StringVar()
equ.set("fawef")
Label(root, textvariable=equ, width=50, height=5, bg="#DDDDDD", relief=SOLID, font=ft).pack(padx=10, pady=10)

frame = Frame(root)
frame.pack()

Button(frame, text='C', relief=SOLID, width=10).grid(row=0, column=0)
Button(frame, text='DEL', relief=SOLID, width=10).grid(row=0, column=1)
Button(frame, text='/', relief=SOLID, width=10).grid(row=0, column=2)
Button(frame, text='*', relief=SOLID, width=10).grid(row=0, column=3)
Button(frame, text='7', relief=SOLID, width=10).grid(row=1, column=0)
Button(frame, text='8', relief=SOLID, width=10).grid(row=1, column=1)
Button(frame, text='9', relief=SOLID, width=10).grid(row=1, column=2)
Button(frame, text='-', relief=SOLID, width=10).grid(row=1, column=3)
Button(frame, text='4', relief=SOLID, width=10).grid(row=2, column=0)
Button(frame, text='5', relief=SOLID, width=10).grid(row=2, column=1)
Button(frame, text='6', relief=SOLID, width=10).grid(row=2, column=2)
Button(frame, text='+', relief=SOLID, width=10).grid(row=2, column=3)
Button(frame, text='1', relief=SOLID, width=10).grid(row=3, column=0)
Button(frame, text='2', relief=SOLID, width=10).grid(row=3, column=1)
Button(frame, text='3', relief=SOLID, width=10).grid(row=3, column=2)
Button(frame, text='=', relief=SOLID, width=10, height=4).grid(row=3, column=3, rowspan=2)
Button(frame, text='0', relief=SOLID, width=21).grid(row=4, column=0, columnspan=2)
Button(frame, text='.', relief=SOLID, width=10).grid(row=4, column=2)



root.mainloop()