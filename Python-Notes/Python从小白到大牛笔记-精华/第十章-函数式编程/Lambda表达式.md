[TOC]
## <font color=#ffac00>【Python入门自学笔记专辑】——函数嵌套-Lambda表达式</font>
### <font color=#09cc55>函数嵌套</font>
#### <font color=#ff0000>前言</font>
&emsp;Python的函数有很多地方不同于c++，它的函数可以嵌套！`c++程序员：望尘莫及，太可怕了！`不过Python主要是基于c语言开发的，c工程师还是可以自豪的，c语言是要自己做功能，而python自带功能。学哪个各有好处。
#### <font color=#ff0000>正题</font>
&emsp;好了扯远了，继续说Python函数，python的一个函数可以嵌套多个函数，多个函数还可以嵌套。
```python
def func():
    def func1():
        print("func1")
    def func2():
        print("func2")
        def func2_1():
            print("func2.1")
print("hello world")
```
比如上面的这个程序，`func`函数中嵌套了两个函数——`func1`和`func2`，`func2`又嵌套了`func2_1`，Python是支持这种情况的。
比如：
```python
def func():
    def func1():
        print("func1")
    def func2():
        print("func2")
        def func2_1():
            print("func2.1")
    print("func")
func()
```
那么输出结果是：
```
func
```
先来一个**温馨提示**：如果要调用函数，必须把函数放在调用的那行**上面**！
再看代码：
```python
def func():
    choose = int(input("> "))
    def func1():
        print("func1")
    def func2():
        print("func2")
        def func2_1():
            print("func2.1")
    if choose == 1:
        func1()
    elif choose == 2:
        func2()
    print("func")
func()
func()
```
运行结果：
```
> 1
func1
func
> 2
func2
func
```
分析：
&emsp;先调用进`func`函数，然后定义两个函数`func1`、`func2`然后选择，函数必须在选择的上面，不信大伙可以试试。
#### <font color=#ff0000>可能出现的错误</font>
##### 1
```python
def func():
    if choose == 1:
        func1()
    elif choose == 2:
        func2()
    choose = int(input("> "))
    def func1():
        print("func1")
    def func2():
        print("func2")
        def func2_1():
            print("func2.1")
    print("func")
func()
```
###### 报错信息：
```
UnboundLocalError: local variable 'func1' referenced before assignment
```
###### 原因
&emsp;语句在函数上面，无法调用
###### 解决办法
&emsp;把调用语句和函数换位置<br><br>
##### 2
```python
def func():
    choose = int(input("> "))
    def func1():
        print("func1")
    def func2():
        print("func2")
        def func2_1():
            print("func2.1")
    if choose == 1:
        func1()
    elif choose == 2:
        func2()
    print("func")
func1()
```
###### 报错信息
```
NameError: name 'func1' is not defined
```
###### 原因
&emsp;调用函数最多一层，比如在函数外面，不可能跨越两层调用`func1`函数，跨级太多:smile_cat:。
###### 解决办法
&emsp;先调用进`func`函数，再调用`func1`，更高级的办法我也不知道:smile:呵呵o(*￣︶￣*)o
### <font color=#09cc55>Lambda表达式</font>
#### <font color=#ff0000>前言</font>
&emsp;理解了函数类型和函数对象:grinning:，学习Lambda就简单了，就是一种函数吧，准确的说，是个解决一两步的方法，小方法。:satisfied:
#### <font color=#ff0000>正题</font>
&emsp;Lambda是一种匿名函数，匿名函数也是函数，有函数类型，也可以创建函数对象。
&emsp;定义Lambda表达式格式如下：
`lambda 参数列表 : Lambda体`
&emsp;Lambda是关键字声明，这是一个Lambda表达式，“参数列表”与函数的参数列表是一样的，但不需要小括号括起来，冒号后面是“Lambda体”，Lambda表达式的主要代码在此处编写，类似于函数体:smirk:。
___
&emsp;**注意：**Lambda体部分不能是一个代码块，不能包含多余语句，<font color = #ff0000>只能有一条语句</font>，语句会计算一个结果返回给Lambda表达式，但是与函数不同的是，不需要使用`return`语句返回。与其他语言中的Lambda表达式相比，Python中提供的Lambda表达式只能处理一些简单的运算。
___
实例：
```python
#-*- coding = utf-8 -*-

def calculate_fun(opr):
    '''
    #定义相加函数
    def add(a, b):
        return a + b
    
    #定义相减函数
    def sub(a, b):
        return a - b
    '''
    if opr == '+':
        # return add
        return lambda a, b : (a + b)
    else:
        # return sub
        return lambda a, b : (a - b)
    
f1 = calculate_fun('+')
f2 = calculate_fun('-')

print(type(f1))

print("10 + 5 = {0}".format(f1(10, 5)))
print("10 - 5 = {0}".format(f2(10, 5)))
```
运行结果：
```
<class 'function'>
10 + 5 = 15
10 - 5 = 5
```
这个Lambda返回看来是“function”？
&emsp;上面的程序注释部分原本是一个旧程序，大家可以把Lambda部分去掉，把注释部分恢复，可以再试试。:smile:
&emsp;上面代码`return lambda a, b : (a + b)`替代了add()函数，`return lambda a, b : (a - b)`替代了sub()函数，使得函数更快。
## The END
###### 幕后
&emsp;今天我又学习python了:sunglasses:，哈哈，本人努力为大家写了一篇好文，也是给自己这个Python小白写的整理，Lambda这些东东还是有难度的，在VScode上忙碌2小时，弄明白了！:smile:，所以麻烦点一个赞，谢谢！:yum:

![image-20200313164809496](C:\Users\33924\AppData\Roaming\Typora\typora-user-images\image-20200313164809496.png)