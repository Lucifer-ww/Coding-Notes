import turtle

from random import random
from random import randint
def draw_petal(turtle_obj, flower):
    # 绘制掉落的花瓣
    turtle.hideturtle()
    for i in range(int(flower)):
        # 有正有负就可以让画笔往二个方向走
        x = flower - 4 * flower * random()

        # 花瓣整体宽度(-10, 10)
        y = 10 - 20 * random()

        # 提笔，向前y，左转90，走x，落笔
        turtle_obj.penup()
        turtle_obj.forward(y)
        turtle_obj.left(90)
        turtle_obj.forward(x)
        turtle_obj.pendown()

        # 珊瑚色
        turtle_obj.pencolor("lightcoral")
        # 画圆
        turtle_obj.circle(1)

        # 回到起点
        # 提笔，后退x，右转90,后退y，落笔
        turtle_obj.penup()
        turtle_obj.backward(x)
        turtle_obj.right(90)
        turtle_obj.backward(y)
        turtle_obj.pendown()


# 画树枝部分
def draw_tree(turtle_obj, branch, tree_color):
    # 设置一个最小分支长度
    turtle.hideturtle()
    min_branch = 4

    if branch > min_branch:
        if branch < 8:
            # 以0.5的概率，向左、右分支
            if randint(0, 1) == 0:
                # 左为白色
                turtle_obj.pencolor("snow")
            else:
                # 右为珊瑚色
                turtle_obj.pencolor("lightcoral")
            # 枝干
            turtle_obj.pensize(branch / 2)
        elif 8 <= branch <= 16:
            # 以0.33的概率，分为左、中、右分支
            if randint(0, 2) == 0:
                # 左为白色
                turtle_obj.pencolor("snow")
            else:
                # 中、右为珊瑚色
                turtle_obj.pencolor("lightcoral")
            # 树枝
            turtle_obj.pensize(branch / 4)
        else:
            # 褐色
            turtle_obj.pencolor(tree_color)
            # 细枝
            turtle_obj.pensize(branch / 10)

        # 最开始的树干长度
        turtle_obj.forward(branch)

        # 随机度数因子
        a = 1.5 * random()
        # 顺时针旋转随机角度（0～30度）
        turtle_obj.right(20 * a)

        # 随机长度因子
        b = 1.5 * random()
        # 往右画，直到画不动为止
        draw_tree(turtle_obj, branch - 10 * b, tree_color)

        # 左转随机角度
        turtle_obj.left(40 * a)
        # 往左画，直到画不动位置
        draw_tree(turtle_obj, branch - 10 * b, tree_color)

        # 右转一定角度
        turtle_obj.right(20 * a)
        # 提笔
        turtle_obj.penup()

        # 递归结束回到起点
        turtle_obj.backward(branch)
        turtle_obj.pendown()


def get_screen(width, height, color, speed):
    # 创建画幕
    screen_obj = turtle.Screen()
    # 画布大小：(width, height)，颜色：color
    screen_obj.screensize(width, height, bg=color)
    screen_obj.setup(1.0, 1.0)
    # speed倍加速
    screen_obj.tracer(speed)

    return screen_obj


def trees(tree_num):
    # 颜色
    color = ['brown', 'tan', 'black']

    for j in range(tree_num):
        # 树干颜色
        tree_color = color[randint(0, len(color) - 1)]

        # 画笔大小
        pensize = randint(2, 5)
        # 前进像素
        forward = ((-1) ** pensize) * pensize * randint(20, 50)
        # 后退像素
        if pensize <= 3:
            backward = ((-1) ** pensize) * (5 - pensize) * randint(10, 15)
        else:
            backward = pensize * randint(45, 50)

        # 创建画笔
        turtle_obj = turtle.Turtle()
        # 画笔粗细
        turtle_obj.pensize(pensize)
        # 提笔，向前forward，左转90，backward，落笔
        turtle_obj.penup()
        turtle_obj.forward(forward)
        turtle_obj.left(90)
        turtle_obj.backward(backward)
        turtle_obj.pendown()
        # 画笔颜色：褐色
        turtle_obj.pencolor(tree_color)

        # 枝干粗细
        branch = pensize * 15
        # 落花数
        flowers = branch
        # 第j棵树
        draw_tree(turtle_obj, branch, tree_color)
        # 花瓣
        draw_petal(turtle_obj, flowers)


if __name__ == '__main__':
    # 创建画幕
    my_screen_width = 800
    my_screen_height = 600
    my_screen_color = 'wheat'
    my_screen_speed = 5
    my_screen_obj = get_screen(my_screen_width, my_screen_height,
                               my_screen_color, my_screen_speed)

    # 樱花树
    # 棵数
    my_tree_num = 5
    trees(my_tree_num)

    # 点击关闭画布
    my_screen_obj.exitonclick()