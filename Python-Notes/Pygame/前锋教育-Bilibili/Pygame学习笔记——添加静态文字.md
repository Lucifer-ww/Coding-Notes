# Pygame学习笔记——添加静态文字

学习资源：<https://www.bilibili.com/video/BV1bE411p7Ue?p=4>

由于依然还没有学习动画，所以还是静态的，不需要考虑帧的问题。

初始化代码：（不明白的可以看看上一章）

```python
'''
@Author: Thomas
@Date: 2020-06-14 19:56:36
@LastEditTime: 2020-06-14 20:05:54
@Description: Pygame设置文字
@FilePath: \Coding-Notes\Python-Notes\Pygame\前锋教育-Bilibili\显示文字.py
'''

import pygame
pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("显示文字")
# 设置背景颜色
window.fill((255, 255, 255))
pygame.display.update() #就连设置颜色都需要更新一次，what？！

flag = True
while flag:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
```

# 1文字创建

模块用`pygame.font`，这是字体模块

+ 创建字体对象

    + 系统默认字体：`pygame.font.SysFont()`，就一种，中文不支持，很难看

    + 自定义字体：`pygame.font.Font(字体文件路径，字号)`，需要TTF、TTC格式的文件，字号自定义

        Windows下打开资源管理器，找到`C:\Windows\Fonts`目录，这里是系统自带的字体，复制一个走

    + `ft = pygame.font.Font("Font/msyh.ttc", 40)`用一个变量存储，这里是msyh微软雅黑字体

+ 创建文字对象

    + 可以写文字了，render方法
+ `render(文字内容, True, 文字颜色， 背景颜色（可以不设）) `第二个True类似是文字是否平滑之类的，固定就是True了
    + `text = ft.render("游戏你好", True, (123, 123, 123))`用一个变量存储，这里是text
    
+ 渲染到窗口

    + 依旧使用blit
    + `window.blit(text, (0, 0))`

+ 刷新，不刷新不能显示

    + `pygame.display.update()`

源代码：

```python
'''
@Author: Thomas
@Date: 2020-06-14 19:56:36
@LastEditTime: 2020-06-14 20:05:54
@Description: Pygame设置文字
@FilePath: \Coding-Notes\Python-Notes\Pygame\前锋教育-Bilibili\显示文字.py
'''

import pygame
pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("显示文字")
# 设置背景颜色
window.fill((255, 255, 255))
pygame.display.update() #就连设置颜色都需要更新一次

# ===========显示文字==========
#1.创建字体对象
#Pygame自带的模块font
# pygame.font.SysFont() 系统字体，一般无法支持中文
# Font(字体文件路径， 字号) 我就问问为什么不能直接一个字符串，写上字体名！

ft = pygame.font.Font("Font/msyh.ttc", 40)

#2.创建文字对象
# render(文字内容, True, 文字颜色， 背景颜色（可以不设）) #是否平滑一定是True
text = ft.render("游戏你好", True, (123, 123, 123)) #背景颜色不写

#3.渲染到窗口上
window.blit(text, (0, 0))

#4.刷新窗口
pygame.display.update()

flag = True
while flag:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         exit()
```

![image-20200614214129318](C:\Users\33924\AppData\Roaming\Typora\typora-user-images\image-20200614214129318.png#pic_center)

背景颜色可以设置，也是RGB

![image-20200614214239777](C:\Users\33924\AppData\Roaming\Typora\typora-user-images\image-20200614214239777.png)

# 2操作文字

文字我们也需要放在不同位置，于是文字也有形变、移动等方法，和图片几乎没有差别。直接给实例，同样支持`scale`和`rotozoom`

```python
'''
@Author: Thomas
@Date: 2020-06-14 19:56:36
@LastEditTime: 2020-06-14 20:05:54
@Description: Pygame设置文字
@FilePath: \Coding-Notes\Python-Notes\Pygame\前锋教育-Bilibili\显示文字.py
'''

import pygame
pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("显示文字")
# 设置背景颜色
window.fill((255, 255, 255))
pygame.display.update() #就连设置颜色都需要更新一次

# ===========显示文字==========
#1.创建字体对象
#Pygame自带的模块font
# pygame.font.SysFont() 系统字体，一般无法支持中文
# Font(字体文件路径， 字号) 我就问问为什么不能直接一个字符串，写上字体名！

ft = pygame.font.Font("Font/msyh.ttc", 40)

#2.创建文字对象
# render(文字内容, True, 文字颜色， 背景颜色（可以不设）) #是否平滑一定是True
text = ft.render("游戏你好", True, (205, 85, 85), (240, 225, 240)) #背景颜色不写

#3.渲染到窗口上
window.blit(text, (0, 0))

#3.1 获取大小

w, h = text.get_size()
window.blit(text, (600-w, 600-h))
#3.2 缩放和旋转
new1 = pygame.transform.scale(text, (200, 50))
window.blit(new1, (0, 60))

new2 = pygame.transform.rotozoom(text, 0, 2) #不旋转，放大二倍
window.blit(new2, (0, 120))

new3 = pygame.transform.rotozoom(text, 90, 2) #旋转九十度
window.blit(new3, (0, 250))
#4.刷新窗口
pygame.display.update()
flag = True
while flag:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
```

![image-20200614215249270](C:\Users\33924\AppData\Roaming\Typora\typora-user-images\image-20200614215249270.png)