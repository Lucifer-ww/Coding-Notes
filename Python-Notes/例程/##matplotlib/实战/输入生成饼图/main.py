import matplotlib.pyplot as plt
from tkinter.ttk import *
from tkinter import *

# 切片个数
# 每个切片的占比
# 每个切片的名称
# 选择输入颜色


def askPrint(fault):
    choose = input("是否打印异常？(Y/N)> ")
    if choose == "Y":
        print(fault)
    else:
        pass


tgt = int(input("输入切片个数> "))
print("-------------------------")
ls = list()
index = 0
while index != tgt:
    try:
        tmp = int(input("输入切片占比> "))
        ls.append(tmp)
    except ValueError as fault:
        print("输入格式错误")
        askPrint(fault)
        continue
    index += 1

print("-------------------------")
cols = list()
for i in range(0, tgt):
    cols.append(input("输入颜色> "))
print("-------------------------")
names = list()
for i in range(0, tgt):
    names.append(input("输入名称> "))
print("输入完成……")
from time import sleep
sleep(0.03)
print("存储完成.")
sleep(0.001)
print("分析中…………")
print("数据拉取100%完成")
sleep(0.5)
print("数据分析中", end="")
sleep(0.9)
from pygame.display import update, flip, quit
print("...", end="")
print("完成")
print("准备成像...就绪")
plt.pie(ls, labels=names, colors=cols, startangle=90, shadow=True, autopct='%1.1f%%')
plt.title("test")
plt.show()
