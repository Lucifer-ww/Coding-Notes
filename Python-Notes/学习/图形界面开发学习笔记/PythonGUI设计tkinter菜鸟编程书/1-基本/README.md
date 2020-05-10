[toc]
# tkinter的基本概念与语法

链接：<https://blog.csdn.net/cool99781/article/details/106035961>

tkinter是一个Python中的图形开发库（GUI库），GUI英文全称是<font color=deepskyblue>Graphical User Interface</font>

早期的人们和计算机沟通使用文字形式，比如终端控制台，当时的DOS时代人们都用终端，每人使用GUI，因为没有

Python自带tkinter模块，只要引入就行
```python
from tkinter import *
```
先看看tkinter的版本

打开交互，输入
```python
>>> import tkinter
>>> print(tkinter.TkVersion)
8.6
```
8.5以上的版本比较全面，如果低于8.5建议升级Python
## 建立一个窗口
建立一个简单的窗口并不难，只需要两句话
```python
# -*- coding: UTF-8 -*-

import tkinter

root = tkinter.Tk()
root.mainloop()
```
![](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcyMDIwLmNuYmxvZ3MuY29tL2Jsb2cvMTk2NDcwMi8yMDIwMDUvMTk2NDcwMi0yMDIwMDUxMDEzNDYwODE5My0xNTk3NjAwMTIwLnBuZw?x-oss-process=image/format,png)

一个窗口就这样成了，但是这个窗口很乏味对吧，后面会说怎么改。

在GUI程序设计中，有时候也将上述所建立的窗口称为<font color=deepskyblue>容器</font>
## 窗口的基础方法
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200510143734775.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Nvb2w5OTc4MQ==,size_16,color_FFFFFF,t_70)

```python
# -*- coding: UTF-8 -*-
import tkinter

root = tkinter.Tk()
root.title("TEST tk window") #标题方法，更改标题，字符串类型
root.geometry("300x160") #设置窗口大小
root.maxsize(400, 400) #最大窗口大小，设置拖拽的最大值
root.minsize(100, 100) #最小窗口大小，设置拖拽的最小值
root.configure(bg="yellow") #背景颜色方法，更改背景颜色
root.iconbitmap("APPICON.ico")

root.resizable(True, True) #设置可不可以更改窗口大小，第一个参数是宽，第二个是高，True就是可拖拽
root.mainloop()
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200510144153940.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Nvb2w5OTc4MQ==,size_16,color_FFFFFF,t_70)
原先没改变图标的窗口的图标是一个羽毛笔，还记得不turtle的海龟绘图窗口图标就是一个羽毛笔，其实turtle就是用tkinter写的。

背景颜色不一定非要写英文单词，也可以写十六进制颜色，如果记不住可以参考这个网站。

菜鸟工具，16进制和rgb、颜色名的转换，向下滑就是查询表：<https://c.runoob.com/front-end/55>
或者这个，都是菜鸟工具，功能都差不多：<https://c.runoob.com/front-end/870>
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020051015493980.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Nvb2w5OTc4MQ==,size_16,color_FFFFFF,t_70)
