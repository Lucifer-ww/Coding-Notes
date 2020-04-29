#### <font color =#ffac00 face = 幼圆>用Python解决简单计算器</font>

&emsp;因为本人也是初学Python，所以今天我闲来无事打算重新做c++曾经做过的简单计算器，就是输入两个数，然后输入一个字符，代表运算符，然后输出结果。C用switch可以解决，这个另见我的博客<https://blog.csdn.net/cool99781/article/details/104071986> ，里面是c++的解题程序，现在来说Python，而且Python可以加上另一个功能，可以加^幂次方的运算，因为Python中**就是x的y次幂。

下面是代码：

```python
# -*- coding = utf-8 -*-
#usr/bin/python3

#做一个简单计算器程序

def check(num1, OP, num2):
    if OP == '+':
        return num1 + num2
    elif OP == '-':
        return num1 - num2
    elif OP == '*':
        return num1 * num2
    elif OP == '/':
        return num1 / num2
    elif OP == '^':
        return num1 ** num2

flag = True
while flag:
    num1 = int(input("输入第一个数>"))
    OP = input("输入运算方法:有+、-、*、/、^   >")
    num2 = int(input("输入第二个数>"))

    answer = check(num1, OP, num2)

    print("答案是:{0}".format(answer))
    print("还玩吗? [y]  [n]")
    Choose = input()

    if Choose == 'y' or Choose == 'Y':
        flag = True
    else:
        flag = False
```

def是声明一个函数，def 函数名（参数列表）:

相比，Python还是比c++代码长度短，诶:sweat:

