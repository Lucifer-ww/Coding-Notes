import pygame

WIN_WIDTH = 400
WIN_HEIGHT = 600
pygame.init()
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("动画的灵活运用")
titlelineico = pygame.image.load("img/airplane.ico")  # 导入窗口图标，规格：32x32，格式：.ico
pygame.display.set_icon(titlelineico)  # 设置窗口图标
window.fill((255, 255, 255))
pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            print("键盘按下", chr(event.key))
        elif event.type == pygame.KEYUP:
            print("键盘抬起", chr(event.key))