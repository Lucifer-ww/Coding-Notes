'''
@Author: your name
@Date: 2020-06-22 10:10:25
@LastEditTime: 2020-06-22 17:54:21
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \Coding-Notes\Python-Notes\Tkturtle\3-MathClass_square.py
'''
import turtle
t = turtle.Turtle()
t.speed(0)


def drawsq(r: int):
    for item in range(0, 4):
        t.forward(r)
        t.right(90)
    

for i in range(0, 180):
    drawsq(100)
    t.right(2)


turtle.mainloop()