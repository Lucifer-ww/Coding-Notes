# __author__=="thomas"

import pygame #导入库

# 1.初始化操作

pygame.init()


#2. 创建游戏窗口

window = pygame.display.set_mode((400, 600))


# 3.让游戏保持一直运行的状态
# 写个死循环吧  game loop (游戏循环)

while True:
	# 4.检测事件
	for event in pygame.event.get(): #获取事件
		pass