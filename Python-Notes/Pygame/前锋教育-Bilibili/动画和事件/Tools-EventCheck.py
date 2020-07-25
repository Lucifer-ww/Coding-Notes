import pygame

WIN_WIDTH = 400
WIN_HEIGHT = 600
pygame.init()
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("事件检测")
titlelineico = pygame.image.load("img/airplane.ico")  # 导入窗口图标，规格：32x32，格式：.ico
pygame.display.set_icon(titlelineico)  # 设置窗口图标
window.fill((255, 255, 255))
pygame.display.flip()
y = 200
x = 200
r = 50
flag = False
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            exit()
