#1. 创建游戏背景
import turtle as t
import random

mz = t.Screen()
mz.setup(700,700)
mz.bgcolor('black')
mz.title('麦叔迷宫')
mz.register_shape('wall.gif')
mz.register_shape('pr.gif')
mz.register_shape('pl.gif')
mz.register_shape('e.gif')
mz.register_shape('gold.gif')
mz.tracer(0)

levels = []
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXX   XXXXXX  XXXXXXXXXXX",
"XXXP XXXXXXX  XXXXXXXXXXX",
"XXX  XXXXXXX  XXXXXXXXXXX",
"XXX                  XXXX",
"XXXXXXX XXXX  XXXXX  XXXX",
"XXXXXXXGXXXX  XXXXXE  EXX",
"XXXXXXXXXXXX  XXXXX   XXX",
"XXXXXXXXXXXX  XXXXX    XX",
"XX                     XX",
"XXXX  XXXXXX  XXXX  EXXXX",
"XXXX  XXXXXX  XXXXXXXXXXX",
"XXXXE            XXXXXXXX",
"XXXXXXXXXXEXXXX  XXXXXXXX",
"XXXXXXXXXXXXXXX  XXXXXXXX",
"XXXXXXXXXXXXXXX  XXEXXXXX",
"XX               XXXXXXXX",
"XX   XXXXXXXXXXXXXXXXXXXX",
"XX   XXXXX              X",
"XX   XXXXXXXXXXXXX  XXXXX",
"XX     XXXXXXXXXXX  XXXXX",
"XX            XXXX      X",
"XXXX                    X",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]
level_2 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXX   XXXXXX  XXXXXXXXXXX",
"XXX  XXXXXXXP XXXXXXXXXXX",
"XXX  XXXXXXX  XXXXXXXXXXX",
"XXX                  XXXX",
"XXX  XX XXXX  XXXXX  XXXX",
"XXX  XXGXXXX  XXXXXE  EXX",
"XXX  XXXXXXX  XXXXX   XXX",
"XXX  XXXXXXX  XXXXX    XX",
"XX                     XX",
"XXXX  XXXXXX  XXXX   XXXX",
"XXXX  XXXXXX  XXXXXXXXXXX",
"XXXXE            XXX XXXX",
"XXXXXXX  XEXXXX  XXXXXXXX",
"XXXXXXXX  XXXXXX  XXXXXXXX",
"XXXXXXX  XXXXXX  XXEXXXXX",
"XX               XXXXXXXX",
"XX   XX  XXXXXXXXXXXXXXXX",
"XX   XX  X              X",
"XX   XXXXXXXXXXXXX  XXXXX",
"XX     XXXXXXXXXXX  XXXXX",
"XX            XXXX      X",
"XXXX                    X",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]
levels.append(level_1)
levels.append(level_2)

