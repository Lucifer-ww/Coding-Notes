# random模块

random模块提供了一些生成随机数的函数，一些介绍为了简单省略`random.`

+ random()：返回在范围<font color=#FF33FF>大于等于</font>0.0，且<font color=#FF33FF>小于</font>1.0内的随机浮点数
+ randrange(stop)：返回<font color=#FF33FF>大于等于</font>0，且<font color=#FF33FF>小于</font>
+ randrange(start, stop[, step])：还是randrange函数，返回在范围<font color=#FF33FF>大于等于</font>start，且<font color=#FF33FF>小于</font>stop内，步长为step的随机整数
+ randint(a, b)：返回在范围<font color=#FF33FF>大于等于</font>a，且<font color=#FF33FF>小于等于</font>b的随机整数

```python
# coding=utf-8
#!/usr/bin/python3

import random

# 0.0 <= x < 1.0随机数
print('0.0 <= x < 1.0随机数')
for i in range(0, 10):
    x = random.random()
    print(x)
    pass

# 0 <= x < 5随机数
print('0 <= x < 5随机数')
for i in range(0, 10):
    x = random.randrange(5)
    print(x)
    pass

# 5 <= x < 10随机数
print('5 <= x < 10随机数')
for i in range(0, 10):
    x = random.randrange(5, 10)
    print(x)
    pass

# 5 <= x <= 10随机数
print('5 <= x <= 10随机数')
for i in range(0, 10):
    x = random.randint(5, 10)
    print(x)
```

> 运行结果：
>
> > 0.0 <= x < 1.0随机数
> > 0.34029878291607385
> > 0.2282371197599904
> > 0.6646715464011697
> > 0.028942492371459738
> > 0.8504465561709386
> > 0.5010168923934861
> > 0.7747864321671818
> > 0.1241085608890693
> > 0.31135409609401055
> > 0.2287655076334516
> > 0 <= x < 5随机数
> > 3 3 1 2 1 0 2 2 2 4 
> > 5 <= x < 10随机数
> > 5 7 7 5 8 6 7 6 8 7 