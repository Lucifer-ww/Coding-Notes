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