# Pygame动画——移动

游戏最小系统摆上，然后开始做动画:muscle:

这一章的代码写在`01动画原理.py`里面

# 对象移动

由于移动需要刷新，所以要写在循环内，正好在死循环内不停循环刷新就很棒:+1:

动态写在循环里，静态写在循环外，如果静态的对象显示一个球是这样

![image-20200626213926742](E:\ProgramThomas\Coding-Notes\Python-Notes\Pygame\前锋教育-Bilibili\动画和事件\image-20200626213926742.png)

如果想要动态，我们需要将圆的坐标保存为变量，在死循环内更改变量的值就可以，然后重新绘制，就可以有更改，理论上是这样的，那么实际效果呢？

```python
flag = True
while flag:
	# 帧动画编辑位置
	y = y + 1
	pygame.draw.circle(window, (255, 0, 0), (100, y), 50)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
```



没什么，没有更新:slightly_smiling_face:加一句`pygame.display.update()`

![](E:\ProgramThomas\Coding-Notes\Python-Notes\Pygame\前锋教育-Bilibili\动画和事件\逐帧动画-Pygame红圆条y轴移动.gif)

代码最后贴出

发现实现的结果和预想的不太一样呀，因为上一次绘画的圆没有消掉，然后紧接着出现了新圆。最简单的方法是将上一个圆设置为与背景色相同的颜色，这样在快速移动的时候就会认为是一个球在移动。具体思路是在更改y之前重新覆盖。

```python
pygame.draw.circle(window, (255, 255, 255), (100, y), 50)
y = y + 1
pygame.draw.circle(window, (255, 0, 0), (100, y), 50)
```

如果认为移动速度太慢，就让y加的多一些，但一般的电脑都很快，要变慢那么就用一个循环变量，if每10次y+1。

# 缩放

如果要实现一个圆放大缩小的功能，其实也很简单，只是改变圆的半径重新画就行了，可能我们心里老有一种负担就是上一次的还在，只是覆盖了，觉得不妥，其实没关系，单独画圆并不是控件，就当是一个画板，画上去再擦掉，就没了。

<font size=6 face="等线">#END#白嫖代码的机会:small_airplane:</font>

```python
# coding: UTF-8
'''@Author: Thomas'''
import pygame

WIN_WIDTH = 400 # 常量宽
WIN_HEIGHT = 600 # 常量高

pygame.init()

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("动画原理")
window.fill((255, 255, 255)) # 填充为白色
pygame.display.flip() # 刷新动画

# 静态动画编辑位置
# 1、显示静态球
y = 100
pygame.draw.circle(window, (255, 0, 0), (100, y), 50)
pygame.display.update()

flag = True
while flag:
	# 帧动画编辑位置
	pygame.draw.circle(window, (255, 255, 255), (100, y), 50)
	y = y + 1
	pygame.draw.circle(window, (255, 0, 0), (100, y), 50)
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
```

