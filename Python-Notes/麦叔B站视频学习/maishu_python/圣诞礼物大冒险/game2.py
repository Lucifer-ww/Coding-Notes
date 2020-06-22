import turtle as t #module
import random as r #随机数
import simpleaudio as sa

t.register_shape('boy.gif')
t.register_shape('gift1.gif')
t.register_shape('gift2.gif')
t.register_shape('gift3.gif')
t.register_shape('zd.gif')

yeah = sa.WaveObject.from_wave_file('yeah.wav')
dead = sa.WaveObject.from_wave_file('dead.wav')

game = t.Screen()
game.setup(900, 700)
game.bgpic('bg.gif')
game.title('圣诞礼物大冒险')
game.tracer(0) #停止默认刷新

boy = t.Turtle()
boy.ht()
boy.speed(0)
boy.up()
boy.shape('boy.gif')
boy.goto(0, -250)
boy.st()
fx = "L" #方向:R向右，L向左，其他就是不动 全局变量
boy_speed = 3
score = 0
life = 3

pen = t.Turtle()
pen.ht()
pen.speed(0)
pen.up()
pen.goto(-400, 300)
pen.color('yellow')
score_text = "分数:{} 命数:{}".format(score, life)
font = ('Arial', 20, 'bold')
pen.write(score_text, align='left', font=font)


#创建礼物：传入图形和数量
def build_gifts(shape, number):
    gift_list = []
    for num in range(number):
        g = t.Turtle()
        g.ht()
        g.speed(0)
        g.up()
        g.shape(shape)
        x = r.randint(-400, 400)
        y = r.randint(0, 300)
        g.goto(x, y)
        g.st()
        g.fall_speed = r.randint(1,5)
        gift_list.append(g)
    return gift_list

gift1_list = build_gifts('gift1.gif', 6)
gift2_list = build_gifts('gift2.gif', 5)
gift3_list = build_gifts('gift3.gif', 4)
dan_list = build_gifts('zd.gif', 5)


def to_left():
    global fx
    global boy_speed 
    if fx == "L":
        boy_speed += 1 #boy_speed = boy_speed + 1
    else:
        fx = "L"
        boy_speed = 3

def to_right():
    global fx
    global boy_speed
    if fx == "R":
        boy_speed += 1 #boy_speed = boy_speed + 1
    else:
        fx = "R"
        boy_speed = 3
 
def fall_gifts(gifts, add_score):
    global score
    #礼物动起来
    for g in gifts:
        g.sety(g.ycor()- g.fall_speed)
        if g.ycor() < -350:
            g.sety(300)
        if g.distance(boy) < 40:
            yeah.play()
            score = score + add_score
            g.sety(300)
            pen.clear()
            pen.write("分数:{} 命数:{}".format(score, life), align='left', font=font)
        

t.listen()
t.onkey(to_left, "Left")
t.onkey(to_right, "Right")

game_over = False
while True:
    #判断游戏是否结束
    if game_over:
        break
    
    game.update() #自主刷新界面
    if fx == "R":
        x = boy.xcor()
        x = x + boy_speed
        boy.setx(x)
    elif fx == "L":
        boy.setx(boy.xcor()-boy_speed)
    
    fall_gifts(gift1_list, 3)
    fall_gifts(gift2_list, 5)
    fall_gifts(gift3_list, 10)
    
    for d in dan_list:
        d.sety(d.ycor()- d.fall_speed)
        if d.ycor() < -350:
            d.sety(300)
        if d.distance(boy) < 40:
            dead.play()
            life = life - 1
            d.sety(300)
            pen.clear()
            pen.write("分数:{} 命数:{}".format(score, life), align='left', font=font)
            if life == 0:
                game_over = True
                pen2 = t.Turtle()
                pen2.ht()
                pen2.speed(0)
                pen2.up()
                pen2.goto(-100, 0)
                pen2.color('red')
                font = ('Arial', 30, 'bold')
                pen2.write("游戏结束！", align='left', font=font)
                                
        
game.mainloop();