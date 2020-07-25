import pygame

pygame.init()
window = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Thomas的游戏")
window.fill((255, 255, 255))
pygame.display.update()
flag = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag = True
        elif event.type == pygame.MOUSEBUTTONUP:
            flag = False
        if event.type == pygame.MOUSEMOTION and flag:
            pass





