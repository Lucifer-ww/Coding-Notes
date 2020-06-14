[toc]

# Pygame学习笔记1——游戏基础及添加图片

学习资料：<https://www.bilibili.com/video/BV1bE411p7Ue?p=1>，快来给这个前锋教育UP主点个赞:rocket:

Pygame有很多的模块，不同的模块专注于不同的功能

Pygame是一个Python的第三方游戏制作模块，可以制作一些比较简单的游戏，但是如果真正开发2D、3D游戏，Pygame就不很实用了，Python可以使用PyQt，但是通常开发大型游戏，比如王者荣耀这种功能超多、高渲染的游戏，用的是Unity之类的2D、3D游戏，都需要使用C系列的语言，比如Unity需要学会C#、Qt要C++。

Pygame在制作小游戏娱乐，哄小孩范畴还是可以的

以下是一些Pygame的类，讲不完的，讲完我也该倒地了

| 模块名           | 功能                                                   |
| ---------------- | :----------------------------------------------------- |
| pygame.cdrom     | 访问光驱（比较古老，现代电脑几乎都没有光驱了）         |
| pygame.cursors   | 加载光标（加载光标，更改光标的形状）                   |
| pygame.display   | 访问显示设备（所有游戏都有界面的）                     |
| pygame.draw      | 绘制形状、​​线和点（以画的形式展现）                     |
| pygame.event     | 管理事件（检测事件，让游戏灵活，鼠标键盘控制游戏）     |
| pygame.font      | 使用字体（游戏的文字字体）                             |
| pygame.image     | 加载和存储图片（游戏中最多的元素）                     |
| pygame.joystick  | 使用游戏手柄:joystick:或者类似的东西（现在很少使用了） |
| pygame.key       | 读取键盘按键（通过键盘控制比如WASD）                   |
| pygame.mixer     | 声音（通常有两种：背景音乐和音效效果）                 |
| pygame.mouse     | 鼠标（鼠标相关功能）                                   |
| pygame.movie     | 播放视频（例如第五人格人物介绍、广告）                 |
| pygame.music     | 播放音频（例如第五人格监管者追击音乐）                 |
| pygame.overlay   | 访问高级视频叠加（视频高级操作）                       |
| pygame.rect      | 管理矩形区域（矩阵-范围相关）                          |
| pygame.sndarray  | 操作声音数据（音频高级操作）                           |
| pygame.sprite    | 操作移动图像（比如人物）                               |
| pygame.surface   | 管理图像和屏幕（看得到的对象）                         |
| pygame.surfarray | 管理点阵图像数据（先不管，高级操作）                   |
| pygame.time      | 管理时间和**帧信息**（管理时间信息，时间控制）         |
| pygame.transform | 缩放和移动图像（游戏界面图像的变形）                   |

# 1、游戏最小系统

Pygame有几步操作

+ 首先导入pygame的库
+ 初始化操作（初始化游戏，初始化硬件）
    + 初始化为一次性初始化，初始很多东西，比如鼠标键盘，也可以一开始不写初始化，等到需要某个部分时分开初始化
+ 创建游戏窗口（创建界面，没有界面怎么玩）
    + 使用`display`方法，设置宽高，设置好的界面需要用一个对象保存，类似于`root = Tk()`，窗口种子
+ 让游戏保持一直运行的状态（类似Tk的消息循环，叫game loop）
    + 如果不加入循环，运行程序会瞬间结束，所以需要一个死循环，结束游戏就跳出
+ 检测事件，比如鼠标、键盘的事件，用for循环遍历

```python
# __author__=="thomas"
import pygame #导入库
# 1.初始化操作
pygame.init()
#2. 创建游戏窗口
window = pygame.display.set_mode((400, 600))
# 3.让游戏保持一直运行的状态
# 写个死循环吧  game loop (游戏循环)
while True:
	# 4.检测事件
	for event in pygame.event.get(): #获取事件
		pass
```

