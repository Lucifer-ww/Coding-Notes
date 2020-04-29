# Tkinter note 02

上一篇笔记说到创建一个GUI的过程
下面开始实践窗体

**实例**

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-

import tkinter
top = Tkinter.Tk()
# 进入消息循环
top.mainloop()
```

以上程序执行完效果如下：

![img](https://www.runoob.com/wp-content/uploads/2013/12/tkwindow.jpg)

再来看一个实例

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
from tkinter import *           # 导入 Tkinter 库
root = Tk()                     # 创建窗口对象的背景色
                                # 创建两个列表
li     = ['C','python','php','html','SQL','java']
movie  = ['CSS','jQuery','Bootstrap']
listb  = Listbox(root)          #  创建两个列表组件
listb2 = Listbox(root)
for item in li:                 # 第一个小部件插入数据
    listb.insert(0,item)
 
for item in movie:              # 第二个小部件插入数据
    listb2.insert(0,item)
 
listb.pack()                    # 将小部件放置到主窗口中
listb2.pack()
root.mainloop()                 # 进入消息循环
```

执行效果如下：

<img src="https://www.runoob.com/wp-content/uploads/2013/12/tk.jpg" alt="img" style="zoom:50%;" />