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

我们实验鼠标按下出现一个球，松开球跟着也消失

获取鼠标坐标的方法叫做pos