![image-20200614134700311](E:\ProgramThomas\Coding-Notes\Python-Notes\Pygame\前锋教育-Bilibili\image-20200614134700311.png#pic_center)

代码执行结果就是这样

## 1窗口标题

下面介绍一下，我们将窗体赋给了一个变量——`window`，而上方的关闭、最小化、全屏、标题等操作是由操作系统控制的，`window`控制的窗体内部。于是设置标题不用`window`操控，还是`display`类的方法叫做`set_caption()`

```python
# __author__=="thomas"
import pygame #导入库
# 1.初始化操作
pygame.init()
#2. 创建游戏窗口
window = pygame.display.set_mode((400, 600))
# 设置游戏标题，标题
pygame.display.set_caption("Thomas的游戏")
# 3.让游戏保持一直运行的状态
# 写个死循环吧  game loop (游戏循环)
while True:
	# 4.检测事件
	for event in pygame.event.get(): #获取事件
		pass
```



![image-20200614135347005](E:\ProgramThomas\Coding-Notes\Python-Notes\Pygame\前锋教育-Bilibili\image-20200614135347005.png#pic_center)

## 2关闭窗口

这个生成的窗口可以最小化，但是不可以关闭，Mac和Windows都这样，点击无效，原因是没有退出无限循环，可以在控制台内按`Ctrl+C`强制中断，但是一般用户不会这么用。

那么**点击叉子**是一个**事件**

需要在for循环中处理事件，这个事件叫做`pygame.QUIT`，下面提供两个方法

方法一：关闭当前线程——`exit()`，由于当前程序只有这一个线程，所以使用`exit()`退出当前线程

```python
while True:
	# 4.检测事件
	for event in pygame.event.get(): #获取事件
		# 检测关闭按钮被点击的事件
		if event.type == pygame.QUIT:
			exit() #结束这一个线程
```

方法二：将`while True`改为`False`，所以可以把True换成一个变量，比如Flag？

```python
flag = True #循环控制
while flag:
	# 4.检测事件
	for event in pygame.event.get(): #获取事件
		# 检测关闭按钮被点击的事件
		if event.type == pygame.QUIT:
			#exit() #结束这一个线程
			flag = False
```

成功关闭！:muscle:但是真正开发大型游戏绝不可能结束这么简单，结束之前需要很多事情，可能要很多函数为了结束，比如要保存日志数据，你的进度、等级、闯了多少关。

# 2、添加内容

第一步还是游戏最小系统，然后添加内容可以写在两个地方，**第一个是**创建游戏窗口之后和无限循环之前，这个地方写==游戏开始页面静态效果==，**第二个是**在循环中写==帧的刷新（动画，这里不涉及）==，当然也可以写在类、函数中。

## 1添加图片

图片咱们先整静态的，放在静态效果中，首先需要一个图片

![](E:\ProgramThomas\Coding-Notes\Python-Notes\Pygame\前锋教育-Bilibili\Img\Plain.png#pic_center)

这个看起来不错，背景透明，是个战机

素材网站（图标图片）：<https://www.easyicon.net>

插入图片步骤：

+ 加载图片（load，打开图片）
+ 渲染图片（用window，光打开无法显示）
    + 使用window.blit()，`blit(渲染对象，坐标)`
    + 坐标是以屏幕左上角为(0, 0)，有些引擎不一样
+ 刷新显示页面（不刷新无法显示）
    + pygame有一个特点，你放置了部件，但是必须刷新界面可能显示出来，不知道大家写没写过前端，写完HTML必须保存，再刷新浏览器才能显示
    + 刷新可以一次更改很多项只刷新一次
+ 操作图片:control_knobs:
    1. 获取图片大小：`img.get_size()`
    2. 旋转和缩放-----形变：
        1. `pygame.transform.scale(img, (100, 100))`，参数：`scale(缩放对象，目标大小)`，但是如果不按照比例缩小会变形
        2. `pygame.transform.rotozoom(img，)`，参数：`rotozoom(缩放/旋转对象，旋转角度，缩放比例)`，也会发生形变

实例代码：

```python
# __author__=="thomas"
import pygame
pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("显示图片")
# ============游戏开始页面静态效果==========

#1.加载图片
img = pygame.image.load("Img/Plain.png") #如果你要尝试，要么图片放在原位，要么改变路径
#2.渲染图片
#blit(渲染对象，坐标)
window.blit(img, (0, 1))
#3.刷新显示页面
#1.第一次刷新用它 pygame.display.flip()
#2.不是第一次刷新
pygame.display.update() #刷新

#========================================
flag = True
while flag:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
```



![image-20200614143537753](E:\ProgramThomas\Coding-Notes\Python-Notes\Pygame\前锋教育-Bilibili\image-20200614143537753.png#pic_center)

<small>注：如果你想使用这个代码，需要改变图片路径</small>

网上下载的图片难免会尺寸不合适，可以在easyicon下载时点击详情找合适尺寸，也可以下载后使用工具

+ windows画图，点击重新调整尺寸
+ WPS图片，工具超多（VIP更多）



前面介绍的transform也差不多了，然后get_size()有两个返回值，可以使用两个变量接收，实例代码如下，重点在于双等线之间

```python
# __author__=="thomas"
import pygame
pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("显示图片")
# 设置背景颜色
window.fill((255, 255, 255))
# ============游戏开始页面静态效果==========
#1.加载图片
img = pygame.image.load("Img/Plain.png") #如果你要尝试，要么图片放在原位，要么改变路径
#2.渲染图片
#blit(渲染对象，坐标)
window.blit(img, (0, 1))

w, h = img.get_size() #获取宽高
#print(w, h) 输出测试
window.blit(img, (600-w, 600-h)) #放在右下角

new1 = pygame.transform.scale(img, (100, 200)) #缩放为x=100，y=200，变形了
window.blit(new1, (210, 0)) #靠右一点放置

new2 = pygame.transform.rotozoom(img, 0, 0.5) #不旋转为0，缩放百分比为0.5
window.blit(new2, (0, 200))
#==================================
#3.刷新显示页面
#1.第一次刷新用它 pygame.display.flip()
#2.不是第一次刷新
pygame.display.update() #刷新

flag = True
while flag:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
```

![image-20200614151518374](E:\ProgramThomas\Coding-Notes\Python-Notes\Pygame\前锋教育-Bilibili\image-20200614151518374.png#pic_center)

缩放比例为0~1，0.5就是50%

旋转是按照度数向左旋转，45就是

![image-20200614175943022](E:\ProgramThomas\Coding-Notes\Python-Notes\Pygame\前锋教育-Bilibili\image-20200614175943022.png#pic_center)

## 2设置背景颜色

接下来我们需要设置窗口背景，如果是windows操作系统背景是黑色的，Mac是白色的，Mac看起来白白的浑然一体，其实是透明，一旦往上添加东西，就会变成黑色。

```python
# 设置背景颜色
window.fill((255, 255, 255))
```

这应该是最小系统里的，更改后代码如下

```python
# __author__=="thomas"
import pygame
pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("显示图片")
# 设置背景颜色
window.fill((255, 255, 255))
# ============游戏开始页面静态效果==========
#1.加载图片
img = pygame.image.load("Img/Plain.png") #如果你要尝试，要么图片放在原位，要么改变路径
#2.渲染图片
#blit(渲染对象，坐标)
window.blit(img, (0, 1))
#3.刷新显示页面
#1.第一次刷新用它 pygame.display.flip()
#2.不是第一次刷新
pygame.display.update() #刷新
flag = True
while flag:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
```

![image-20200614145513024](E:\ProgramThomas\Coding-Notes\Python-Notes\Pygame\前锋教育-Bilibili\image-20200614145513024.png#pic_center)

pygame的颜色是RGB系统，tkinter是十六进制和颜色名系统



下一节课讲的