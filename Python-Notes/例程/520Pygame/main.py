import pygame
import random
from turtle import *
import time

# 设置屏幕大小
WIDTH, HEIGHT = 1014, 605
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('520 属于你的表白日')


# 添加文本信息
def title(text, screen, scale, color=(0, 0, 0)):
    font = pygame.font.SysFont('KaiTi', 25)
    textRender = font.render(text, True, color)
    screen.blit(textRender, (WIDTH / scale[0], HEIGHT / scale[1]))


# 设置按钮信息
def button(text, x, y, w, h, color, screen, color_text):
    pygame.draw.rect(screen, color, (x, y, w, h))
    font = pygame.font.SysFont('KaiTi', 25)
    textRender = font.render(text, True, color_text)
    textRect = textRender.get_rect()
    textRect.center = ((x+w/2), (y+h/2))
    screen.blit(textRender, textRect)


# 生成随机的位置坐标
def get_random_pos():
    x, y = random.randint(20, 620), random.randint(20, 460)
    return x, y


# 点击YES后显示的页面
def show_like_interface(screen):
    def setTurtle():
        screensize(1200, 900, 'pink')
        pensize(3)
        speed(12)
        penup()

    def getStart(h):
        # 去到的坐标,窗口中心为0,0
        goto(0, -180)
        r = h / 5
        drawBigL(r, h)
        drawBigArc(r, 140)
        drawBigArc(r, 70)
        drawBigR(r, h)
        centerRange()
        drawHope()
        drawName()

    def drawBigL(r, h):
        colors = ['red', 'orange', 'yellow', '#87CEEB', 'violet', 'red']
        for i in range(int(240 / h) + 1):
            seth(0)
            color(colors[i], colors[i + 1])
            drawHeart(r)
            seth(140)
            fd(h)

    def drawBigArc(r, rad):
        colors = ['red', 'orange', 'yellow', 'SkyBlue', 'violet', 'red']
        for i in range(50):
            if (i % 10 == 0):
                color(colors[int(i / 10)], colors[int(i / 10) + 1])
                seth(0)
                drawHeart(r)
                seth(rad - (i + 1) * 4)
            rt(4)
            fd(10.5)

    def drawBigR(r, h):
        colors = ['red', 'orange', 'yellow', 'SkyBlue', 'violet', 'red']
        for i in range(int(240 / h) + 1):
            color(colors[i], colors[i + 1])
            seth(0)
            drawHeart(r)
            setheading(220)
            fd(h)

    def drawHeart(r):
        down()
        begin_fill()
        factor = 180
        seth(45)
        circle(-r, factor)
        fd(2 * r)
        right(90)
        fd(2 * r)
        circle(-r, factor)
        end_fill()
        up()

    # 在大心中写字
    def centerRange():
        for i in range(6):
            drawCenter(i)
            time.sleep(1)

    def drawCenter(i):
        goto(-85, 0)
        colors = ['red', 'orange', 'yellow', 'SkyBlue', 'violet', 'red']
        pencolor(colors[i])
        write('love 荣仔', font=('gungsuh', 30,), )
        up()

    # 写情话
    def drawHope():
        pencolor('black')
        goto(-310, -170)
        showturtle()
        write('情书给你一封', font=('华文行楷', 20,), move=True)
        goto(-290, -200)
        write('情话给你一句', font=('华文行楷', 20,), move=True)
        goto(-260, -230)
        write('余生给你一人', font=('华文行楷', 20,), move=True)

    # 写日期
    def drawName():
        pencolor('black')
        goto(150, -200)
        showturtle()
        write('2020年5月20日 ', font=('华文行楷', 20,), move=True)

    setTurtle()
    getStart(80)

    # 点击窗口关闭
    window = Screen()
    window.exitonclick()


# 点击NO按钮后返回程序开头重新执行
def show_unlike_interface(screen):
    return main()


