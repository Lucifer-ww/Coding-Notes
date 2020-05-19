# coding: UTF-8
#!/usr/bin/python3

from tkinter import *
import random
import time
from datetime import datetime
import os

# ---------------------------check---------------------------

#查看


def check(index:str, commit:str) -> list:
    # 首先需要一个记录原来字符串长度
    aclen = 0.0
    celen = 0.0
    zql = 0.0 #正确率
    # 循环遍历
    for i, j in zip(index, commit):
        if i == j:
            aclen += 1.0
            print('aclen++, aclen={0}'.format(aclen))
        else:
            celen += 1.0
            print('celen++, celen={0}'.format(celen))
    zql = float(aclen / 50) * 100.0
    print('zql={0}'.format(zql))

    ainfo = [zql, aclen, celen]
    return ainfo
# ---------------------------check---------------------------


constin = None  # 输入汇总changliang
cyongshi = None  # 用时
timestrS = datetime.utcnow()  # 时间记录器-first
timestrLast = 0  # 时间记录器-last
chstr = None

ft = r"E:\ProgramThomas\Coding-Notes\Project\PYT\打字游戏Python的GUI界面\resource\loggerstr.log"
'''
def msgShow():
    label["text"] = 'I Love Python'
    label["bg"] = 'orangerad'
'''


def getStr(ent):
    global constin
    # 返回Entry的值
    tmp = ent.get()
    print("输入：{0}".format(tmp))
    fff.write("\n"+tmp)
    constin = tmp


def pushStart():
    # timestrS=time.time()
    timestrS = datetime.utcnow()
    print("get timestamp start of->timestrS={0}".format(timestrS))
'''
def itg(chstr, constin):
    #"时间:"+str(cyongshi)+'秒'
    ccList = check(chstr, constin)
    endstr = "时间:" + str(cyongshi) + '秒' + '\n'
    endstr += '正确率:' + str(ccList[0]) + '\n'
    endstr += '对了:' + str(ccList[1]) + '个\n'
    endstr += '错了:' + str(ccList[2]) + '个\n'
    return endstr
'''


def pushEnd():
    getStr(intxt)
    global cyongshi
    #fmmf = time.time()
    fmmf = datetime.utcnow()
    #timtmp = fmmf - timestrS
    timtmps = timestrS.second+timestrS.minute*60
    timtmpe = fmmf.second+fmmf.minute*60
    #print("get timestamp this of->time.time()={0}".format(time.time()))
    #print("get timestamp minx of->timtmp={0}".format(timtmp))
    timestrLast = timtmpe - timtmps
    print("get timestamp end of->timestrLast={0}".format(timestrLast))
    print("时间：{0}".format(timestrLast))
    cyongshi = timestrLast

    ccList = check(chstr, constin)
    endstr = "时间:" + str(cyongshi) + '秒' + '\n'
    endstr += '正确率:' + str(ccList[0]) + '\n'
    endstr += '对了:' + str(ccList[1]) + '个\n'
    endstr += '错了:' + str(ccList[2]) + '个\n'
    #PHOTO IMAGE
    lbot = Label(root, width=50, text=endstr,
             #bitmap='',
             compound='left',
             anchor=SW,
             bg='skyblue')
    lbot.grid()


# --------------------------------
root = Tk()
root.title("打字游戏GUI")
root.iconbitmap("iconbitmap.ico")
root.geometry("500x400")  # 779*655
lb = Label(root, bitmap="hourglass",
           compound="left",
           cursor="target",
           text="AC打字通",
           fg="blue", bg="yellow",
           anchor=CENTER, font=("Helvetic", 20, "bold")
           )
# r"E:\ProgramThomas\Coding-Notes\Project\PYT\打字游戏Python的GUI界面\resource\BITMAP_TITLE.ico"
lb2 = Label(root, bitmap="question",
            compound="left",
            text="提示：打字游戏，点击 开始 按钮即开始计时，最后点击 提交 按钮即可",
            fg="#FF0000", bg="lightyellow",
            )

characters = []  # 0~26
for i in range(0, 50):
    tmp = random.randint(0, 25)
    characters.append(chr(ord('a') + tmp))

# print(characters)
chstr = ""
for i in characters:
    chstr += i

print(chstr)
fff = open(ft, 'a+')
fff.write('\n'+chstr)
lbtip = Label(root, bitmap="info",
              compound="left",
              text="样例" + chstr,
              fg="green", bg="#cccccc",
              font=("simsun", 12), underline=True)
# Entry cursor circle

INframe = Frame(root, width=70)  # 定义输入框架
intxtL = Label(INframe, text="输入> ")

intxt = Entry(INframe, width=50, show="*")

btnframe = Frame(root, width=60)
# BUTTON 按钮    开始和结束
btnStart = Button(btnframe, text="开始输入", fg="blue", width=20,
                  command=pushStart)
btnEnd = Button(btnframe, text="输入结束", fg="blue", width=20,
                command=pushEnd)
btnExit = Button(btnframe, text='退出程序', fg="red", width=20,
                 command=root.destroy)

#cc = Cac(chstr, constin)   class init to cc var


lb.grid()
lb2.grid()
lbtip.grid()
INframe.grid()
intxtL.grid(row=3, column=0, sticky=W)  # 输入>Label
intxt.grid(row=3, column=1)  # 输入框Entry th
btnframe.grid()


btnStart.grid(row=4, column=0)
btnEnd.grid(row=4, column=1)
btnExit.grid(row=4, column=2)


#lbot.grid()

# textTip = Text(root)
# textTip.pack(fill=BOTH, expand=True, padx=3, pady=2)
# textTip.insert(END, chstr)
root.mainloop()
print("时间={0}".format(cyongshi))
