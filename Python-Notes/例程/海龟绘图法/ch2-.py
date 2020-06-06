#coding: UTF-8
import turtle
from random import randint as ri
#16777216‬)
def getColor():
    color: int
    color1 = ri(16, 255)
    color2 = ri(16, 255)
    color3 = ri(16, 255)
    color1 = hex(color1)
    color2 = hex(color2)
    color3 = hex(color3)
    ans = "#" + color1[2:] + color2[2:] + color3[2:]
    return ans

def tuxing():
    tmpc = "#558912"
    for i in range(1, 1000):
        #
        if i % 5 == 0:
            tmpc = getColor()
        tmpss = "#558912"
        turtle.color(tmpc)
        turtle.begin_fill()
        tmpnx = ri(-200, 200)
        tmpny = ri(-200, 200)
        turtle.goto(tmpnx, tmpny)
        turtle.end_fill()
    turtle.done()

tuxing()
