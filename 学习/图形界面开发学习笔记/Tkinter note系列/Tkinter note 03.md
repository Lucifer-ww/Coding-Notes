# Tkinter note 03

介绍以下几个控件的用法：

+ Label
+ Frame
+ Entry
+ Text
+ Button
+ Listbox
+ Scrollbar

文章目录：

[TOC]

说明：每个控件最后要加上`pack()`，<font color=red>否则控件是无法显示的</font>

## 1、Label

说明：标签
用法：Label(根对象，【属性列表】)
属性：
text    要显示的文本
bg      背景颜色
bd      外围3D边界的宽度
font    字体(颜色、大小)
width   控件宽度
height  控件高度
实例：(在Python2中运行，在Python3需要把<font color=orangered>Tkinter都改成tkinter</font>)
```python
#-*- coding: UTF-8 -*-
__author__ = '007'
__date__ = '2016/4/7'

from Tkinter import *
root = Tk() # 初始化Tk()
root.title("label-test")    # 设置窗口标题
root.geometry("200x300")    # 设置窗口大小 注意：是x 不是*
root.resizable(width=True, height=False) # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True
l = Label(root, text="label", bg="pink", font=("Arial",12), width=8, height=3)
l.pack(side=LEFT)   # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
root.mainloop() # 进入消息循环
```