def main():
    num = 0
    pygame.init()
    clock = pygame.time.Clock()

    # 添加背景音乐
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play(-1, 40)
    pygame.mixer.music.set_volume(0.5)

    # 设置YES按钮属性
    unlike_pos_x = 130
    unlike_pos_y = 375
    unlike_pos_width = 450
    unlike_pos_height = 55
    unlike_color = (115, 76, 243)

    # 设置NO按钮属性
    like_pos_x = 130
    like_pos_y = 280
    like_pos_width = 450
    like_pos_height = 55
    like_color = (115, 76, 243)

    running = True
    while running:
        # 填充窗口
        screen.fill((255, 255, 255))
        # 添加背景图
        background = pygame.image.load('love520.PNG').convert()
        screen.blit(background, (0, 0))

        # 获取鼠标坐标
        pos = pygame.mouse.get_pos()
        if pos[0] < unlike_pos_x + unlike_pos_width + 5 and pos[0] > unlike_pos_x - 5 and pos[1] < unlike_pos_y + unlike_pos_height + 5 and pos[1] > unlike_pos_y - 5:
            while True:
                if num > 5:
                    break
                num += 1
                unlike_pos_x, unlike_pos_y = get_random_pos()
                if pos[0] < unlike_pos_x + unlike_pos_width + 5 and pos[0] > unlike_pos_x - 5 and pos[1] < unlike_pos_y + unlike_pos_height + 5 and pos[1] > unlike_pos_y - 5:
                    continue
                break

        # 设置撩动女生助你表白成功的话及按钮内容信息等
        title('你是不是喜欢我？', screen, scale=[8, 3])
        button('YES', like_pos_x, like_pos_y, like_pos_width,
               like_pos_height, like_color, screen, (255, 255, 255))
        # 设置一些套路
        # 当拒绝次数小于6时，并未执行小矩形不动的程序，当将要触碰时小矩形还可继续随机跳动
        if num < 6:
            button('NO', unlike_pos_x, unlike_pos_y, unlike_pos_width,
                   unlike_pos_height, unlike_color, screen, (255, 255, 255))
        if num > 5:
            button('看来我只能接收喜欢你的事实咯', unlike_pos_x, unlike_pos_y, unlike_pos_width,
                   unlike_pos_height, unlike_color, screen, (255, 255, 255))
        # 设置知道她喜欢你事实的文本
        if num == 1:
            button('一看见你就对我傻笑', unlike_pos_x, unlike_pos_y - 50, unlike_pos_width,
                   unlike_pos_height, (255, 255, 255), screen, (192, 0, 0))
        if num == 2:
            button('天天来看我的朋友圈', unlike_pos_x, unlike_pos_y - 50, unlike_pos_width,
                   unlike_pos_height, (255, 255, 255), screen, (192, 0, 0))
        if num == 3:
            button('一抄作业就来找我', unlike_pos_x, unlike_pos_y - 50, unlike_pos_width,
                   unlike_pos_height, (255, 255, 255), screen, (192, 0, 0))
        if num == 4:
            button('滚滚红尘', unlike_pos_x, unlike_pos_y - 50, unlike_pos_width,
                   unlike_pos_height, (255, 255, 255), screen, (192, 0, 0))
        if num == 5:
            button('我喜欢你的同时', unlike_pos_x, unlike_pos_y - 50, unlike_pos_width,
                   unlike_pos_height, (255, 255, 255), screen, (192, 0, 0))
        if num == 6:
            button('正好你也喜欢我', unlike_pos_x, unlike_pos_y - 50, unlike_pos_width,
                   unlike_pos_height, (255, 255, 255), screen, (192, 0, 0))

        # 当拒绝次数达到峰值时，跳转到NO指定程序，即回到main()函数重新执行，达到女神不得不答应你的目的
        if num > 5:
            if pos[0] < unlike_pos_x + unlike_pos_width + 5 and pos[0] > unlike_pos_x - 5 and pos[1] < unlike_pos_y + unlike_pos_height + 5 and pos[1] > unlike_pos_y - 5:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    show_unlike_interface(screen)

        # 当点击窗口关闭按钮时，亦关闭不了，直到承认喜欢你的事实后方可结束程序
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return main()

        # 点击YES按钮
        if pos[0] < like_pos_x + like_pos_width + 5 and pos[0] > like_pos_x - 5 and pos[1] < like_pos_y + like_pos_height + 5 and pos[1] > like_pos_y - 5:
            if event.type == pygame.MOUSEBUTTONDOWN:
                show_like_interface(screen)

        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)


main()
