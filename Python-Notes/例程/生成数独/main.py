#!/usr/bin/env python3
# -*- coding: UTF -*-

import random
import math
import time
import pathlib
import os
import os.path
import sys


# 生成一个随机的数组
def get_random_unit():
    _num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(_num_list)
    return _num_list


def PrintMatrix():
    # 按照格式输出数独
    x = 0
    for i in matrix:
        print("|", end="")
        for j in i:
            print(" %d |"%j, end="")
        print("\n", end="")
        x += 1
        if x % 3 == 0:
            for item in range(0, 9):
                print("  - ", end="")
            print("")


def isrep(num, bx, ex, by, ey, ix, iy)->bool:
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
    else: cnt = 0
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


def TwoD_rand(xyf: tuple, xye: tuple):
    global matrix
    # 打开一些文件
    file = open(r"log\xy.log", 'a+')
    tmpxy = open(r"log\tmpxy.log", 'a+')
    blxy = open(r"log\blxy.log", 'a+')
    # 无聊且骚的操作将坐标取出
    xf = xyf[0]; xe = xye[0] # 发现重大bug，已改
    yf = xyf[1]; ye = xye[1] # bug是元组名称写反
    # 打印日志
    print("xf={0}, xe={1}, yf={2}, ye={3}".format(xf, xe, yf, ye))
    tmpxy.write("xf={0}, xe={1}, yf={2}, ye={3}\n".format(xf, xe, yf, ye))
    # 遍历选区
    # 比如第一次的坐标范围是(0, 0)~(2, 2) 0, 1, 2
    for x in range(xf, xe + 1):
        for y in range(yf, ye + 1):
            # 打印日志
            log = str(x) + ", " + str(y) + "\n"
            file.write(log)
            blxy.write("x={0}, y={1}\n".format(x, y))
            # ----------------------
            flag = True
            while flag:
                tmp = random.randint(1, 9)
                print("in x={0}, y={1}, tmp={2}".format(x, y, tmp))
                matrix[x][y] = tmp
                flag = not(isrep(tmp, xf, xe, yf, ye, x, y))


def get_gblock():
    global matrix
    pass



'''
测试一个宫：
——————————————————————————————————
| 9-(0, 0) | 10(0, 1) | 10(0, 2) |
| 10(1, 0) | 10(1, 1) | 10(1, 2) |
| 10(2, 0) | 10(2, 1) | 10(2, 2) |3
                              3
'''


# 9 * 9
# 第一个格随机生成，random.randint(0, 9)
def main():
    global matrix
    # 使用列表推导式推出二维列表地图，初始化都为10
    matrix = [[10 for i in range(9)] for i in range(9)]
    '''
    tmp = random.randint(0, 9)
    matrix[0][0] = tmp
    '''
    
    # 接下来每一个3*3的宫生成一组
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
    TwoD_rand((0, 3), (2, 5))
    TwoD_rand((0, 6), (2, 8))
    TwoD_rand((3, 0), (5, 2))
    TwoD_rand((3, 6), (5, 8))
    TwoD_rand((6, 0), (8, 2))
    TwoD_rand((6, 3), (8, 5))
    PrintMatrix()

ggt = time.time()
main()
resultime = time.time() - ggt
print(resultime)
