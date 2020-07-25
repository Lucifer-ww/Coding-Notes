from time import sleep
import pygame
import random

pygame.init()
window = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Thomas的游戏")
window.fill((255, 255, 255))

# ========加载任务========
player = pygame.image.load("Img/plane.png")
window.blit(player, (168, 536))
pygame.display.update()

flag = True
num = 0
while flag:
    if num % 10000 == 0:
        sleep(0.5)
        bpng = pygame.image.load("Img/barrier.png")
        tx = random.randint(0, 400)
        window.blit(bpng, (tx, 50))
        pygame.display.update()
    num += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
