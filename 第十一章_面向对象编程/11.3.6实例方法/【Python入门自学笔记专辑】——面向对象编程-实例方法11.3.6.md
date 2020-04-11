[TOC]
#### <font color = #ffac00>实例方法</font>
&emsp;实例方法与实例变量一样都是某个实例（或对象）个体特有的。下面介绍实例方法。
&emsp;**方法**是在**类**中**定义的函数**。而定义实例方法时它的第一个参数也应该是self，这个过程是将当前实例与该方法绑定起来，使该方法成为实例方法。
```python
class Animal(object):
    """定义动物类"""

    def __init__(self, age, sex = 1, weight = 0.0):
        self.age = age
        self.sex = sex
        self.weight = weight

    def eat(self):
        self.weight += 0.05
        print('eat...')

    def run(self):
        self.weight -= 0.01
        print('run...')

a1 = Animal(2, 0, 10.0)
print('a1 体重:{0:0.2f}'.format(a1.weight))
a1.eat()
print('a1 体重:{0:0.2f}'.format(a1.weight))
a1.run()
print('a1 体重:{0:0.2f}'.format(a1.weight))
```
结果如下:
|a1 体重：10.00<br>eat...<br>a1 体重：10.05<br>run...<br>a1 体重：10.04|
|:-|