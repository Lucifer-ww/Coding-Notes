import turtle as t

#2. 创建背景
game = t.Screen()
game.title("麦叔打乒乓")
game.bgcolor("black")
game.setup(800,600)
game.tracer(0)

#3. 创建球拍
xm = t.Turtle()
xm.ht() #先隐藏
xm.up()
xm.speed(0)
xm.color('yellow')
xm.shape('square')
xm.shapesize(5, 1)
xm.goto(-350, 0)
xm.st() #再显示

#5. 创建如花
ruhua = t.Turtle()
ruhua.ht() #先隐藏
ruhua.up()
ruhua.speed(0)
ruhua.color('white')
ruhua.shape('square')
ruhua.shapesize(5, 1)
ruhua.goto(350, 0)
ruhua.st() #再显示


#6. 创建乒乓球
pp = t.Turtle()
pp.up()
pp.speed(0)
pp.color('white')
pp.shape('circle')
pp.st() #再显示
pp.dx = 2
pp.dy = 2

player_speed = 10
xm_score = 0
ruhua_score = 0

def write_score():
    pen.clear()
    score_text = "小明：{}  如花：{}".format(xm_score, ruhua_score)
    pen.write(score_text, align="center", font=("Arial", 20, 'bold'))

pen = t.Turtle()
pen.ht()
pen.up()
pen.color('white')
pen.goto(-30, 250)
write_score()

    

def xm_up():
    y = xm.ycor()
    y = y + player_speed
    xm.sety(y)

def xm_down():
    y = xm.ycor()
    y = y - player_speed
    xm.sety(y)

def ruhua_up():
    y = ruhua.ycor()
    y = y + player_speed
    ruhua.sety(y)

def ruhua_down():
    y = ruhua.ycor()
    y = y - player_speed
    ruhua.sety(y)

game.listen()
game.onkey(xm_up, 's')
game.onkey(xm_down, 'x')
game.onkey(ruhua_up, 'Up')
game.onkey(ruhua_down, 'Down')

#判定是否要退出
running = True 
def stop_loop():
    global running
    running = False

#获得窗口的Tk对象，并注册关闭事件
root = game.getcanvas().winfo_toplevel()
root.protocol('WM_DELETE_WINDOW', stop_loop)

#主循环
while running:
    game.update()
    pp.setx(pp.xcor() + pp.dx)
    pp.sety(pp.ycor() + pp.dy)
    
    if(pp.ycor() > 290) or (pp.ycor() < -290):
        pp.dy *= -1
    
    #9 接球
    y_up = ruhua.ycor()+50
    y_down = ruhua.ycor()-50
    if(pp.ycor() < y_up and pp.ycor() > y_down and pp.xcor() > 340):
        pp.dx *= -1
        pp.setx(339)

    if(pp.ycor() < xm.ycor() + 50 and pp.ycor() > xm.ycor() - 50 and pp.xcor() < -340):
        pp.dx *= -1
        pp.setx(-339)
    
    #10 球出界
    if (pp.xcor() > 380):
        pp.goto(0,0)
        xm_score += 1
        print("小明得分！")
        write_score()
        
    if (pp.xcor() < -380):
        pp.goto(0,0)
        ruhua_score += 1
        print("如花得分！")
        write_score()

#game.mainloop()
