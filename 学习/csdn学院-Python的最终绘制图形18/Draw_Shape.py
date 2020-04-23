# -*- coding=utf-8 -*-

import turtle
#todo:调整屏幕大小
turtle.screensize(10, 10)
turtle.showturtle()

#todo:调整字体、字号、用途
turtle.write("hello!", font=("华文琥珀", 80, "normal"))
#todo:画圆步长和填充颜色
turtle.begin_fill()
turtle.circle(100, steps =5)
turtle.color("blue")
turtle.end_fill()

turtle.reset()
turtle.pensize(20)

turtle.begin_fill()
turtle.circle(100, steps =5)
turtle.color("blue")
turtle.end_fill()

turtle.reset()
turtle.hideturtle()
turtle.pensize(20)
turtle.begin_fill()
turtle.circle(100, steps =5)
turtle.color("yellow")
turtle.end_fill()



turtle.reset()

turtle.hideturtle()
turtle.begin_fill()
turtle.circle(100, steps =5)
turtle.color("yellow")
turtle.end_fill()
turtle.done()