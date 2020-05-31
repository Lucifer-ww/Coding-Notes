- [添加jpg文件](#添加jpg文件)
- [文字与图像共存](#文字与图像共存)

语法如下
```
imageobj = PhotoImage(file="xxx.gif")
```
请留意早期PhotoImage只支持GIF格式，现在已经接受jpg和png了，为了使用方便将GIF图片放在程序所在的文件夹中。

在标签中可以用`image=imageobj`参数设置此图像对象
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200531134429280.png#pic_center)
实例代码

```python
#!usr/bin/env python3
# -*- coding: UTF-8 -*-

from tkinter import *

window = Tk()
window.title("添加gif")

html_gif = PhotoImage(file="小埋.gif")
label = Label(window, image = html_gif)
label.pack()

window.mainloop()
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200531134522848.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Nvb2w5OTc4MQ==,size_16,color_FFFFFF,t_70#pic_center)
# 添加jpg文件
如果要在标签内显示jpg需要借助PIL模块的Image和ImageTk模块，安装pillow模块
```powershell
pip install pillow
```
引入模块
```python
from PIL import Image, ImageTk
```
找一个图片
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200531135308543.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Nvb2w5OTc4MQ==,size_16,color_FFFFFF,t_70#pic_center)
这个图片比较大，但是全屏应该可以显示了，代码如下：
```python
#coding: UTF-8

from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("使用pillow模块插入jpg")
root.state("zoomed") #全屏

image = Image.open("Python.jpg")
pyt = ImageTk.PhotoImage(image)
label = Label(root, image=pyt)
label.pack()

root.mainloop()
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200531135237975.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Nvb2w5OTc4MQ==,size_16,color_FFFFFF,t_70#pic_center)

# 文字与图像共存
使用Label的compound参数让文字与标签共存，compound参数设置图像的位置。

compound参数可以是下列值
+ left：图像在左
+ right：图像在右
+ top：图像在顶部
+ bottom：在下
+ center：文字覆盖在图像上方

实例：
```python
#coding:UTF-8

from tkinter import *

root = Tk()
root.title("compound")
root.state("zoomed")
GText = """GitHub 是一个面向开源及私有软件项目的托管平台，\n
因为只支持 Git 作为唯一的版本库格式进行托管，\n
故名 GitHub。"""

G_gif = PhotoImage(file='Github.jpg')

label = Label(root, text=GText, image = G_gif, bg='lightyellow',
            compound="left", font=("simsun", 20))

label.pack()

root.mainloop()
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200531140252613.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Nvb2w5OTc4MQ==,size_16,color_FFFFFF,t_70#pic_center)