# TK：标签Label的基本应用

一起开始学习tkinter吧！<sup><u><a href=#demo><font color=#bbbbbb>NEWS</font></a></u></sup>:rocket:

Label()可以在窗口内建立<font color=#00B0F0>文字</font>或<font color=#00B0F0>图像</font>标签，语法格式如下：

```
Label(父对象, options, ···)
```

Label()的第一个参数是<font color=#00B0F0>父对象</font>，表示这个标签将建立在哪一个父对象（可以想象成父窗口或称容器）内。下列是Label()方法内其他常用的options参数

1. anchor：如果空间大于所需时，控制标签的位置，默认是<font color=#00B0F0>CENTER（居中）</font>，
2. bg或background：背景色
3. bitmap：使用默认图标当做标签内容
4. borderwidth或bd：标签边界宽度，默认1
5. compound：设置标签内含图像和文字时，彼此的位置关系
6. cursor：当鼠标光标在标签上方时的外形
7. fg或foreground：前景色
8. font：字形、字型样式和大小（类似HTML中的&lt;font>标签）
9. height：标签高度，<font color=#00B0F0>单位是字符</font>
10. image：标签以图像方式呈现
11. justify：存在多行文本时最后一行的对齐方式，可取值有<font color=#00B0F0>LEFT/CENTER/RIGHT</font>，默认是居中对齐
12. padx/pady：标签文字与标签区间的间距，单位是<font color=#00B0F0>像素</font>
13. relief：默认`relief=FLAT`，可由此控制标签的外框
14. text：便签内容，`\n`可以换行
15. textvariable：可以设置标签以及变量方式显示
16. underline：可以设置第几个文字有下划线，从0开始算起，默认是-1，表示无下划线‘
17. width：标签宽度，<font color=#00B0F0>单位是字符</font>
18. wraplength：本文到多少宽度后换行，单位是像素

我们在设计程序时，可以将上述参数称为<font color=#00B0F0>属性</font>设置:sunglasses:

## Test

```python
# -*- coding: UTF-8 -*-
#!/usr/bin/python3

from tkinter import *

root = Tk()
root.title("ch2_1")
label = Label(root, text="I LIKE TKINTER")
label.pack()  # 包装与定位组件
print(type(label))  # 传回Label数据类型

root.mainloop()
```

一个窗口就出来了，中间有一句话：I LIKE TKINTER，对吗，不对的话就是Python安装有问题

<img src="E:\ProgramThomas\Coding-Notes\Python-Notes\学习\图形界面开发学习笔记\PythonGUI设计tkinter菜鸟编程书\2-Label\image-20200515202659403.png" alt="image-20200515202659403" style="zoom:50%;" />

然后在Python shell中的输出，label的类型是`<class 'tkinter.Label'>`

## Widget共同属性 Color

<font color=#00B0F0>fg</font>或<font color=#00B0F0>foreground</font>可以设置前景色，相当于标签的颜色；<font color=#00B0F0>bg</font>或<font color=#00B0F0>background</font>可以设置背景色。直接实例说明

```python
# coding: UTF-8
from tkinter import *

root = Tk()
root.title("ch2_3")
label = Label(root, text="I Like Tkinter",
                fg ="blue", bg = "yellow")
label.pack()

root.mainloop()
```

<img src="E:\ProgramThomas\Coding-Notes\Python-Notes\学习\图形界面开发学习笔记\PythonGUI设计tkinter菜鸟编程书\2-Label\image-20200515203704216.png" alt="image-20200515203704216" style="zoom:50%;" />



><p id=demo>News:</p>
>
>我的编程学习笔记仓库已经出炉上线，正在快速维护中……
>地址：<https://github.com/Github-Programer/Coding-Notes>
>欢迎大家光临，大家可以配合着博客一起看
>收录Web、Python、C++知识，整理笔记，一起学习、加油！:rocket:
>欢迎大家贡献：
>
>+ 欢迎提出Issue，我会立刻回答
>+ 欢迎Star，以资鼓励，你们的支持是我维护仓库的最大动力
>+ 现有的知识点难免存在不完善或者错误，所以你可以对已有知识点进行修改/补充。
>+ 笔记内容大多是手敲，所以难免会有笔误，你可以帮我找错别字。
>+ 很多知识点我可能没有涉及到，所以你可以对其他知识点进行补充。
>
>:cloud:仓库正在迅速扩张中……欢迎大家投稿！