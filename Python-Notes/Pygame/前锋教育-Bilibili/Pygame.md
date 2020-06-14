# Pygame

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

