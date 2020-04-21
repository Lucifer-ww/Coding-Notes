# Python在10行内有什么高端操作？
:link:原文链接<https://blog.csdn.net/ZackSock/article/details/105193651?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522158744456419724835819698%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&request_id=158744456419724835819698&biz_id=0&utm_source=distribute.pc_search_result.none-task-blog-2~blog~first_rank_v2~rank_v25-2>
:cloud:我来把这些代码自己试验一下

<big><font color=orangered>:books:都有什么操作？</font></big>
+ 生成二维码
+ 生成词云
+ 批量抠图
+ 文字情绪识别
+ 识别是否带了口罩
+ 识别图片中的文字
+ 人工智能

## 生成二维码
用到MyQR库，用`pip install MtQR`
代码：
```py
#coding: UTF-8
from MyQR import myqr
myqr.run(
    words='https://blog.csdn.net/cool99781',	# 包含信息
    picture='Python10行内的高端操作/IMG/git.png',			# 背景图片
    colorized=True,			# 是否有颜色，如果为False则为黑白
    save_name='Python10行内的高端操作/view/blogc1.png'  # 输出文件名
)
```
做一个自己博客的二维码

![北极光~]("E:\王一涵programThomas\王一涵PythonThomas\Python-Learned\Python10行内的高端操作\view\blogc1.png")