import pygame
from random import randint
from time import sleep

pygame.init()
window = pygame.display.set_mode((600, 800), pygame.VIDEORESIZE)
pygame.display.set_caption("XXX")
window.fill((255, 255, 255))
pygame.display.update()
# 	R	G	B
# 红	255	0	0
# 橙	255	150	0
# 黄	255	255	0
# 绿	0	255	0
# 青	0	255	255
# 蓝	0	0	255
# 紫	150	0	255

colors = ((255, 0, 0), (255, 150, 0), (255, 255, 0), (0, 255, 0), (0, 255, 255), (150, 0, 255))
item = 0
flag = False
y = 0
x = 0
r = 50
cnt6 = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == 27:
                pygame.display.update()
        if event.type == pygame.VIDEORESIZE:
            SCREEN_SIZE = event.size
            window = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE)
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     x, y = event.pos
        #     flag = True
        # elif event.type == pygame.MOUSEBUTTONUP:
        #     flag = False
        # if event.type == pygame.MOUSEMOTION and flag:
        #     # pygame.draw.circle(window, (255, 255, 255), (x, y), r)
        #     x, y = event.pos
        #     pygame.draw.circle(window, colors[item], (x, y), r)
        #     pygame.display.update()
        tx = randint(0, 599)
        ty = randint(0, 799)
        pygame.draw.circle(window, colors[item], (tx, ty), r)
        if item == 5:
            item = 0
        else:
            item += 1
    pygame.display.update()