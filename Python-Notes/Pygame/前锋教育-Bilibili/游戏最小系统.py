# __author__=="thomas"

import pygame #导入库

# 1.初始化操作

pygame.init()


#2. 创建游戏窗口

window = pygame.display.set_mode((400, 600))
# 设置游戏标题，标题
pygame.display.set_caption("Thomas的游戏")
# 3.让游戏保持一直运行的状态
# 写个死循环吧  game loop (游戏循环)
flag = True #循环控制
while flag:
	# 4.检测事件
	for event in pygame.event.get(): #获取事件
		# 检测关闭按钮被点击的事件
		if event.type == pygame.QUIT:
			exit() #结束这一个线程
			#flag = False