![img](https://images2015.cnblogs.com/blog/883532/201604/883532-20160407174823437-73583247.jpg)

## 2、Frame

说明：在屏幕上创建一块矩形区域，多作为容器来布局窗体
用法：frame(根对象，【属性列表】)
实例：
```python
#-*- coding: UTF-8 -*-
__author__ = '007'
__date__ = '2016/4/7'

from Tkinter import *
root = Tk() # 初始化Tk()
root.title("frame-test")    # 设置窗口标题
root.geometry("300x200")    # 设置窗口大小 注意：是x 不是*
root.resizable(width=True, height=False) # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True
Label(root, text="frame", bg="red", font=("Arial",15)).pack()
frm = Frame(root)
#left
frm_L = Frame(frm)
Label(frm_L, text="左上", bg="pink", font=("Arial",12)).pack(side=TOP)
Label(frm_L, text="左下", bg="green", font=("Arial",12)).pack(side=TOP)
frm_L.pack(side=LEFT)
#right
frm_R = Frame(frm)
Label(frm_R, text="右上", bg="yellow", font=("Arial",12)).pack(side=TOP)
Label(frm_R, text="右下", bg="purple", font=("Arial",12)).pack(side=TOP)
frm_R.pack(side=RIGHT)
frm.pack()   # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
root.mainloop() # 进入消息循环
```

运行结果：

![img](https://images2015.cnblogs.com/blog/883532/201604/883532-20160407175126953-2139349475.jpg)

## 3、Entry

说明：创建单行文本框
用法：
创建Entry(根对象，【属性列表】)
绑定变量`var=StringVar()`       `e = Entry(根对象, textvariable = var)`
获取文本框中的值    `var.get()`
设置文本框中的值    `var.set(item1)`

实例：
```python
#-*- coding: UTF-8 -*-
__author__ = '007'
__date__ = '2016/4/7'

from Tkinter import *
root = Tk() # 初始化Tk()
root.title("entry-test")    # 设置窗口标题
root.geometry("300x200")    # 设置窗口大小 注意：是x 不是*
root.resizable(width=True, height=False) # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True
var = Variable()
e = Entry(root, textvariable=var)
var.set("entry") # 设置文本框中的值
e.pack()   # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
root.mainloop() # 进入消息循环
```

![img](https://images2015.cnblogs.com/blog/883532/201604/883532-20160407175332109-1205974070.jpg)

## 4、Text

说明：向该空间内输入文本
用法：
`t = Text(对象)`
插入：`t.insert(mark, 内容)`
删除：`t.delete(mark1, mark2)`
其中，mark可以使行号，或者特殊标识，例如
INSERT：光标插入点CURRENT：鼠标的当前位置所对应的字符位置
END：这个Textbuffer的最后一个字符
SEL_FIRST：选中文本域的第一个字符，如果没有选中区域则会引发异常
SEL_LAST：选中文本域的最后一个字符，如果没有选中区域则会引发异常

实例：
```python
#-*- coding: UTF-8 -*-
__author__ = '007'
__date__ = '2016/4/7'

from Tkinter import *
root = Tk() # 初始化Tk()
root.title("text-test")    # 设置窗口标题
root.geometry("300x200")    # 设置窗口大小 注意：是x 不是*
root.resizable(width=True, height=False) # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True
t = Text(root)
t.insert('1.0',"text1\n")   # 插入
t.insert(END,"text2\n") # END:这个Textbuffer的最后一个字符
t.insert('1.0',"text3\n")
#t.delete('1.0','2.0')   # 删除
t.pack()   # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
root.mainloop() # 进入消息循环
```

![img](https://images2015.cnblogs.com/blog/883532/201604/883532-20160407175620328-379620339.jpg)

## 5、Button

说明：按钮
用法：Button(根对象，【属性列表】)

实例：
```python
#-*- coding: UTF-8 -*-
__author__ = '007'
__date__ = '2016/4/7'

from Tkinter import *
root = Tk() # 初始化Tk()
root.title("button-test")    # 设置窗口标题
root.geometry()    # 设置窗口大小 注意：是x 不是*

def printhello():
    t.insert(END,"hello\n")
t = Text()
t.pack()   # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
Button(root, text="press", command=printhello).pack()
root.mainloop() # 进入消息循环
```

![img](https://images2015.cnblogs.com/blog/883532/201604/883532-20160407175827734-385650554.jpg)

## 6.Listbox
说明：列表控件，可以含有一个或者多个文本框，可单选也可多选
用法：
创建  lb = ListBox(根对象，【属性列表】)
绑定变量 var = StringVar() lb=ListBox(根对象,listvariable=var)
得到列表中的所有值 var.get()
设置列表中的所有值 var.set((item1,item2,......))
添加：lb.insert(item)
删除：lb.delete(item,...)
绑定事件 lb.bind('&lt;ButtonRelease-1>',函数)
获得所选中的选项 lb.get(lb.curselection())
属性：selectmode可以为BROWSE MULTIPL SINGLE
实例：
```python
#-*- coding: UTF-8 -*-
__author__ = '007'
__date__ = '2016/4/7'

from Tkinter import *
root = Tk()
root.title("listbox-test")
root.geometry()
def print_item(event):
    print lb.get(lb.curselection())
var = StringVar()
lb = Listbox(root, listvariable = var)
list_item = [1,2,3,4]
for item in list_item:
    lb.insert(END,item)
lb.delete(2,4)
var.set(('a','b','c','d'))
print var.get()
lb.bind('<ButtonRelease-1>',print_item)
lb.pack()
root.mainloop()
```

![img](https://images2015.cnblogs.com/blog/883532/201604/883532-20160407180155859-1363353202.jpg)

## 7.Scrollbar
说明：垂直滚动控件
用法：ListBox(根对象，【属性列表】
实例：
```python
#-*- coding: UTF-8 -*-
__author__ = '007'
__date__ = '2016/4/7'

from Tkinter import *
root = Tk() # 初始化Tk()
root.title("scrl-test")    # 设置窗口标题
root.geometry()    # 设置窗口大小 注意：是x 不是*
def print_item(event):
    print lb.get(lb.curselection())
var = StringVar()
lb = Listbox(root, height=5, selectmode=BROWSE, listvariable = var)
lb.bind('<ButtonRelease-1>',print_item)
list_item = [1,2,3,4,5,6,7,8,9,0]
for item in list_item:
    lb.insert(END,item)
scrl = Scrollbar(root)
scrl.pack(side=RIGHT,fill=Y)
lb.configure(yscrollcommand=scrl.set)   # 指定Listbox的yscrollbar的回调函数为Scrollbar的set，表示滚动条在窗口变化时实时更新
lb.pack(side=LEFT,fill=BOTH)
scrl['command'] = lb.yview  # 指定Scrollbar的command的回调函数是Listbar的yview
root.mainloop()
```

![img](https://images2015.cnblogs.com/blog/883532/201604/883532-20160407180354250-304091969.jpg)