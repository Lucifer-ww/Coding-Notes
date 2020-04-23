from tkinter import *
from tkinter.scrolledtext import scrolledText

def load():
	with open(filename.get()) as file:
		contents.delete('1.0', END)
		contents.insert(INSERT, file.read())
		
def save():
	with open(filename.get(), 'w') as file:
		file.write(contents.get('1.0', END))

top = Tk()
top.title("Simple Editor")

contents = scrolledText()
contens.pack(side = BOTTOM, expand = True, fill = BOTH)