class Enemy(t.Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.shape('e.gif')
        self.speed(0)
        self.penup()
        
    def move(self):
        self.turn()
        if self.fx == 'U':
            go_x = self.xcor()
            go_y = self.ycor() + 24
        elif self.fx == 'D':
            go_x = self.xcor()
            go_y = self.ycor() - 24
        elif self.fx == 'R':
            go_x = self.xcor() + 24
            go_y = self.ycor()
        elif self.fx == 'L':
            go_x = self.xcor() - 24
            go_y = self.ycor()
        self.goto(go_x, go_y)
        t.ontimer(self.move, random.randint(100,300))
    def turn(self):
        #跟随功能
        if self.distance(player) < 48:
            if self.xcor() < player.xcor():
                self.fx = 'R'
            elif self.xcor() > player.xcor():
                self.fx = 'L'
            elif self.ycor() > player.ycor():
                self.fx = 'D'
            elif self.ycor() < player.ycor():
                self.fx = 'U'        
        else:
            self.fx = random.choice(['U', 'D', 'R', 'L'])
        
        
class Gold(t.Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.shape('gold.gif')
        self.speed(0)
        self.penup()
        
class Player(t.Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.shape('pr.gif')
        self.speed(0)
        self.penup()
    def go_right(self):
        go_x = self.xcor()+24
        go_y = self.ycor()
        self.shape('pr.gif')
        self.move(go_x, go_y)
    def go_left(self):
        go_x = self.xcor()-24
        go_y = self.ycor()
        self.shape('pl.gif')
        self.move(go_x, go_y)
    def go_up(self):
        go_x = self.xcor()
        go_y = self.ycor()+24
        self.move(go_x, go_y)        
    def go_down(self):
        go_x = self.xcor()
        go_y = self.ycor()-24
        self.move(go_x, go_y)
    def move(self, go_x, go_y):
        if (go_x, go_y) not in walls:
            self.goto(go_x, go_y)
            self.look_for_gold(go_x, go_y)
        else:
            print('哎呀，hitting wall')
    def look_for_gold(self, go_x, go_y):
        global score
        for g in golds:
            if g.distance(player) == 0:
                score += 1
                print(f"current score is {score}")
                g.ht()
                golds.remove(g)
        if not golds:
            print("金币吃完啦！")
            success()

class Pen(t.Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.shape('wall.gif')
        self.speed(0)
        self.penup()
    def make_maze(self):
        level = levels[current_level-1]
        for i in range(len(level)):
            row = level[i]
            for j in range(len(row)):
                screen_x = -288 + 24 * j
                screen_y = 288 - 24 * i
                char = row[j]
                if char == 'X':
                    self.goto(screen_x, screen_y)
                    self.stamp()
                    walls.append((screen_x, screen_y)) #tuple
                elif char == 'P':
                    player.goto(screen_x, screen_y)
                    player.st()
                elif char == 'G':
                    gold = Gold()
                    golds.append(gold)
                    gold.goto(screen_x, screen_y)
                    gold.st()
                elif char == 'E':
                    ene = Enemy()
                    enemies.append(ene)
                    ene.goto(screen_x, screen_y)
                    ene.st()
#进入下一关 start
current_level = 1
def success():
    if(current_level == len(levels)):
        print('你已称王！太帅啦！')
        show_success_msg('你已称王', '按回车键从新开始')
    else:
        print('成功过关，按回车键进入下一关')
        show_success_msg('成功过关', '按回车键进入下一关')

success_pen = t.Turtle() #用来写成功消息的画笔
def show_success_msg(title, msg):
    success_pen.ht()
    success_pen.speed(0)
    success_pen.penup()
    success_pen.goto(-100, -100)
    success_pen.fillcolor('green') #设置填充色
    success_pen.begin_fill() #开始填充
    for i in range(4):
        success_pen.fd(200)
        success_pen.left(90)
    success_pen.end_fill() #结束填充
    success_pen.goto(-80,30)
    success_pen.color('yellow')
    success_pen.write(title, align='left', font=('Arial', 20, 'bold'))
    success_pen.goto(-80,-30)
    success_pen.write(msg, align='left', font=('Arial', 20, 'bold'))   

#进入下一关
def next_level():
    global current_level
    if(current_level == len(levels)):
        current_level = 1
    else:
        current_level = current_level + 1

    #清楚提示信息
    success_pen.clear()

    #隐藏并清空敌人
    for e in enemies:
        e.ht()
    enemies.clear()

    #清除迷宫的砖墙
    pen.clear()

    #重建迷宫
    pen.make_maze()
    
    #给恶魔加定时器，让他动起来
    for e in enemies:
        t.ontimer(e.move, random.randint(100,300))

#end
    
score = 0
pen = Pen()
player = Player()
walls = []
golds = []
enemies = []
pen.make_maze()

mz.listen()
mz.onkey(player.go_right, 'Right')
mz.onkey(player.go_left, 'Left')
mz.onkey(player.go_up, 'Up')
mz.onkey(player.go_down, 'Down')
mz.onkey(next_level, 'Return') #回车键

for e in enemies:
    t.ontimer(e.move, random.randint(100,300))

while True:
    mz.update()

mz.mainloop()