<font size=5 id=0>:zero:前言</font>
此文章代码都在Github：<a href="https://github.com/Github-Programer/Coding-Notes/tree/master/Python-Notes/%E5%AD%A6%E4%B9%A0/%E5%9B%BE%E5%BD%A2%E7%95%8C%E9%9D%A2%E5%BC%80%E5%8F%91%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0/PythonGUI%E8%AE%BE%E8%AE%A1tkinter%E8%8F%9C%E9%B8%9F%E7%BC%96%E7%A8%8B%E4%B9%A6/3-%E7%AA%97%E5%8F%A3%E6%8E%A7%E4%BB%B6%E9%85%8D%E7%BD%AE%E7%AE%A1%E7%90%86%E5%91%98/pack%E6%96%B9%E6%B3%95">3-窗口控件配置管理员/pack方法</a>别忘了:star:呀
___
做一个应用程序，肯定需要更多的widget控件，所以这时候就牵扯到了如何将这些widget控件配置到 **容器** 或 **窗口** 内。在设计GUI程序时，可以使用三种方法包装和定为各组件在 **容器** 或 **窗口** 内的位置，这三个方法又称==窗口控件配置管理员（Widget Layout Manager）==，通常叫做**布局方法**。

一共有三种布局方法：pack、grid和place，最常用的是pack方法，本章介绍pack方法
# 窗口控件配置管理员
+ <a href=#0>前言</a>
+ <a href=#1>side参数</a>
+ <a href=#2>padx/pady参数</a>
+ <a href=#3>ipadx/ipady参数</a>
+ <a href=#4>anchor参数</a>
+ <a href=#5>fill参数</a>
+ <a href=#6>expand参数</a>
+ <a href=#7>pack参数</a>
___
pack方法的语法格式如下
```
***.pack(options, ...)
```
options参数可以是如下属性：
+ side
+ fill
+ padx/pady
+ ipadx/ipady
+ anchor

下面将详细说明
<font size=5 id=1>:one:side参数</font>
可以==垂直==或==水平==配置控件，可以设置控件的==排列顺序==
```python
#coding:UTF-8
#ch1.py

from tkinter import *

root = Tk()
root.title("普通设置控件")

Label(root, text="Tkinter", bg="lightyellow").pack()
#第一个标签
#这些标签不需要保存在变量中，设置好直接布局
Label(root, text="wxPython", bg="lightgreen").pack()

Label(root, text="PyQt", bg="lightblue").pack()

root.mainloop()
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200531163453756.png#pic_center)
如果窗口中有多个控件，pack会自动让控件**从上往下**排列显示，这是默认设置。也可以使用side参数改变排列方式，此参数取值如下
+ **TOP**：默认值，**由上往下**排列
+ **BOTTOM**：**由下往上**排列
+ **LEFT**：**从左往右**排列
+ **RIGHT**：**从右往左**排列

重新改造，使用side，并让标签的宽度都为15
```python
#coding:UTF-8
#ch2.py --ch1.py 2.0

from tkinter import *

root = Tk()
root.title("普通设置控件")

Label(root, text="Tkinter", bg="lightyellow", width=15).pack(side=BOTTOM)
#第一个标签
#这些标签不需要保存在变量中，设置好直接布局
Label(root, text="wxPython", bg="lightgreen", width=15).pack(side=BOTTOM)

Label(root, text="PyQt", bg="lightblue", width=15).pack(side=BOTTOM)

root.mainloop()

```
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020053116395969.png#pic_center)
再改成LEFT
```python
#coding:UTF-8
#ch3.py -- ch2.py->side->LEFT

from tkinter import *

root = Tk()
root.title("普通设置控件")

Label(root, text="Tkinter", bg="lightyellow", width=15).pack(side=LEFT)
#第一个标签
#这些标签不需要保存在变量中，设置好直接布局
Label(root, text="wxPython", bg="lightgreen", width=15).pack(side=LEFT)

Label(root, text="PyQt", bg="lightblue", width=15).pack(side=LEFT)

