# coding: utf-8
'''
from tkinter import *

root = Tk()

def calc():
    for i in s:
        if i == 'c':
            lbmark['bg'] = 'green'
        else:
            lbmark['bg'] = 'red'

s = 'abcdef'
lbmark = Label(root, text=s, bg='azure')

calc()

lbmark.grid()
root.mainloop()
'''
# 本课程中所有的GUI程序，都必须有这一句话
from tkinter import *

# 函数定义语句，定义了计算过程


def calculate():
    # get方法获得的对象是文本类型，必须转换为整数类型（int）才能用于进制转换
    value = int(entry.get())
    # 用修改颜色的方法来表示输出
    if value % 2 == 0:
        lbMark['bg'] = 'green'
    else:
        lbMark['bg'] = 'red'


# root 是主窗口
root = Tk()

# 给主窗口定一个标题
root.title("偶数检测器")

# 纯提示用的标签（类型Label），属于root窗口，不必起名字，定义后直接布局
Label(root, text="请输入一个数字：").grid(column=1, row=1, padx=10, pady=10)
# 输入数字，单行文本输入框（类型Entry），它属于root窗口
entry = Entry(root)
entry.grid(column=2, row=1, padx=10, pady=10)

# 输出用的标签（类型Label），属于root窗口
# 标记留白，通过改变整个Label的背景色来实现分类输出
lbMark = Label(root, text="    ")
lbMark.grid(column=2, row=2, padx=10, pady=10)

# 按钮（类型Button），属于root窗口，显示文字是“检测”，按下去动作（command）是函数calculate
# 无须起名，因为后面不用访问按钮本身
Button(root, text="检测", command=calculate).grid(
    column=1, row=2, padx=10, pady=10)


# 这一句是运行窗口
root.mainloop()
