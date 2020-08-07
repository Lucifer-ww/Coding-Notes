# __author__=="thomas"

import pygame  # 导入库

# 1.初始化操作

pygame.init()

# 2. 创建游戏窗口

window = pygame.display.set_mode((400, 600))
# 设置游戏标题，标题
pygame.display.set_caption("Thomas的游戏")
window.fill((255, 255, 255))
# 3.让游戏保持一直运行的状态
# 写个死循环吧  game loop (游戏循环)
img = pygame.image.load("img/umaru.jpg") # 我就喜欢小埋!
window.blit(img, (180, 180))
flag = True  # 循环控制
y = r = x = 0
from time import sleep
while flag:
    sleep(0.02)
    pygame.draw.circle(window, (255, 255, 255), (150, y), r)
    window.blit(img, (180, 180)) # 重新渲染
    y += 4
    r += 1
    pygame.draw.circle(window, (255, 0, 0), (150, y), r)
    pygame.display.update()
    # 4.检测事件
    for event in pygame.event.get():  # 获取事件
        # 检测关闭按钮被点击的事件
        if event.type == pygame.QUIT:
            exit()  # 结束这一个线程
    # flag = False