root.mainloop()
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200531164144887.png#pic_center)
混合使用side
```python
#coding:UTF-8
#ch4.py -- ch3.py->side->混合使用

from tkinter import *

root = Tk()
root.title("普通设置控件")

Label(root, text="Tkinter", bg="lightyellow", width=15).pack()
#第一个标签
#这些标签不需要保存在变量中，设置好直接布局
Label(root, text="wxPython", bg="lightgreen", width=15).pack(side=RIGHT)

Label(root, text="PyQt", bg="lightblue", width=15).pack(side=LEFT)

root.mainloop()
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200531164348947.png#pic_center)

<font size=5 id=2>:two:padx / pady参数</font>
可以使用padx/pady参数设定控件边界与容器（可以想成窗口边界）的距离或是控件边界间的距离。在默认环境下窗口控件间的距离是 1 像素，如果希望有适度间距，可以设置<font color=royalblue face=simsun>padx</font>/<font color=forestgreen face=simsun>pady</font>，代表<font color=royalblue face=simsun>水平间距</font>/<font color=forestgreen face=simsun>垂直间距</font>
___
实例：

```python
#coding:UTF-8
from tkinter import *

root = Tk()
root.title("relief")

Label(root, text="flat", relief="flat").pack(side=LEFT, pady=5, padx=4, ipadx=10, ipady=10)
Label(root, text="groove", relief="groove").pack(side=LEFT, pady=5, padx=4, ipadx=10, ipady=10)
Label(root, text="raised", relief="raised").pack(side=LEFT, pady=5, padx=4, ipadx=10, ipady=10)
Label(root, text="ridge", relief="ridge").pack(side=LEFT, pady=5, padx=4, ipadx=10, ipady=10)
Label(root, text="solid", relief="solid").pack(side=LEFT, pady=5, padx=4, ipadx=10, ipady=10)
Label(root, text="sunken", relief="sunken").pack(
    side=LEFT, pady=5, padx=4, ipadx=10, ipady=10)

root.mainloop()
```
用relief参数实现各种标签的边框，ipadx和ipady等会讲，运行结果
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200531175600489.png#pic_center)
<font size=5 id=3>:three:ipadx / ipady参数</font>
ipadx/ipady是调整内部距离的，padx/pady是调整外部距离的，还是刚才的程序运行结果，再次分析
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200531175853115.png#pic_center)
<font size=5 id=4>:four:anchor参数</font>
可以设定Widget控件在窗口中的位置，参数如下

![在这里插入图片描述](https://img-blog.csdnimg.cn/2020053118025466.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Nvb2w5OTc4MQ==,size_16,color_FFFFFF,t_70#pic_center)
实例：

```python
#coding: UTF-8
#ch7.py anchor
from tkinter import *
root = Tk()
root.title("ch7.py")
root.geometry("300x180")
okbtn = Button(root, text="OK",
                font="Times 20 bold",
                fg="white", bg="blue")
okbtn.pack(anchor=S, side=RIGHT,
            padx=10, pady=10)
root.mainloop()
```
原本书中写的是Label的，因为这个是鉴于刚学了Label其他的都不知道的同学看的，我觉得既然是OK，Button更好一些吧
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200531180805184.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Nvb2w5OTc4MQ==,size_16,color_FFFFFF,t_70#pic_center)
那么再加上一个NO键是不是更好？

```python
#coding: UTF-8
#ch8.py anchor + NO BTN
from tkinter import *
root = Tk()
root.title("ch7.py")
root.geometry("300x180")
okbtn = Button(root, text="OK",
               font="Times 20 bold",
               fg="white", bg="blue")
okbtn.pack(anchor=S, side=RIGHT,
           padx=10, pady=10)
nobtn = Button(root, text = "NO",
                font="Times 20 bold",
                fg="white", bg="red")
nobtn.pack(anchor=S, side=RIGHT,
            pady=10)
