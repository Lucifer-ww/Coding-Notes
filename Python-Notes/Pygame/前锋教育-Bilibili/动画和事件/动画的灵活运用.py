import pygame
from   time import sleep
from tkinter import *
from tkinter import messagebox

WIN_WIDTH = 400
WIN_HEIGHT = 600
pygame.init()
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("动画的灵活运用")
titlelineico = pygame.image.load("img/airplane.ico")  # 导入窗口图标，规格：32x32，格式：.ico
pygame.display.set_icon(titlelineico)  # 设置窗口图标
window.fill((255, 255, 255))
pygame.display.flip()

y = 100
r = 50
pygame.draw.circle(window, (255, 0, 0), (100, y), r)
pygame.display.update()


def get_speed(event):
    global y_speed
    if txt.get() == "":
        messagebox.showwarning("Error", "输入为空，按下确定重试")
    else:
        y_speed = int(txt.get())
        root.destroy()


root = Tk()
root.geometry("300x180")
root.title("AskSpeed")
lbf = LabelFrame(root, text='输入Y轴移动速度，回车确定')
lbf.pack()
txt = Entry(lbf, width=30)
txt.bind("<Return>", get_speed)
txt.focus_set()
txt.pack()
root.mainloop()
num= 0
while True:
    # 帧动画编辑位置
    # if num % 10000 == 0:
    #     pygame.draw.circle(window, (255, 255, 255), (100, y), 50)
    #     y = y + 1
    #     pygame.draw.circle(window, (255, 0, 0), (100, y), 50)
    #     pygame.display.update()
    # num += 1
    if num % 1000 == 0:
        sleep(0.001)
        pygame.draw.circle(window, (255, 255, 255), (100, y), r)
        y = y + y_speed
        if y > 550:
            y_speed = -y_speed
        if y < 50:
            y_speed = -y_speed
        pygame.draw.circle(window, (255, 0, 0), (100, y), r)
        pygame.display.update()
    num += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()