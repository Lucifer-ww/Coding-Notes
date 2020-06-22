import turtle as t
import datetime as dt
import time

#2. 画出背景
game = t.Screen()
game.bgcolor('black')
game.setup(600,600)
game.title("Python程序员打开新年的方法!")
game.tracer(0)

#3. 画圈
pen = t.Turtle()
pen.ht()
pen.speed(0)
pen.up()
pen.pensize(3)

def draw_clock(h, m, s):
    pen.clear()
    pen.up()
    pen.color('green')
    pen.goto(0, -210)
    pen.seth(0)
    pen.down()
    pen.circle(210)

    #4. 画刻度
    pen.up()
    pen.goto(0,0)
    pen.seth(90)

    for _ in range(12):
        pen.fd(190)
        pen.down()
        pen.fd(20)
        pen.up()
        pen.goto(0,0)
        pen.rt(30)
    
    #5. 画时针
    pen.up()
    pen.goto(0,0)
    pen.down()
    pen.color('white')
    pen.seth(90)
    pen.rt(h/12*360)
    pen.fd(80)
    
    #6. 画分针和秒针
    pen.up()
    pen.goto(0,0)
    pen.down()
    pen.color('yellow')
    pen.seth(90)
    pen.rt(m/60*360)
    pen.fd(120)
    
    pen.up()
    pen.goto(0,0)
    pen.down()
    pen.color('blue')
    pen.seth(90)
    pen.rt(s/60*360)
    pen.fd(160)
    
    pen.up()
    pen.goto(-150, 250)
    pen.color('red')
    font = ('Arial', 20, 'bold')
    hello = "你好B站! 今天是{}年{}月{}日".format(now.year, now.month, now.day)
    pen.write(hello, 'center', font=font)

now = dt.datetime.now()
draw_clock(now.hour,now.minute,now.second)

while True:
    game.update()
    time.sleep(1)
    now = dt.datetime.now()
    draw_clock(now.hour,now.minute,now.second)

game.mainloop()
