'''
@Author: Thomas
@Date: 2020-06-14 19:56:36
@LastEditTime: 2020-06-14 20:05:54
@Description: Pygame设置文字
@FilePath: \Coding-Notes\Python-Notes\Pygame\前锋教育-Bilibili\显示文字.py
'''

import pygame

pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("显示文字")
# 设置背景颜色
window.fill((255, 255, 255))
pygame.display.update()  # 就连设置颜色都需要更新一次

# ===========显示文字==========
# 1.创建字体对象
# Pygame自带的模块font
# pygame.font.SysFont() 系统字体，一般无法支持中文
# Font(字体文件路径， 字号) 我就问问为什么不能直接一个字符串，写上字体名！

ft = pygame.font.Font("Font/msyh.ttc", 40)

# 2.创建文字对象
# render(文字内容, True, 文字颜色， 背景颜色（可以不设）) #是否平滑一定是True
text = ft.render("游戏你好", True, (205, 85, 85), (240, 225, 240))  # 背景颜色不写

# 3.渲染到窗口上
window.blit(text, (0, 0))

# 3.1 获取大小

w, h = text.get_size()
window.blit(text, (600 - w, 600 - h))
# 3.2 缩放和旋转
new1 = pygame.transform.scale(text, (200, 50))
window.blit(new1, (0, 60))

new2 = pygame.transform.rotozoom(text, 0, 2)  # 不旋转，放大二倍
window.blit(new2, (0, 120))

new3 = pygame.transform.rotozoom(text, 90, 2)  # 旋转九十度
window.blit(new3, (0, 250))
# 4.刷新窗口
pygame.display.update()
flag = True
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
