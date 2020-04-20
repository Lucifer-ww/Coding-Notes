[toc]

# Datetime模块

​	Python官方的时间模块主要有`time`和`datetime`模块。time偏重于底层平台，模块中大多数函数会调用本地平台的C链接库，因此有些函数运行的结果，在不同的平台上会有所不同。datetime模块对time模块进行了封装，提供了高级<font color=#12acff>API</font>，因此本章重点介绍datetime模块。

datetime包含以下几个类：

+ datetime：包含时间和日期
+ date：只包含日期
+ time：只包含时间
+ timedelta：计算时间跨度
+ tzinfo：时区信息

## datetime、date和time类

### datetime类

构造方法：

```PyTHON
datetime.datetime(year, month, day, hour = 0, minute = 0, second = 0, microsecond = 0, tzinfo = None)
```

其中的year、month和day三个参数是<font color=OrangeRed><big>不能省略</big></font>的

PythonShell实例：
```python
>>> import datetime
>>> dt = datetime.datetime(2018, 2, 29)
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    dt = datetime.datetime(2018, 2, 29)
ValueError: day is out of range for month
>>> dt = datetime.datetime(2018, 2, 28)
>>> dt
datetime.datetime(2018, 2, 28, 0, 0)
>>> print(dt)
2018-02-28 00:00:00
>>> type(dt)
<class 'datetime.datetime'>
```

`dt = datetime.datetime(2018, 2, 29)`这一行抛出<font color=tomato face="Microsoft YAHEI">ValueError</font>，是因为**不存在**2018年2月29号。
然后`dt = datetime.datetime(2018, 2, 28)`这一天存在，所以dt的类型是<font face="yahei" color=Tomato>datetime.datetime</font>，输出用`print`语句可以输出时间

一些datetime的类方法

+ today()：返回当前本地日期和时间
+ now(tz=None)：返回当前本地日期和时间，如果tz为None或未指定，则等同于today()
+ utcnow()：返回当前<font color=royalblue>UTC</font>[^1]日期和时间
+ fromtimestamp(timestamp, tz=None)：返回UNIX时间戳[^2]对应本地日期和时间
+ utcfromtimestamp(timestamp)：返回UNIX时间戳对应本地日期和时间对应的UTC日期和时间

Shell实例代码

```python
>>> import datetime
>>> datetime.datetime.today()
datetime.datetime(2020, 4, 15, 22, 3, 32, 599159)
>>> datetime.datetime.now()
datetime.datetime(2020, 4, 15, 22, 3, 55, 881638)
>>> datetime .datetime.utcnow()
datetime.datetime(2020, 4, 15, 14, 4, 10, 894521)
>>> datetime.datetime.fromtimestamp(9999999999.999)
datetime.datetime(2286, 11, 21, 1, 46, 39, 999001)
>>> datetime.datetime.utcfromtimestamp(999999999.999)
datetime.datetime(2001, 9, 9, 1, 46, 39, 999000)
```
### Date类

一个date对象可以表示日期等信息，创建date对象可以使用如下构造方法。

```python
datetime.date(year, month, day)
```

其中year、month和day三个参数是不能省略的
Shell实例：

```python
>>> import datetime
>>> d = datetime.date(2018, 2, 29)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    d = datetime.date(2018, 2, 29)
ValueError: day is out of range for month
>>> d = datetime.date(2018, 2, 28)
>>> print(d)
2018-02-28
>>> d
datetime.date(2018, 2, 28)
```

异常是因为没有29号。
注意：print和使用交互直接显示是不同的，直接交互是输出了类型，你可以试试type(d)，会显示datetime.date类型，然后print直接输出了2018-02-28。

类方法

+ date.today()：返回本地日期（当前）
+ date.fromtimestamp(timestamp)：范湖与UNIX时间戳[^2]对应的本地日期

```python
>>> import datetime
>>> datetime.date.today()
datetime.date(2020, 4, 20)
>>> print(datetime.date.today())
2020-04-20
>>> datetime.date.fromtimestamp(999999.999)
datetime.date(1970, 1, 12)
>>> print(datetime.date.fromtimestamp(99999999.999))
1973-03-03
```

### time类

构造方法

```python
datetime.time(hour = 0, minute = 0, second = 0, microsecond = 0, tzinfo - None)
```

实例：

```python
>>> import datetime
>>> datetime.time(24, 59, 58, 1999)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    datetime.time(24, 59, 58, 1999)
ValueError: hour must be in 0..23
>>> datetime.time(23, 59, 58, 1999)
datetime.time(23, 59, 58, 1999)
```

异常因为一天不超过24小时

## 日期时间计算

如果想知道10天之后是那一天，或者想知道2018年1月1日前5周是那一天，就要用到timedelta类，用来计算对象时间间隔
构造方法：

```python
datetime.timedelta(days = 0, seconds = 0, microseconds = 0, milliseconds = 0, minutes = 0, hours = 0, weeks = 0)
```

test：

```python
>>> import datetime
>>> datetime.date.today()
datetime.date(2020, 4, 20)
>>> d = datetime.date.today()
>>> delta = datetime.timedelta(10)
>>> d += delta
>>> print(d)
2020-04-30
>>> d = datetime.date(2018, 1, 1)
>>> delta = datetime.timedelta(weeks = 5)
>>> d -= delta
>>> print(d)
2017-11-27
```

:partly_sunny:是不是发现​写的不怎么样​了​？​确实是​，​我确实有点晕了，哈哈:partly_sunny:

解释：
d是获取日期，然后将d+delta就是增加，d-delta就是相减



后面的搞不明白了……:sweat:

[^1]:UTC——协调世界时，又称世界统一时间、世界标准时间、国际协调时间。由于英文（CUT）和法文（TUC）的缩写不同，作为妥协，简称UTC。协调世界时是以[原子时](https://baike.baidu.com/item/原子时/692466)秒长为基础，在时刻上尽量接近于[世界时](https://baike.baidu.com/item/世界时/692237)的一种时间计量系统。中国大陆采用ISO 8601-1988的《数据元和交换格式信息交换日期和时间表示法》（GB/T 7408-1994）称之为国际协调时间，代替原来的GB/T 7408-1994；中国台湾采用CNS 7648的《资料元及交换格式–资讯交换–日期及时间的表示法》，称之为世界统一时间。
[^2]:时间戳是指格林威治时间1970年01月01日00时00分00秒起至现在的总毫秒数。通俗的讲， 时间戳是一份能够表示一份数据在一个特定时间点已经存在的完整的可验证的数据。 它的提出主要是为用户提供一份电子证据， 以证明用户的某些数据的产生时间。 在实际应用上， 它可以使用在包括电子商务、 金融活动的各个方面， 尤其可以用来支撑公开密钥基础设施的 “不可否认” 服务。