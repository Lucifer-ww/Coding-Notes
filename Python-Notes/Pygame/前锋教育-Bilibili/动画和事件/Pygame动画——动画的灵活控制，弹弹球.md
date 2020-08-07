# Pygame动画的灵活控制

做动画不可能只让一个小球动起来就完了，所以控制好每一个部件是最重要的，在帧动画内部，最好不要出现太多固定的数字，最好使用变量存储代替，这样更灵活控制，直接修改变量的大小不就可以直接修改很多地方吗？但是固定的数字就无法实现。

这次我们来一个使用小球弹来弹去，scratch中模拟。![](F:\Coding-Thomas\Coding-Notes\Python-Notes\Pygame\前锋教育-Bilibili\动画和事件\img\scratch弹弹球.gif)

下面来说怎么实现Pygame的弹弹球，还是纵向移动，就是以Y轴。

重点：如果制作中出现可能变化的量尽量赋值为变量，不要是固定数字，Y轴可变，存入变量y，这说起来简单，但是做起来难！

让球移动的思路就是让球的Y轴变化，每次擦除上次的圆球，然后Y轴增加再画一次。这是一个球的向下运动，试试看，球运动到末尾就下去了，窗口边界拦不住它。说明Pygame窗口是没有给你设置边界的，需要你自己写判断。绘制圆球的时候有一个值是半径，存到r变量里，那么只需要判断y的值是不是大于`WIN_HEIGHT(窗口高度常量)-r(圆半径)`，就知道是不是到达了底边界，顶部就直接是`y==r`。那么向下运动的时候是`y += 1`，那么向上的时候y怎么办，既然每次增长的量会变，那么就把1变成变量`y_speed`，每次`y += y_speed`，在到达底部的时候将`y_speed = -1`，在到达顶部的时候`y_speed = 1`就行了。于是有了清晰的思路，代码出现！核心部分

```python
while True:
    # 帧动画编辑位置
    # if num % 10000 == 0:
    #     pygame.draw.circle(window, (255, 255, 255), (100, y), 50)
    #     y = y + 1
    #     pygame.draw.circle(window, (255, 0, 0), (100, y), 50)
    #     pygame.display.update()
    # num += 1
    if num % 10 == 0:
        sleep(0.001)
        pygame.draw.circle(window, (255, 255, 255), (100, y), r)
        y = y + y_speed
        if y > 550:
            y_speed = -1
        if y < 50:
            y_speed = 1
        pygame.draw.circle(window, (255, 0, 0), (100, y), r)
        pygame.display.update()
    num += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
```

中间`if`语句是最关键的，sleep函数需要`from time import sleep`

那我们让Pygame的行动更智能一点，可以支持输入一个速度，然后让它移动，将一个正数变量转为负数只需要这样`-var`就够了。还可以加上窗口，使用tkinter制作。

完整代码

```python
import pygame
from   time import sleep
from tkinter import *
from tkinter import messagebox

WIN_WIDTH = 400
WIN_HEIGHT = 600
pygame.init()
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("动画的灵活运用")
titlelineico = pygame.image.load("img/airplane.ico")  # 导入窗口图标，规格：32x32，格式：.ico
pygame.display.set_icon(titlelineico)  # 设置窗口图标
window.fill((255, 255, 255))
pygame.display.flip()

y = 100
r = 50
pygame.draw.circle(window, (255, 0, 0), (100, y), r)
pygame.display.update()


def get_speed(event):
    global y_speed
    if txt.get() == "":
        messagebox.showwarning("Error", "输入为空，按下确定重试")
    else:
        y_speed = int(txt.get())
        root.destroy()


root = Tk()
root.geometry("300x180")
root.title("AskSpeed")
lbf = LabelFrame(root, text='输入Y轴移动速度，回车确定')
lbf.pack()
txt = Entry(lbf, width=30)
txt.bind("<Return>", get_speed)
txt.focus_set()
txt.pack()
root.mainloop()
num= 0
while True:
    # 帧动画编辑位置
    # if num % 10000 == 0:
    #     pygame.draw.circle(window, (255, 255, 255), (100, y), 50)
    #     y = y + 1
    #     pygame.draw.circle(window, (255, 0, 0), (100, y), 50)
    #     pygame.display.update()
    # num += 1
    if num % 1000 == 0:
        sleep(0.001)
        pygame.draw.circle(window, (255, 255, 255), (100, y), r)
        y = y + y_speed
        if y > 550:
            y_speed = -y_speed
        if y < 50:
            y_speed = -y_speed
        pygame.draw.circle(window, (255, 0, 0), (100, y), r)
        pygame.display.update()
    num += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
```

