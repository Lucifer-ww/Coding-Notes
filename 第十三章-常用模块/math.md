# 常用模块之math模块
Python官方提供了众多模块，这里介绍一些常用模块，不常用的可以去查询Python官方的API文档

[TOC]
Python官方提供math模块进行数学运算，如<font color=#3366FF>指数</font>、<font color=#3366FF>对数</font>、<font color=#3366FF>平方根</font>和<font color=#3366FF>三角函数</font>等运算。math模块中只包括<font color=#FF0033>整数</font>和<font color=#FF0033>浮点数</font>，不包括<font color=#FF0033>复数</font>，复数需要用到<font color=#FF6666>cmath</font>

## 舍入函数

math模块提供的舍入函数有`math.ceil(a)`和`math.floor(a)`，math.ceil(a)用来返回大于或等于a的最小整数，math.floor(a)返回小于或等于a的最大整数

```python
>>> from math import *
>>> ceil(1.4)
2
>>> floor(1.4)
1
>>> round(1.4)
1


>>> ceil(1.5)
2
>>> floor(1.5)
1
>>> round(1.5)
2


>>> ceil(1.6)
2
>>> floor(1.6)
1
>>> round(1.6)
2
```
## 幂和对数函数
math模块提供的<font color=#FF0033>幂</font>和<font color=#FF0033>对数</font>函数如下所示。

+ 对数运算：math.log(a[,base])返回以base为<font color=#FF0033>底</font>a的对数，省略底数base，是a的自然对数
+ 平方根：math.sqrt(a)返回a的平方根
+ 幂运算：math.pow(a, b)返回a的b次幂
在PythonShell
```python
>>> from math import *
>>> log(8, 2)
3.0
>>> pow(8, 2)
64.0
>>> log(8)
2.0794415416798357
>>> sqrt(1.6)
1.2649110640673518
```
## 三角函数
为了简单，于是我省略了`math.`

+ sin(a)：返回弧度a的三角正弦
+ cos(a)：返回弧度a的三角余弦
+ tan(a)：返回弧度a的三角正切
+ asin(a)：返回弧度a的反正弦
+ acos(a)：返回弧度a的反余弦
+ atan(a)：返回弧度a的反正切
+ degrees(a)：将弧度a转换为角度
+ radians(a)：将角度a转换为弧度