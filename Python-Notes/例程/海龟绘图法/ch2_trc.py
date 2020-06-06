# coding: utf-8

from random import randint as ri
import turtle

def getColor():
    #662233
    #rgb(66, 22, 33)
    color1 = ri(16, 255)
    color2 = ri(16, 255)
    color3 = ri(16, 255)
    color1 = hex(color1) #系统自带函数-hex，将整数转换为十六进制
    color2 = hex(color2)
    color3 = hex(color3)
    ans = "#" + color1[2:] + color2[2:] + color3[2:]
    return ans


tmpc = "#558912"
for i in range(1, 1000):
    #
    if i % 5 == 0:
        tmpc = getColor()
    tmpss = "#558912"
    turtle.color(tmpc)
    tmpnx = ri(-200, 200)
    tmpny = ri(-200, 200)
    turtle.goto(tmpnx, tmpny)
turtle.done()