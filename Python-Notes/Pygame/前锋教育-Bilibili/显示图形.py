import pygame
pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("显示图形")
# 设置背景颜色
window.fill((255, 255, 255))
pygame.display.update() #就连设置颜色都需要更新一次

# ============显示图形============
#1画直线
#line()
pygame.draw.line(window, (234, 190, 233), (20, 20), (90, 90), 2) #一看这就是斜线
window.blit(window, (0, 0))
pygame.display.update()

#2画折线
#lines()
points = [(10, 300), (100, 160), (180, 260), (300, 100)]
pygame.draw.lines(window, (0, 255, 0), True, points, 3)
window.blit(window, (0, 0))
pygame.display.update()

#3画圆
#circle()
pygame.draw.circle(window, (0, 0, 255), (200, 250), 100, 2)

#4矩形
pygame.draw.rect(window, (120, 20, 60), (100, 70, 200, 100), 0)
pygame.display.update()

#5椭圆
pygame.draw.ellipse(window, (255, 0, 0), (30, 70, 100, 200), 3)
pygame.display.update()

#6弧线
pygame.draw.arc(window, (0, 0, 0), (30, 70, 100, 200), 0, 3.1415926, 7)
pygame.display.update()

# ==============================
flag = True
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()