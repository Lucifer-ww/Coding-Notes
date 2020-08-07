# Event事件检测——鼠标

按下一个键，点一下鼠标，都是事件，一个游戏中需要很多事件，比如点击一下屏幕，就是一个事件，鼠标的滑动，也是事件，于是我们需要在死循环中侦测事件的发生去处理。

首先先不处理，先说说怎么检测事件，游戏最小系统中的`pygame.QUIT`是一个点击关闭按钮的事件，是在for循环中检测到的，for循环检测原理是让循环变量event在每次检测到的事件列表（即`pygame.event.get()`）中遍历。于是把遍历到的事件（即`event`）都输出，看看结果。

```python
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            exit()
```

这是死循环部分，运行，结果说不清楚，看动图

![](F:\Coding-Thomas\Coding-Notes\Python-Notes\Pygame\前锋教育-Bilibili\动画和事件\动画时间检测.gif)

发现鼠标移动能触发很多事件，pos是坐标，按下鼠标左键或右键，会触发两个事件，按下和抬起，键盘也是按下和抬起，按键会多一个ascll参数。把这个程序保存为一个工具，如果你需要什么事件的名字，拿起这个程序实验就知道了。

鼠标事件

+ MOUSEMOTION：鼠标移动
+ MOUSEBUTTONDOWN：鼠标按下
+ MOUSEBUTTONUP：鼠标抬起
+ 返回鼠标位置：`event.pos`

我们实验鼠标按下出现一个球，松开球跟着也消失，所以需要探测两个事件，一个是鼠标按下，一个是鼠标抬起，代码实现很简单

```python
for event in pygame.event.get():
    # print(event)
    if event.type == pygame.QUIT:
        exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
        pygame.draw.circle(window, (255, 255, 0), (x, y), r)
        pygame.display.update()
    elif event.type == pygame.MOUSEBUTTONUP:
        pygame.draw.circle(window, (255, 255, 255), (x, y), r)
        pygame.display.update()
    # elif event.type == pygame.MOUSEBUTTONDOWN:
    #     print("鼠标按下 ", event.pos)
```

可以实现，于是需要进阶，做一个可以拖拽的小球？按下鼠标并拖拽松开小球消失。这时候需要一个标记变量，在按下的时候标记为True，抬起标记为False，判断`MOUSEMOTION`的时候看看标记，如果是True，就可以拖拽，如果为False就不能，让小球跟着鼠标动起来的原理也很简单，首先用白色覆盖上一次画的球，再将临时坐标等于鼠标事件坐标（即`event.pos`），重新画圆，记住每次更改界面都需要刷新屏幕`pygame.display.update()`。

如何获取鼠标事件坐标，获取鼠标坐标的方法叫做pos，完整使用方法

```python
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            print(event.pos) # 当前在屏幕中的坐标
```



这次贴出完整代码

```python
import pygame

WIN_WIDTH = 400
WIN_HEIGHT = 600
pygame.init()
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("事件检测")
titlelineico = pygame.image.load("img/airplane.ico")  # 导入窗口图标，规格：32x32，格式：.ico
pygame.display.set_icon(titlelineico)  # 设置窗口图标
window.fill((255, 255, 255))
pygame.display.flip()
y = 200
x = 200
r = 50
flag = False
while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            flag = True
            pygame.draw.circle(window, (255, 255, 0), (x, y), r)
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            flag = False
            pygame.draw.circle(window, (255, 255, 255), (x, y), r)
            pygame.display.update()
        if event.type == pygame.MOUSEMOTION and flag:
            pygame.draw.circle(window, (255, 255, 255), (x, y), r)
            print(event, flag)
            x, y = event.pos
            pygame.draw.circle(window, (255, 255, 0), (x, y), r)
            pygame.display.update()
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     print("鼠标按下 ", event.pos)

        # 491 <Event(2-KeyDown {'unicode': '', 'key': 273, 'mod': 0, 'scancode': 72, 'window': None})>
        # 492 <Event(3-KeyUp {'key': 273, 'mod': 0, 'scancode': 72, 'window': None})>
        # 493 <Event(2-KeyDown {'unicode': '', 'key': 274, 'mod': 0, 'scancode': 80, 'window': None})>
        # 494 <Event(3-KeyUp {'key': 274, 'mod': 0, 'scancode': 80, 'window': None})>
```

![](F:\Coding-Thomas\Coding-Notes\Python-Notes\Pygame\前锋教育-Bilibili\动画和事件\拖拽小球实例.gif)

下一节讲键盘的事件