root.mainloop()
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200531181346422.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Nvb2w5OTc4MQ==,size_16,color_FFFFFF,t_70#pic_center)
<font size=5 id=5>:five:fill参数</font>
此参数是告诉pack管理程序，设置控件填满==所分配容器区间==的方式，如果是`fill=X`表示控件可以填满所分配空间X轴不留白，反之亦然，如果是`fill=BOTH`表示控件可以填满所分配空间的X轴和Y轴。fill的默认值是None，表示保持原始大小。

实例：（改编第一个ch1.py）

```python
#coding:UTF-8
#ch9.py fill
from tkinter import *

root = Tk()
root.title("普通设置控件")

Label(root, text="Tkinter", bg="lightyellow").pack(fill=X)
#第一个标签
#这些标签不需要保存在变量中，设置好直接布局
Label(root, text="wxPython", bg="lightgreen").pack()

Label(root, text="PyQt", bg="lightblue").pack(fill=X)

root.mainloop()
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200531182006614.gif#pic_center)
如果所分配容器空间已经满了，则使用fill没有任何作用，将wxPython那个标签设置为`.pack(fill=Y)`不会有任何效果。
<font size=5 id=6>:six:expand参数</font>
expand参数可设定Widget控件是否填满额外的父容器空间，默认是False（或0），表示不填满，如果是True（或是1）则填满。这很重要！
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200531182620480.gif#pic_center)
不管怎么设置fill参数，其结果都没有填满整个窗口，于是expand隆重出场！

```python
#coding:UTF-8
#ch9.py fill
from tkinter import *

root = Tk()
root.title("expand")

Label(root, text="Tkinter", bg="lightyellow").pack(side=LEFT, fill=Y)
#第一个标签
#这些标签不需要保存在变量中，设置好直接布局
Label(root, text="wxPython", bg="lightgreen").pack(fill=X)

Label(root, text="PyQt", bg="lightblue").pack(fill=BOTH, expand=True) #设置可以变化

root.mainloop()
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200531183040667.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Nvb2w5OTc4MQ==,size_16,color_FFFFFF,t_70)

```python
#coding:UTF-8
#ch9.py fill
from tkinter import *

root = Tk()
root.title("expand")

Label(root, text="Tkinter", bg="lightyellow").pack(
    side=LEFT, fill=Y)
#第一个标签
#这些标签不需要保存在变量中，设置好直接布局
Label(root, text="wxPython", bg="lightgreen").pack(fill=BOTH, expand=True)

Label(root, text="PyQt", bg="lightblue").pack(fill=BOTH, expand=True) #设置可以变化

root.mainloop()
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200531183247919.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Nvb2w5OTc4MQ==,size_16,color_FFFFFF,t_70)
<font size=5 id=7>:seven:pack参数</font>
+ forget()——隐藏Widget控件，可以用`pack(option, ...)`复原
+ info()——传回pack选项的对应值
+ size()——传回Widget控件的大小
+ …………更多问度娘:smirk:

<font color=red>PS：一个程序只能有一种窗口布局，如果使用pack，就不能使用grid、place了</font>
<font color=blue>再PS：别忘了点赞留言收藏呀:smile_cat:哦还要关注啊:stars:</font>
<font color=forestgreen>*还PS：此文章代码都在Github：<a href="https://github.com/Github-Programer/Coding-Notes/tree/master/Python-Notes/%E5%AD%A6%E4%B9%A0/%E5%9B%BE%E5%BD%A2%E7%95%8C%E9%9D%A2%E5%BC%80%E5%8F%91%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0/PythonGUI%E8%AE%BE%E8%AE%A1tkinter%E8%8F%9C%E9%B8%9F%E7%BC%96%E7%A8%8B%E4%B9%A6/3-%E7%AA%97%E5%8F%A3%E6%8E%A7%E4%BB%B6%E9%85%8D%E7%BD%AE%E7%AE%A1%E7%90%86%E5%91%98/pack%E6%96%B9%E6%B3%95">Coding-Notes/Python-Notes/学习/图形界面开发学习笔记/PythonGUI设计tkinter菜鸟编程书/3-窗口控件配置管理员/pack方法</a><strong>别忘了star仓库！</strong></font>