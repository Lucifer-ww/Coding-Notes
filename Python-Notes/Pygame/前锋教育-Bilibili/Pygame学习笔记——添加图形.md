# Pygame显示图形

pygame专门提供了一个画图的模块，叫做`draw`，其中又有很多模块

# 1、画直线

+ 模块为：`pygame.draw.line()`
    + line方法参数为`line(画在哪儿，线的颜色，线的起点，线的终点，线宽)`
    + 线宽默认为1
    + 画在哪儿一般都是在window上

```python
import pygame
pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("显示图形")
# 设置背景颜色
window.fill((255, 255, 255))
pygame.display.update() #就连设置颜色都需要更新一次

# ============显示图形============
#1画直线
#line()
pygame.draw.line(window, (234, 190, 233), (20, 20), (90, 90), 2)
window.blit(window, (0, 0))
pygame.display.update()


flag = True
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
```

![image-20200615203856534](E:\ProgramThomas\Coding-Notes\Python-Notes\Pygame\前锋教育-Bilibili\image-20200615203856534.png)

# 2、画折线

大家说了，折线好画，就是多个直线连接在一起就是折线，可以但是麻烦，line方法的升级lines集合这个方案，就是依然是拼接原理。

![image-20200615213243775](E:\ProgramThomas\Coding-Notes\Python-Notes\Pygame\前锋教育-Bilibili\image-20200615213243775.png)

+ 模块为：`pygame.draw.lines()`
    + 参数为`lines(画在哪，线的颜色，是否闭合，多个点的列表，线宽)`
    + 前两个参数和上面一模一样
    + 是否闭合：假如有四个点，`点1->点2->点3->点4->点1`，就是最后一个点连接第一个点
    + 多个点的列表，就是把**每一条线**的**起始位置**和**结束位置**放在一个**元组**中，将多个元组放在**列表**中
        + 实例：`points = [(10, 300), (100, 160), (180, 260), (300, 100)]`
        + 将每一条线的数据存储
    + 线宽不用说吧



实例：

```python
import pygame
pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("显示图形")
# 设置背景颜色
window.fill((255, 255, 255))
pygame.display.update() #就连设置颜色都需要更新一次

# ============显示图形============
#1画直线
#line()
pygame.draw.line(window, (234, 190, 233), (20, 20), (90, 90), 2) #一看这就是斜线
window.blit(window, (0, 0))
pygame.display.update()

#2画折线
#lines()
points = [(10, 300), (100, 160), (180, 260), (300, 100)]
pygame.draw.lines(window, (0, 255, 0), True, points, 3)
window.blit(window, (0, 0))
pygame.display.update()
# ==============================
flag = True
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
```



![image-20200616184305051](E:\ProgramThomas\Coding-Notes\Python-Notes\Pygame\前锋教育-Bilibili\image-20200616184305051.png)

# 3、画圆

+ 函数：`pygame.draw.circle()`
    + 参数详解：`circle(画在哪儿，线的颜色，圆心，半径，线宽=0)`
    + 圆心为一个坐标点
    + 颜色为RGB
    + 线宽默认为零，为填充

# 4、矩形

+ 函数：`pygame.draw.rect()`
    + 参数详解：`rect(画在哪，线的颜色，矩形范围，线宽=0)`
    + 颜色为RGB
    + 只需要定下左上角的顶点和长和宽，就是矩形范围
    + 如果不需要线宽的话，也就是线宽为0，就是填充了

画圆和矩形的综合代码

```python
# ============显示图形============
#1画直线
#line()
pygame.draw.line(window, (234, 190, 233), (20, 20), (90, 90), 2) #一看这就是斜线
window.blit(window, (0, 0))
pygame.display.update()

#2画折线
#lines()
points = [(10, 300), (100, 160), (180, 260), (300, 100)]
pygame.draw.lines(window, (0, 255, 0), True, points, 3)
window.blit(window, (0, 0))
pygame.display.update()

#3画圆
#circle()
pygame.draw.circle(window, (0, 0, 255), (200, 250), 100, 2)

#4矩形
pygame.draw.rect(window, (120, 20, 60), (100, 70, 200, 100), 1)
pygame.display.update()
# ==============================
```

![image-20200616210001524](E:\ProgramThomas\Coding-Notes\Python-Notes\Pygame\前锋教育-Bilibili\image-20200616210001524.png)



如果长方形的线宽为0，就是填充

![image-20200616210047535](E:\ProgramThomas\Coding-Notes\Python-Notes\Pygame\前锋教育-Bilibili\image-20200616210047535.png)

我们改变这些图形的位置，就改变xy坐标就行了



# 5、椭圆

+ 函数：`pygame.draw.ellipse()`
    + 画一个长方形的**内切圆**，正方形是圆
    + 参数详解：`ellipse(画在哪儿, 线的颜色, 矩形范围, 线宽=0)`
    + 实例：`ellipse(window, (255, 0, 0), (30, 70, 100, 200), 3)`

![image-20200616211404891](E:\ProgramThomas\Coding-Notes\Python-Notes\Pygame\前锋教育-Bilibili\image-20200616211404891.png)

# 6、弧线

其实弧线和椭圆又有关系，其实都是按照**矩形**的一些参数绘制的

弧线也使用长方形内的内切圆，只是去其中一部分

+ 函数：`pygame.draw.arc()`
    + 参数详解：`arc(画在哪儿，线的颜色，矩形范围，起始弧度，终止弧度，线宽=1)`
    + 注意这里是弧度（0~2π），而不是角度！
    + 椭圆的这里是0
        + ![image-20200616212235236](E:\ProgramThomas\Coding-Notes\Python-Notes\Pygame\前锋教育-Bilibili\image-20200616212235236.png)
    + 如果取一半就是0~π，π怎么表示？就写成3.1415926就够了，如果有人想究极精准，那就多写几位，直接用PI需要模块
    + 线宽默认1
    + 颜色都是RGB

```python
# ============显示图形============
#1画直线
#line()
pygame.draw.line(window, (234, 190, 233), (20, 20), (90, 90), 2) #一看这就是斜线
window.blit(window, (0, 0))
pygame.display.update()

#2画折线
#lines()
points = [(10, 300), (100, 160), (180, 260), (300, 100)]
pygame.draw.lines(window, (0, 255, 0), True, points, 3)
window.blit(window, (0, 0))
pygame.display.update()

#3画圆
#circle()
pygame.draw.circle(window, (0, 0, 255), (200, 250), 100, 2)

#4矩形
pygame.draw.rect(window, (120, 20, 60), (100, 70, 200, 100), 0)
pygame.display.update()

#5椭圆
pygame.draw.ellipse(window, (255, 0, 0), (30, 70, 100, 200), 3)
pygame.display.update()

#6弧线
pygame.draw.arc(window, (0, 0, 0), (30, 70, 100, 200), 0, 3.1415926, 7)
pygame.display.update()

# ==============================
```



![image-20200616212550811](E:\ProgramThomas\Coding-Notes\Python-Notes\Pygame\前锋教育-Bilibili\image-20200616212550811.png)

对于椭圆取弧度是逆时针的

然后π可以使用math模块导入

```python
from math import pi
print(pi)
```

直接pi就出来了，就比刚才多了一些，也是一个固定的常量