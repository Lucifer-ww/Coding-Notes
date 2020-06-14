#coding:UTF-8
from tkinter import *

root = Tk()
root.title("relief")

Label(root, text="flat", relief="flat").pack(side=LEFT, pady=5, padx=4, ipadx=10, ipady=10)
Label(root, text="groove", relief="groove").pack(side=LEFT, pady=5, padx=4, ipadx=10, ipady=10)
Label(root, text="raised", relief="raised").pack(side=LEFT, pady=5, padx=4, ipadx=10, ipady=10)
Label(root, text="ridge", relief="ridge").pack(side=LEFT, pady=5, padx=4, ipadx=10, ipady=10)
Label(root, text="solid", relief="solid").pack(side=LEFT, pady=5, padx=4, ipadx=10, ipady=10)
Label(root, text="sunken", relief="sunken").pack(
    side=LEFT, pady=5, padx=4, ipadx=10, ipady=10)

root.mainloop()
