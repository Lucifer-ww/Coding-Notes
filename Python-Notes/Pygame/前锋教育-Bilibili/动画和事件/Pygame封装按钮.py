import pygame
WIN_WIDTH = 400
WIN_HEIGHT = 600
pygame.init()
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Calc")
titlelineico = pygame.image.load("img/airplane.ico")  # 导入窗口图标，规格：32x32，格式：.ico
pygame.display.set_icon(titlelineico)  # 设置窗口图标
window.fill((240, 240, 240))
pygame.display.flip()
ft = pygame.font.Font("Font/msyh.ttc", 25)

def button(name, bx, by, bw, bh):
    text1 = ft.render(name, True, (255, 255, 255))
    tw, th = text1.get_size()
    tx1 = bx + bw/2 - tw/2
    ty1 = by + bh/2 - th/2
    window.blit(text1, (tx1, ty1))
    pygame.display.update()
BTH = 100
BTY = 60
pygame.draw.rect(window, (255, 0, 0), (100, 100, BTH, BTY), 0)
button("取消", 100, 100, BTH, BTY)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()