import turtle as t
import random
import time
import simpleaudio as sa

#记录时间
start_time = time.time()
used_time = 0

#3. 创建背景
game = t.Screen()
game.setup(700, 700)
game.bgpic('bg.gif')
t.tracer(3)

#4. 创建猫咪
cat = t.Turtle()
cat.color('yellow')
cat.shapesize(2,2)
cat.speed(0)
cat.up()

#17. 加上计时
pen = t.Turtle()
pen.ht()
pen.up()
pen.setpos(240, 255)
pen.color('red')
pen.write("计时 " , align="left", font=('Arial', 18, 'bold'))

pen2 = t.Turtle()
pen2.ht()
pen2.up()
pen2.setpos(280, 255)
pen2.color('red')

def update_time():
    global used_time
    now_used_time = int(time.time() - start_time)
    if now_used_time > used_time:
        used_time = now_used_time
        time_str = str(used_time)
        pen2.clear()
        pen2.write(time_str , align="left", font=('Arial', 18, 'bold'))
        
    
#11. 创建小老鼠
rats_number = 1
rats = []
t.register_shape('rat.gif')

for r in range(rats_number):
    rat = t.Turtle()
    rat.ht() #hideturtle
    rat.up()
    rat.speed(0)
    rat.left(random.randint(0, 360))
    rat.shape('rat.gif')
    x = random.randint(-340, 340)
    y = random.randint(-340, 240)
    rat.setpos(x, y)
    rat.st() #showturtle
    rats.append(rat)

def move_left():
    cat.left(30)

def move_right():
    cat.right(30)

def speedup():
    global cat_speed
    cat_speed += 1
    
def slowdown():
    global cat_speed
    cat_speed -= 1

def catch(rat):
    if cat.distance(rat) < 10:
        rat.ht()
        rats.remove(rat)

t.listen()
t.onkey(move_left, 'Left')
t.onkey(move_right, 'Right')
t.onkey(speedup, 'Up')
t.onkey(slowdown, 'Down')


cat_speed = 1
while True:
    update_time()
    cat.fd(cat_speed)
    x = cat.xcor()
    y = cat.ycor()
    if x > 350 or x < -350 or y < -350 or y > 250:
        cat.left(180)
        
    #12. 小老鼠动起来
    for rat in rats:
        rat.fd(1)
        catch(rat)
        x = rat.xcor()
        y = rat.ycor()
        if x > 350 or x < -350 or y < -350 or y > 250:
            rat.left(180)
        
    #判断游戏结束
    if len(rats) == 0:
        pen3 = t.Turtle()
        pen3.ht()
        pen3.up()
        pen3.setpos(-100, 0)
        pen3.color('red')
        over_str = "游戏结束，用时" + str(used_time) + "秒"
        pen3.write(over_str, align="left", font=('Arial', 25, 'bold'))
        break;

game.mainloop()