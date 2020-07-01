import random
import math
from tkinter import *
from tkinter.font import Font
import time
import matplotlib.pyplot as plt
import csv


def PrintMatrix():
    # 按照格式输出数独
    x = 0
    for i in matrix:
        print("|", end="")
        for j in i:
            print(" %d |" % j, end="")
        print("\n", end="")
        x += 1
        if x % 3 == 0:
            for item in range(0, 9):
                print("  - ", end="")
            print("")


def labmapget():
    ret = str()
    for item in range(0, 9):
        # print("  - ", end="")
        ret += "-- "
    ret += "\n"
    x = 0
    for i in matrix:
        # print("|", end="")
        ret += "|"
        for j in i:
            # print(" %d |" % j, end="")
            ret += " {0} |".format(j)
        # print("\n", end="")
        ret += "\n"
        x += 1
        if x % 3 == 0:
            for item in range(0, 9):
                # print("  - ", end="")
                ret += "-- "
            # print("")
            ret += "\n"
    return ret



matrix = []


# 生成一个随机的数组
def get_random_unit():
    _num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(_num_list)
    return _num_list


def print_grid(arr):
    for i in range(9):
        print(arr[i])


def get_row(row):
    row_arr = []
    for v in matrix[row]:
        if v == 0:
            continue
        row_arr.append(v)
    return row_arr


def get_col(col):
    col_arr = []
    for i in range(9):
        val = matrix[i][col]
        if val == 0:
            continue
        col_arr.append(matrix[i][col])
    return col_arr


def isrep(num, bx, ex, by, ey, ix, iy) -> bool:
    global matrix
    # 宫内查找
    cnt = 0
    for x in range(bx, ex + 1):
        for y in range(by, ey + 1):
            if matrix[x][y] == num:
                cnt += 1
            print("in serch gg: x={0}, y={1}, cnt={2}".format(x, y, cnt))
    # print("1cnt:%d"%cnt)
    if cnt > 1:
        return False
    else:
        cnt = 0
    # 行列查找
    # 1.列
    yy = iy
    for line in range(0, 9):
        # print("in serch column: line={0}, idxy={1}".format(line, yy))
        if matrix[line][yy] == num:
            cnt += 1
    # print("2cnt:%d"%cnt)
    if cnt > 1:
        return False
    else:
        cnt = 0
    # 2.行
    xx = ix
    for column in range(0, 9):
        # print("in serch line: column={0}, idxy={1}".format(column, xx))
        if matrix[column][xx] == num:
            cnt += 1
    # print("3cnt:%d"%cnt)
    if cnt > 1:
        return False
    return True


def get_block(num):
    col_arr = []
    seq = num % 3
    col_end = 9 if seq == 0 else seq * 3
    row_end = int(math.ceil(num / 3) * 3)
    for i in range(row_end - 3, row_end):
        for j in range(col_end - 3, col_end):
            val = matrix[i][j]
            if val != 0:
                col_arr.append(matrix[i][j])
    return col_arr


def get_block_seq(row, col):
    col_seq = int(math.ceil((col + 0.1) / 3))
    row_seq = int(math.ceil((row + 0.1) / 3))
    return 3 * (row_seq - 1) + col_seq


def get_enable_arr(row, col):
    avail_arr = get_random_unit()
    seq = get_block_seq(row, col)
    block = get_block(seq)
    row = get_row(row)
    col = get_col(col)
    unable_arr = list(set(block + row + col))
    for v in unable_arr:
        if v in avail_arr:
            avail_arr.remove(v)
    return avail_arr


def cutsome():
    global matrix
    for i in range(0, 41):
        x = random.randint(0, 8)
        y = random.randint(0, 8)
        matrix[x][y] = "  "


def main():
    global matrix
    can_num = {}
    count = 0
    # 初始化一个9行9列的数组
    for i in range(9):
        matrix.append([0] * 9)

    num_list = get_random_unit()
    for row in range(3):
        for col in range(3):
            matrix[row][col] = num_list.pop(0)

    num_list = get_random_unit()
    for row in range(3, 6):
        for col in range(3, 6):
            matrix[row][col] = num_list.pop(0)

    num_list = get_random_unit()
    for row in range(6, 9):
        for col in range(6, 9):
            matrix[row][col] = num_list.pop(0)

    box_list = []
    for row in range(9):
        for col in range(9):
            if matrix[row][col] == 0:
                box_list.append({'row': row, 'col': col})

    i = 0
    while i < len(box_list):
        count += 1
        position = box_list[i]
        row = position['row']
        col = position['col']
        key = '%dx%d' % (row, col)
        if key in can_num:
            enable_arr = can_num[key]
        else:
            enable_arr = get_enable_arr(row, col)
            can_num[key] = enable_arr

        if len(enable_arr) <= 0:
            i -= 1
            if key in can_num:
                del (can_num[key])
            matrix[row][col] = 0
            continue
        else:
            matrix[row][col] = enable_arr.pop()
            i += 1

    # print_grid(matrix)
    PrintMatrix()
    cutsome()
    print(count)


def save():
    global matrix
    file = open("view/suduku.csv", "wb")
    cr = csv.writer(file)
    for i in range(0, 9):
        cr.writerow(matrix[i])
    file.close()



labmap=[]
def guisudu():
    global matrix
    global labmap
    labmap = matrix
    for x in range(0, 9):
        for y in range(0, 9):
            ftfont = Font(family="等线", size=10)
            labmap[x][y] = Label(lbf, text=matrix[x][y], relief=FLAT, width=5, height=2,
                  font=ftfont, fg="#9C5700", bg="#FFEB9C")
            labmap[x][y].grid(row=x, column=y)
            def focusdo():
                labmap[x][y].config(relief=RAISED)  # 设置边框
                putnum.focus_set()  # 输入框聚焦
            labmap[x][y].bind("<Button-1>", lambda self:focusdo()) # Lambda表达式进入函数，绑定键位鼠标单击


# 以下为GUI部分
ggt = time.time()
root = Tk()
root.title("数独面板")
root.config(bg="#9BC2E6")
main()
resultime = time.time() - ggt
print(resultime)
matmap = labmapget()
lbf = LabelFrame(root, text="数独小游戏")
lbf.pack(padx=20, pady=20)
fontset = Font(family="等线", size=16)
guisudu()
# Label(lbf, text=matmap, width=40, fg="#9C5700", bg="#FFEB9C", font=fontset, relief=SOLID).pack(padx=20, pady=20, ipadx=20, ipady=20)
# Button(lbf, text="导出CSV", command=save).pack(side=LEFT)
putnum = Entry(root)
putnum.pack()


def pushinnum(event):
    labmap[0][0].config(text=putnum.get())
    putnum.delete(0.0, END)


putnum.bind("<Return>", pushinnum)
root.mainloop()
