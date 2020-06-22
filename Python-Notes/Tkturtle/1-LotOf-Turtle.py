'''
@Author: Wyh
@Date: 2020-06-21 17:00:00
@LastEditTime: 2020-06-21 17:29:30
@LastEditors: Please set LastEditors
@Description: 多个Turtle
@FilePath: \Coding-Notes\Python-Notes\Tkturtle\1-LotOf-Turtle.py
'''

import turtle

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
t5 = turtle.Turtle()

t1.penup()
t2.penup()
t3.penup()
t4.penup()
t5.penup()

t1.color("#FF0000")
t2.color("#00FF00")
t3.color("#FF00FF")
t4.color("#0000FF")
t5.color("#FF9900")

t1.goto(0, 50)
t2.goto(0, 100)
t3.goto(0, 150)
t4.goto(0, 200)
t5.goto(0, 250)

t1.goto(0, 0)
t2.goto(0, 0)
t3.goto(0, 0)
t4.goto(0, 0)
t5.goto(0, 0)

t1.goto(0, -50)
t2.goto(0, -100)
t3.goto(0, -150)
t4.goto(0, -200)
t5.goto(0, -250)

t1.pendown()
t2.pendown()
t3.pendown()
t4.pendown()
t5.pendown()

while True:
    t1.circle(50)
    t2.circle(100)
    t3.circle(150)
    t4.circle(200)
    t5.circle(250)
