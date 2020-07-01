# coding: UTF-8
'''@Author: Thomas'''
import pygame

WIN_WIDTH = 400 # 常量宽
WIN_HEIGHT = 600 # 常量高

pygame.init()

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("动画原理")
window.fill((255, 255, 255)) # 填充为白色
pygame.display.flip() # 刷新动画

# 静态动画编辑位置
# 1、显示静态球
y = 100
pygame.draw.circle(window, (255, 0, 0), (100, y), 50)
pygame.display.update()

flag = True
while flag:
	# 帧动画编辑位置
	pygame.draw.circle(window, (255, 255, 255), (100, y), 50)
	y = y + 1
	pygame.draw.circle(window, (255, 0, 0), (100, y), 50)
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
