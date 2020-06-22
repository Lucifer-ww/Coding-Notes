'''
@Author: your name
@Date: 2020-06-21 17:30:44
@LastEditTime: 2020-06-21 20:34:35
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \Coding-Notes\Python-Notes\Tkturtle\2-angle.py
'''
import turtle

x = 0; y = 0
flagUp = 0


def choose():
    global em, colors
    em = int(input("每次移动> "))
    colors = input("颜色：#十六进制> ")


choose()
t1 = turtle.Turtle()
t1.color(colors)
turtle.addshape("player.gif")
t1.shape("player.gif")


def go_left():
    global x, y
    t1.goto(x-em, y)
    x -= em


def go_right():
    global x, y
    t1.goto(x+em, y)
    x += em


def go_up():
    global x, y
    t1.goto(x, y+em)
    y += em


def go_down():
    global x, y
    t1.goto(x, y-em)
    y -= em


def go_penup():
    global flagUp
    if flagUp == 0:
        t1.penup()
        flagUp += 1
    else:
        t1.pendown()
        flagUp -= 1


turtle.listen()
turtle.onkey(go_left, "Left")
turtle.onkey(go_right, "Right")
turtle.onkey(go_down, "Down")
turtle.onkey(go_up, "Up")
turtle.onkey(go_penup, "Return")

turtle.mainloop()
