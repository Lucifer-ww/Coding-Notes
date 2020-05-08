# 捕获异常
程序运行会抛出异常，以下将介绍怎样捕获异常使得程序不中断以及处理异常
## try-except语句
最基础的捕获异常是通过`try-except`组合语句实现的

基本语法格式：
```python
try:
    <可能会抛出异常的语句>
except [猜测异常类型]:
    <处理异常的代码>
```

1）try：
顾名思义——尝试，把你觉得可能报错的语句写在try内，就算有异常也不会暂停程序

2）except：
类似else语句，是为了处理异常的，你需要猜测异常的类型，如：`TypeError`、`ValueError`等，<small><font color=#c586c0>注意异常类型是大小写区别的，TypeError和typeerror不是一回事</font></small>

如果try中发现异常，那么就要走except语句，分析异常并处理；如果没有异常，就不走except，直接跳过，try中的语句正常执行

来来来，注意看一个实验：<br>第一个代码
```python
# -*- coding: UTF-8 -*-
#!/usr/bin/python3

import datetime as dt

def read_date(in_date):
    try:
        date = dt.datetime.strptime(in_date, '%Y-%m-%d')
        return date
    except ValueError:
        print("ValueError!")

str_date = '2018-8-18'
print("日期 = {0}".format(read_date(str_date)))
```
这个程序输出的很正常，因为2018-8-18没有任何问题，所以就正常的执行了try语句，没有走except语句，输出结果如下：
```
日期 = 2018-08-18 00:00:00
```
但是你把`str_date`改成`'201B-8-18'`

这就有问题了，输出如下
```
ValueError!
日期 = None
```
这样try语句抛出异常，无法正确执行，只能走except语句，所以输出了处理异常语句

<font color=orangered>如果你还想要异常对象，就是异常的报错，还可以修改代码</font>

```python
def read_date(in_date):
    try:
        date = dt.datetime.strptime(in_date, '%Y-%m-%d')
        return date
    except ValueError as e:
        print("ValueError!")
        print("异常对象：", e)
```
那么输出：
```
ValueError!
异常对象： time data '201B-8-18' does not match format '%Y-%m-%d'
日期 = None
```
**as关键字**

这个关键字，可以把一个长的名称简化，也可以实现带入功能<br>
比如：
```python
import datetime
datetime.datetime.today()
```
可以调用datetime模块datetime类的today方法，我们可以用`from`简化
```python
from datetime import datetime
datetime.today()
```
这样又减少了，再用`as`简化
```python
from datetime import datetime as dt
dt.today()
```
这样可以把datetime简化成一个比较短的单词dt，意思不变

还可以把异常信息用as带入一个字符串，就像刚才那样。

## 多层except代码块

捕获异常可以有多重异常，那么就像elif一样，可以有多重except语句块。

格式如下：
```python
try:
    <语句>
except [异常类型1]:
    <处理异常>
except [异常类型2]:
    <处理异常>
...
```