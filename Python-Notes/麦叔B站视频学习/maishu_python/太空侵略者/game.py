import turtle
import random
import simpleaudio as sa

#15 引入音乐
laser = sa.WaveObject.from_wave_file('laser.wav')
explosion = sa.WaveObject.from_wave_file('explosion.wav')

#3 设置背景
game = turtle.Screen()
game.setup(700, 700)
game.title("麦叔-太空侵略者")
game.bgpic('bg.gif')

#4 创建玩家
turtle.addshape('player.gif');
player = turtle.Turtle()
player.ht()
player.speed(0)
player.up()
player.shape('player.gif');
player.setpos(0, -300)
player.st()

#5. 玩家动起来
player_step = 15
def go_left():
    x = player.xcor()
    x = x - player_step
    if x < -300:
        x = -300
    player.setx(x)
    
def go_right():
    x = player.xcor()
    x = x + player_step
    if x > 300:
        x = 300
    player.setx(x)

turtle.listen()
turtle.onkey(go_left, 'Left')
turtle.onkey(go_right, 'Right')

#8. 添加子弹
bomb = turtle.Turtle()
bomb.ht()
bomb.speed(0)
bomb.up()
bomb.shape('triangle')
bomb.color('yellow')
bomb.shapesize(0.5, 0.5)
bomb.seth(90)

#12. 添加分数
score = 0
pen = turtle.Turtle()
pen.color("white")
pen.speed(0)
pen.up()
pen.ht()
pen.setpos(-340, 230)
score_string = "分数：%s" %score
pen.write(score_string, align="left", font=('Arial', 12, 'normal'))

#9. 发射子弹
is_fired = False
def fire():
    global is_fired
    if is_fired == False:
        bomb.setpos(player.xcor(), player.ycor() + 20)
        bomb.st()
        is_fired = True
        laser.play()
    
turtle.onkey(fire, 'space')

#6. 添加敌人
num = 6
inv_list = []
turtle.addshape('inv.gif');
for i in range(6):
    inv = turtle.Turtle()
    inv_list.append(inv)
    inv.ht()
    inv.speed(0)
    inv.up()
    inv.shape('inv.gif')
    x = random.randint(-200, 200)
    y = random.randint(100, 200)
    inv.setpos(x,y)
    inv.st()
    
#7. 敌人动起来
inv_step = 2
go_back = False
bomb_step = 20
game_over = False
while True:
    if game_over:
        pen2 = turtle.Turtle()
        pen2.color('red')
        pen2.ht()
        pen2.write('游戏结束', align='center', font=('Arial', 18, 'bold'))
        explosion.play()
        break
    
    for inv in inv_list:
        x = inv.xcor()
        x += inv_step
        inv.setx(x)
        if x > 300 or x < -300:
            go_back = True
        if inv.distance(bomb) < 15:
            inv.setpos(0, 240)
            is_fired = False
            bomb.setpos(-350, -350)
            bomb.ht()
            score += 10
            score_string = "分数：%s" %score
            pen.clear()
            pen.write(score_string, align="left", font=('Arial', 12, 'normal'))
            explosion.play()
        if inv.ycor() < -280:
            game_over = True
            
        
    if go_back:
        inv_step *= -1
        go_back = False
        for inv in inv_list:
            y = inv.ycor()
            y -= 100
            inv.sety(y)
    
    if is_fired:
        y = bomb.ycor()
        y += bomb_step
        bomb.sety(y)
        if y > 250:
            is_fired = False
            bomb.setpos(-350, -350)
            bomb.ht()
    
    
    
       
       
    
