'''
@Author: thomas
@Date: 2020-06-14 14:11:25
@LastEditTime: 2020-06-14 18:23:32
@LastEditors: Please set LastEditors
@Description: Pygame添加图片
@FilePath: \Coding-Notes\Python-Notes\Pygame\前锋教育-Bilibili\添加图片.py
'''
# __author__=="thomas"
import pygame
pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("显示图片")
# 设置背景颜色
window.fill((255, 255, 255))
# ============游戏开始页面静态效果==========
#1.加载图片
img = pygame.image.load("Img/Plain.png") #如果你要尝试，要么图片放在原位，要么改变路径
#2.渲染图片
#blit(渲染对象，坐标)
window.blit(img, (0, 1))

w, h = img.get_size() #获取宽高
#print(w, h) 输出测试
window.blit(img, (600-w, 600-h)) #放在右下角

new1 = pygame.transform.scale(img, (100, 200)) #缩放为x=100，y=200，变形了
window.blit(new1, (210, 0)) #靠右一点放置

new2 = pygame.transform.rotozoom(img, 0, 0.5) #不旋转为0，缩放百分比为0.5
window.blit(new2, (0, 200))
#3.刷新显示页面
#1.第一次刷新用它 pygame.display.flip()
#2.不是第一次刷新
pygame.display.update() #刷新
#==================================
flag = True
while flag:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

            