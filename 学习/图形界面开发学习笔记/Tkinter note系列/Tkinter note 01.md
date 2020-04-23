# Tkinter note 01

Python提供了一些图形开发界面的库，几个常用的如下

+ Tkinter：Tkinter 模块(Tk 接口)是 Python 的标准 Tk GUI 工具包的接口 .Tk 和 Tkinter 可以在大多数的 Unix 平台下使用,同样可以应用在 Windows 和 Macintosh 系统里。Tk8.0 的后续版本可以实现本地窗口风格,并良好地运行在绝大多数平台中。
+ Pyqt：是python最复杂也是使用最广泛的图形化
+ Wxpython：wxPython 是一款开源软件，是 Python 语言的一套优秀的 GUI 图形库，允许 Python 程序员很方便的创建完整的、功能健全的 GUI 用户界面。
+ Pywin：是python windows 下的模块，摄像头控制(opencv)，常用于外挂制作
+ Jython：Jython 程序可以和 Java 无缝集成。除了一些标准模块，Jython 使用 Java 的模块。Jython 几乎拥有标准的Python 中不依赖于 C 语言的全部模块。比如，Jython 的用户界面将使用 Swing，AWT或者 SWT。Jython 可以被动态或静态地编译成 Java 字节码。

Tkinter是最简单的Python图形开发库，只有14种组件
Tkinter是Python的标准GUI库。Python使用Tkinter可以最快速度创建GUI应用程序。

**安装问题**

由于Tkinter是内置的Python库，所以安装好Python之后就能使用Tkinter库、而且<font color=royalblue>IDLE也是用<strong>Tkinter编写而成</strong></font>，*对于简单的图形界面用Tkinter就够了*。

**初始引入**

*<strong>注意：</strong>Python3.x版本使用的库名为 tkinter，即首写字母 T 为小写。*

```python
import tkinter
```

创建一个GUI程序

+ 1、导入 Tkinter 模块
+ 2、创建控件
+ 3、指定这个控件的 master，即这个控件属于哪一个
+ 告诉 GM(geometry manager) 有一个控件产生了

**参考**

1、菜鸟教程：<https://www.runoob.com/python/python-gui-tkinter.html>

2、博客园：<https://www.cnblogs.com/morries123/p/8568666.html>