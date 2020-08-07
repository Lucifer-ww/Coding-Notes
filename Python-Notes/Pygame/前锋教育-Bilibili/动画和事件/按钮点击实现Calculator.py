import pygame
from tkinter import *
from tkinter import messagebox
import winsound
import time
import win32api, win32con
lastset = 0
stra = time.time()
SLCHECK = True
def back():
    global  SLCHECK
    SLCHECK = True
    tmps = equ.get()
    ret = tmps[:-1]
    equ.set(ret)


def add(cr):
    if SLCHECK:
        tmps = equ.get()
        equ.set(tmps + cr)


def calculate():
    try:
        tmps = equ.get()
        equ.set(str(eval(tmps)))
        pygame.draw.rect(window, (252, 228, 214), (20, 140, 90, 80), 0)
        pygame.draw.rect(window, (60, 60, 60), (20, 140, 90, 80), 1)
    except SyntaxError as error:
        # # root.focus_set()
        # # messagebox.showerror("ERROR", str(error)+"\n出现计算异常")
        # root = Tk()
        # root.geometry("350x120+800+500")
        # root.title("ERROR!")
        # var = StringVar()
        # var.set(str(error) + "\n" + "eval函数出现计算异常，请重试")
        # LB = LabelFrame(root, text="不明异常，可能是输入问题")
        # LB.pack(padx=10, pady=10)
        # msg = Label(LB, textvariable=var, relief=RAISED)
        # # msg.config(bg="#EFEFEF")
        # msg.pack()
        # from tkinter import ttk as tttk
        # tttk.Button(root, text="确定", command=lambda : root.destroy()).pack()
        # root.mainloop()
        win32api.MessageBox(0, str(error) + "\n\n" + "eval() FUNCTION HAS A CALCULATION EXCEPTION\n\nMaybe INPUTERROR", "ERROR", win32con.MB_ICONWARNING)

def clear():
    global SLCHECK
    SLCHECK = True
    equ.set("")


def layout(x1, x2, x3):
    global SLCHECK
    global  lastset
    if not SLCHECK:
        equ.set(lastset)
    EQUTEXT = ft.render(equ.get(), True, (90, 90, 90))
    tx, ty = EQUTEXT.get_size()
    if tx >= 360-30:
        winsound.Beep(2000, 1)
        SLCHECK = False
    else:
        pygame.draw.rect(window, (226, 239, 218), (20, 20, 360, 100), 0)
        pygame.draw.rect(window, (0, 0, 0), (20, 20, 360, 100), 1)
        window.blit(EQUTEXT, (25, 50))
        pygame.display.update()
    # print(equ.get())
    lastset = equ.get()


WIN_WIDTH = 400
WIN_HEIGHT = 600
pygame.init()
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Calc")
titlelineico = pygame.image.load("img/airplane.ico")  # 导入窗口图标，规格：32x32，格式：.ico
pygame.display.set_icon(titlelineico)  # 设置窗口图标
window.fill((240, 240, 240))
pygame.display.flip()


root = Tk()
equ = StringVar()
equ.set("")
equ.trace("w", layout)


def button(name, bx, by, bw, bh, color):
    text1 = ft.render(name, True, color)
    tw, th = text1.get_size()
    tx1 = bx + bw/2 - tw/2
    ty1 = by + bh/2 - th/2
    window.blit(text1, (tx1, ty1))
    pygame.display.update()


# C
# /
# *
# -
###
# 7
# 8
# 9
# +
###
# 4
# 5
# 6
# +
###
# 1
# 2
# 3
# ENTER
###
# 0
# 0
# .
# ENTER
ft = pygame.font.Font("Font/msyh.ttc", 40)
textC = ft.render("C", True, (0, 0, 49))
textDel = ft.render("←", True, (190, 45, 49))
textPlus = ft.render("+", True, (190, 45, 49))
textM = ft.render("-", True, (190, 45, 49))
texttime = ft.render("*", True, (190, 45, 49))
textdi = ft.render("/", True, (190, 45, 49))
text1 = ft.render("1", True, (0, 0, 56))
text2 = ft.render("2", True, (0, 0, 56))
text3 = ft.render("3", True, (0, 0, 56))
text4 = ft.render("4", True, (0, 0, 56))
text5 = ft.render("5", True, (0, 0, 56))
text6 = ft.render("6", True, (0, 0, 56))
text7 = ft.render("7", True, (0, 0, 56))
text8 = ft.render("8", True, (0, 0, 56))
text9 = ft.render("9", True, (0, 0, 56))
text0 = ft.render("0", True, (0, 0, 56))
textENTER = ft.render("=", True, (63, 63, 118))
EQUTEXT = ft.render(equ.get(), True, (90, 90, 90))
pygame.draw.rect(window, (226, 239, 218), (20, 20, 360, 100), 0)
pygame.draw.rect(window, (0, 0, 0), (20, 20, 360, 100), 1)
BHEIGHT = 80
BWIDTH = 90
pygame.draw.rect(window, (252, 228, 214), (20, 140, 90, 80), 0)
pygame.draw.rect(window, (60, 60, 60), (20, 140, 90, 80), 1)
button("C", 20, 140, BWIDTH, BHEIGHT, color=(101, 0, 49))

pygame.draw.rect(window, (255, 199, 206), (110, 140, 90, 80), 0)
pygame.draw.rect(window, (60, 60, 60), (110, 140, 90, 80), 1)
button("DEL", 110, 140, BWIDTH, BHEIGHT, color=(156, 45, 117))
pygame.draw.rect(window, (255, 199, 206), (200, 140, 90, 80), 0)
pygame.draw.rect(window, (60, 60, 60), (200, 140, 90, 80), 1)
button("/", 200, 140, BWIDTH, BHEIGHT, color=(156, 45, 117))
pygame.draw.rect(window, (255, 199, 206), (290, 140, 90, 80), 0)
pygame.draw.rect(window, (60, 60, 60), (290, 140, 90, 80), 1)
button("*", 290, 140, BWIDTH, BHEIGHT, color=(156, 45, 117))

pygame.draw.rect(window, (221, 235, 247), (20, 220, 90, 80), 0)
pygame.draw.rect(window, (60, 60, 60), (20, 220, 90, 80), 1)
button("7", 20, 220, BWIDTH, BHEIGHT, color=(0, 0, 0))
pygame.draw.rect(window, (221, 235, 247), (110, 220, 90, 80), 0)
pygame.draw.rect(window, (60, 60, 60), (110, 220, 90, 80), 1)
button("8", 110, 220, BWIDTH, BHEIGHT, color=(0, 0, 0))
pygame.draw.rect(window, (221, 235, 247), (200, 220, 90, 80), 0)
pygame.draw.rect(window, (60, 60, 60), (200, 220, 90, 80), 1)
button("9", 200, 220, BWIDTH, BHEIGHT, color=(0, 0, 0))
pygame.draw.rect(window, (255, 199, 206), (290, 220, 90, 80), 0)
pygame.draw.rect(window, (60, 60, 60), (290, 220, 90, 80), 1)
button("+", 290, 220, BWIDTH, BHEIGHT, color=(0, 0, 0))

pygame.draw.rect(window, (221, 235, 247), (20, 300, 90, 80), 0)
pygame.draw.rect(window, (60, 60, 60), (20, 300, 90, 80), 1)
button("4", 20, 300, BWIDTH, BHEIGHT, color=(0, 0, 0))
pygame.draw.rect(window, (221, 235, 247), (110, 300, 90, 80), 0)
pygame.draw.rect(window, (60, 60, 60), (110, 300, 90, 80), 1)
button("5", 110, 300, BWIDTH, BHEIGHT, color=(0, 0, 0))
pygame.draw.rect(window, (221, 235, 247), (200, 300, 90, 80), 0)
pygame.draw.rect(window, (60, 60, 60), (200, 300, 90, 80), 1)
button("6", 200, 300, BWIDTH, BHEIGHT, color=(0, 0, 0))
pygame.draw.rect(window, (255, 199, 206), (290, 300, 90, 80), 0)
pygame.draw.rect(window, (60, 60, 60), (290, 300, 90, 80), 1)
button("-", 290, 300, BWIDTH, BHEIGHT, color=(0, 0, 0))

pygame.draw.rect(window, (221, 235, 247), (20, 380, 90, 80), 0)
pygame.draw.rect(window, (60, 60, 60), (20, 380, 90, 80), 1)
button("1", 20, 380, BWIDTH, BHEIGHT, color=(0, 0, 0))
pygame.draw.rect(window, (221, 235, 247), (110, 380, 90, 80), 0)
pygame.draw.rect(window, (60, 60, 60), (110, 380, 90, 80), 1)
button("2", 110, 380, BWIDTH, BHEIGHT, color=(0, 0, 0))
pygame.draw.rect(window, (221, 235, 247), (200, 380, 90, 80), 0)
pygame.draw.rect(window, (60, 60, 60), (200, 380, 90, 80), 1)
button("3", 200, 380, BWIDTH, BHEIGHT, color=(0, 0, 0))
pygame.draw.rect(window, (255, 204, 153), (290, 380, 90, 160), 0)
pygame.draw.rect(window, (60, 60, 60), (290, 380, 90, 160), 1)
button("=", 290, 380, BWIDTH, 160, color=(0, 0, 0))

pygame.draw.rect(window, (217, 225, 242), (20, 460, 180, 80), 0)
pygame.draw.rect(window, (60, 60, 60), (20, 460, 180, 80), 1)
button("0", 20, 460, 160, BHEIGHT, color=(0, 0, 0))
pygame.draw.rect(window, (255, 235, 156), (200, 460, 90, 80), 0)
pygame.draw.rect(window, (60, 60, 60), (200, 460, 90, 80), 1)
button(".", 200, 460, BWIDTH, BHEIGHT, color=(0, 0, 0))
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            if x >= 20 and x <= 110 and y >= 140 and y <= 220:
                pygame.draw.rect(window, (219, 219, 219), (20, 140, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (20, 140, 90, 80), 1)
                button("C", 20, 140, BWIDTH, BHEIGHT, color=(101, 0, 49))
            else:
                pygame.draw.rect(window, (252, 228, 214), (20, 140, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (20, 140, 90, 80), 1)
                button("C", 20, 140, BWIDTH, BHEIGHT, color=(101, 0, 49))
            if x >= 110 and x <= 200 and y >= 140 and y <= 220:
                pygame.draw.rect(window, (219, 219, 219), (110, 140, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (110, 140, 90, 80), 1)
                button("DEL", 110, 140, BWIDTH, BHEIGHT, color=(156, 45, 117))
            else:
                pygame.draw.rect(window, (255, 199, 206), (110, 140, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (110, 140, 90, 80), 1)
                button("DEL", 110, 140, BWIDTH, BHEIGHT, color=(156, 45, 117))
            if x >= 200 and x <= 290 and y >= 140 and y <= 220:
                pygame.draw.rect(window, (219, 219, 219), (200, 140, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (200, 140, 90, 80), 1)
                button("/", 200, 140, BWIDTH, BHEIGHT, color=(156, 45, 117))
            else:
                pygame.draw.rect(window, (255, 199, 206), (200, 140, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (200, 140, 90, 80), 1)
                button("/", 200, 140, BWIDTH, BHEIGHT, color=(156, 45, 117))
            if x >= 290 and x <= 380 and y >= 140 and y <= 220:
                pygame.draw.rect(window, (219, 219, 219), (290, 140, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (290, 140, 90, 80), 1)
                button("*", 290, 140, BWIDTH, BHEIGHT, color=(156, 45, 117))
            else:
                pygame.draw.rect(window, (255, 199, 206), (290, 140, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (290, 140, 90, 80), 1)
                button("*", 290, 140, BWIDTH, BHEIGHT, color=(156, 45, 117))
            # 2
            if x >= 20 and x <= 110 and y >= 220 and y <= 300:
                pygame.draw.rect(window, (219, 219, 219), (20, 220, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (20, 220, 90, 80), 1)
                button("7", 20, 220, BWIDTH, BHEIGHT, color=(0, 0, 0))
            else:
                pygame.draw.rect(window, (221, 235, 247), (20, 220, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (20, 220, 90, 80), 1)
                button("7", 20, 220, BWIDTH, BHEIGHT, color=(0, 0, 0))
            if x >= 110 and x <= 200 and y >= 220 and y <= 300:
                pygame.draw.rect(window, (219, 219, 219), (110, 220, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (110, 220, 90, 80), 1)
                button("8", 110, 220, BWIDTH, BHEIGHT, color=(0, 0, 0))
            else:
                pygame.draw.rect(window, (221, 235, 247), (110, 220, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (110, 220, 90, 80), 1)
                button("8", 110, 220, BWIDTH, BHEIGHT, color=(0, 0, 0))
            if x >= 200 and x <= 290 and y >= 220 and y <= 300:
                pygame.draw.rect(window, (219, 219, 219), (200, 220, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (200, 220, 90, 80), 1)
                button("9", 200, 220, BWIDTH, BHEIGHT, color=(0, 0, 0))
            else:
                pygame.draw.rect(window, (221, 235, 247), (200, 220, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (200, 220, 90, 80), 1)
                button("9", 200, 220, BWIDTH, BHEIGHT, color=(0, 0, 0))
            if x >= 290 and x <= 380 and y >= 220 and y <= 300:
                pygame.draw.rect(window, (219, 219, 219), (290, 220, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (290, 220, 90, 80), 1)
                button("+", 290, 220, BWIDTH, BHEIGHT, color=(0, 0, 0))
            else:
                pygame.draw.rect(window, (255, 199, 206), (290, 220, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (290, 220, 90, 80), 1)
                button("+", 290, 220, BWIDTH, BHEIGHT, color=(0, 0, 0))
            # 3
            if x >= 20 and x <= 110 and y >= 300 and y <= 380:
                pygame.draw.rect(window, (219, 219, 219), (20, 300, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (20, 300, 90, 80), 1)
                button("4", 20, 300, BWIDTH, BHEIGHT, color=(0, 0, 0))
            else:
                pygame.draw.rect(window, (221, 235, 247), (20, 300, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (20, 300, 90, 80), 1)
                button("4", 20, 300, BWIDTH, BHEIGHT, color=(0, 0, 0))
            if x >= 110 and x <= 200 and y >= 300 and y <= 380:
                pygame.draw.rect(window, (219, 219, 219), (110, 300, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (110, 300, 90, 80), 1)
                button("5", 110, 300, BWIDTH, BHEIGHT, color=(0, 0, 0))
            else:
                pygame.draw.rect(window, (221, 235, 247), (110, 300, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (110, 300, 90, 80), 1)
                button("5", 110, 300, BWIDTH, BHEIGHT, color=(0, 0, 0))
            if x >= 200 and x <= 290 and y >= 300 and y <= 380:
                pygame.draw.rect(window, (219, 219, 219), (200, 300, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (200, 300, 90, 80), 1)
                button("6", 200, 300, BWIDTH, BHEIGHT, color=(0, 0, 0))
            else:
                pygame.draw.rect(window, (221, 235, 247), (200, 300, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (200, 300, 90, 80), 1)
                button("6", 200, 300, BWIDTH, BHEIGHT, color=(0, 0, 0))
            if x >= 290 and x <= 380 and y >= 300 and y <= 380:
                pygame.draw.rect(window, (219, 219, 219), (290, 300, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (290, 300, 90, 80), 1)
                button("-", 290, 300, BWIDTH, BHEIGHT, color=(0, 0, 0))
            else:
                pygame.draw.rect(window, (255, 199, 206), (290, 300, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (290, 300, 90, 80), 1)
                button("-", 290, 300, BWIDTH, BHEIGHT, color=(0, 0, 0))
            # 4
            if x >= 20 and x <= 110 and y >= 380 and y <= 460:
                pygame.draw.rect(window, (219, 219, 219), (20, 380, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (20, 380, 90, 80), 1)
                button("1", 20, 380, BWIDTH, BHEIGHT, color=(0, 0, 0))
            else:
                pygame.draw.rect(window, (221, 235, 247), (20, 380, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (20, 380, 90, 80), 1)
                button("1", 20, 380, BWIDTH, BHEIGHT, color=(0, 0, 0))
            if x >= 110 and x <= 200 and y >= 380 and y <= 460:
                pygame.draw.rect(window, (219, 219, 219), (110, 380, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (110, 380, 90, 80), 1)
                button("2", 110, 380, BWIDTH, BHEIGHT, color=(0, 0, 0))
            else:
                pygame.draw.rect(window, (221, 235, 247), (110, 380, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (110, 380, 90, 80), 1)
                button("2", 110, 380, BWIDTH, BHEIGHT, color=(0, 0, 0))
            if x >= 200 and x <= 290 and y >= 380 and y <= 460:
                pygame.draw.rect(window, (219, 219, 219), (200, 380, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (200, 380, 90, 80), 1)
                button("3", 200, 380, BWIDTH, BHEIGHT, color=(0, 0, 0))
            else:
                pygame.draw.rect(window, (221, 235, 247), (200, 380, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (200, 380, 90, 80), 1)
                button("3", 200, 380, BWIDTH, BHEIGHT, color=(0, 0, 0))
            if x >= 290 and x <= 380 and y >= 380 and y <= 540:
                pygame.draw.rect(window, (219, 219, 219), (290, 380, 90, 160), 0)
                pygame.draw.rect(window, (60, 60, 60), (290, 380, 90, 160), 1)
                button("=", 290, 380, BWIDTH, 160, color=(0, 0, 0))
            else:
                pygame.draw.rect(window, (255, 204, 153), (290, 380, 90, 160), 0)
                pygame.draw.rect(window, (60, 60, 60), (290, 380, 90, 160), 1)
                button("=", 290, 380, BWIDTH, 160, color=(0, 0, 0))
            # 5
            if x >= 20 and x <= 200 and y >= 460 and y <= 540:
                pygame.draw.rect(window, (219, 219, 219), (20, 460, 180, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (20, 460, 180, 80), 1)
                button("0", 20, 460, 160, BHEIGHT, color=(0, 0, 0))
            else:
                pygame.draw.rect(window, (217, 225, 242), (20, 460, 180, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (20, 460, 180, 80), 1)
                button("0", 20, 460, 160, BHEIGHT, color=(0, 0, 0))
            if x >= 200 and x <= 290 and y >= 460 and y <= 540:
                pygame.draw.rect(window, (219, 219, 219), (200, 460, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (200, 460, 90, 80), 1)
                button(".", 200, 460, BWIDTH, BHEIGHT, color=(0, 0, 0))
            else:
                pygame.draw.rect(window, (255, 235, 156), (200, 460, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (200, 460, 90, 80), 1)
                button(".", 200, 460, BWIDTH, BHEIGHT, color=(0, 0, 0))
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if x >= 20 and x <= 110 and y >= 140 and y <= 220:
                pygame.draw.rect(window, (165, 165, 165), (20, 140, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (20, 140, 90, 80), 1)
                clear()
                button("C", 20, 140, BWIDTH, BHEIGHT, color=(101, 0, 49))
            else:
                pygame.draw.rect(window, (252, 228, 214), (20, 140, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (20, 140, 90, 80), 1)
                button("C", 20, 140, BWIDTH, BHEIGHT, color=(101, 0, 49))
            if x >= 110 and x <= 200 and y >= 140 and y <= 220:
                pygame.draw.rect(window, (165, 165, 165), (110, 140, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (110, 140, 90, 80), 1)
                back()
                button("DEL", 110, 140, BWIDTH, BHEIGHT, color=(156, 45, 117))
            else:
                pygame.draw.rect(window, (255, 199, 206), (110, 140, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (110, 140, 90, 80), 1)
                button("DEL", 110, 140, BWIDTH, BHEIGHT, color=(156, 45, 117))
            if x >= 200 and x <= 290 and y >= 140 and y <= 220:
                pygame.draw.rect(window, (165, 165, 165), (200, 140, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (200, 140, 90, 80), 1)
                add("/")
                button("/", 200, 140, BWIDTH, BHEIGHT, color=(156, 45, 117))
            else:
                pygame.draw.rect(window, (255, 199, 206), (200, 140, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (200, 140, 90, 80), 1)
                button("/", 200, 140, BWIDTH, BHEIGHT, color=(156, 45, 117))
            if x >= 290 and x <= 380 and y >= 140 and y <= 220:
                pygame.draw.rect(window, (165, 165, 165), (290, 140, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (290, 140, 90, 80), 1)
                add("*")
                button("*", 290, 140, BWIDTH, BHEIGHT, color=(156, 45, 117))
            else:
                pygame.draw.rect(window, (255, 199, 206), (290, 140, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (290, 140, 90, 80), 1)
                button("*", 290, 140, BWIDTH, BHEIGHT, color=(156, 45, 117))
            # 2
            if x >= 20 and x <= 110 and y >= 220 and y <= 300:
                pygame.draw.rect(window, (165, 165, 165), (20, 220, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (20, 220, 90, 80), 1)
                add("7")
                button("7", 20, 220, BWIDTH, BHEIGHT, color=(0, 0, 0))
            else:
                pygame.draw.rect(window, (221, 235, 247), (20, 220, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (20, 220, 90, 80), 1)
                button("7", 20, 220, BWIDTH, BHEIGHT, color=(0, 0, 0))
            if x >= 110 and x <= 200 and y >= 220 and y <= 300:
                pygame.draw.rect(window, (165, 165, 165), (110, 220, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (110, 220, 90, 80), 1)
                add("8")
                button("8", 110, 220, BWIDTH, BHEIGHT, color=(0, 0, 0))
            else:
                pygame.draw.rect(window, (221, 235, 247), (110, 220, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (110, 220, 90, 80), 1)
                button("8", 110, 220, BWIDTH, BHEIGHT, color=(0, 0, 0))
            if x >= 200 and x <= 290 and y >= 220 and y <= 300:
                pygame.draw.rect(window, (165, 165, 165), (200, 220, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (200, 220, 90, 80), 1)
                add("9")
                button("9", 200, 220, BWIDTH, BHEIGHT, color=(0, 0, 0))
            else:
                pygame.draw.rect(window, (221, 235, 247), (200, 220, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (200, 220, 90, 80), 1)
                button("9", 200, 220, BWIDTH, BHEIGHT, color=(0, 0, 0))
            if x >= 290 and x <= 380 and y >= 220 and y <= 300:
                pygame.draw.rect(window, (165, 165, 165), (290, 220, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (290, 220, 90, 80), 1)
                add("+")
                button("+", 290, 220, BWIDTH, BHEIGHT, color=(0, 0, 0))
            else:
                pygame.draw.rect(window, (255, 199, 206), (290, 220, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (290, 220, 90, 80), 1)
                button("+", 290, 220, BWIDTH, BHEIGHT, color=(0, 0, 0))
            # 3
            if x >= 20 and x <= 110 and y >= 300 and y <= 380:
                pygame.draw.rect(window, (165, 165, 165), (20, 300, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (20, 300, 90, 80), 1)
                add("4")
                button("4", 20, 300, BWIDTH, BHEIGHT, color=(0, 0, 0))
            else:
                pygame.draw.rect(window, (221, 235, 247), (20, 300, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (20, 300, 90, 80), 1)
                button("4", 20, 300, BWIDTH, BHEIGHT, color=(0, 0, 0))
            if x >= 110 and x <= 200 and y >= 300 and y <= 380:
                pygame.draw.rect(window, (165, 165, 165), (110, 300, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (110, 300, 90, 80), 1)
                add("5")
                button("5", 110, 300, BWIDTH, BHEIGHT, color=(0, 0, 0))
            else:
                pygame.draw.rect(window, (221, 235, 247), (110, 300, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (110, 300, 90, 80), 1)
                button("5", 110, 300, BWIDTH, BHEIGHT, color=(0, 0, 0))
            if x >= 200 and x <= 290 and y >= 300 and y <= 380:
                pygame.draw.rect(window, (165, 165, 165), (200, 300, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (200, 300, 90, 80), 1)
                add("6")
                button("6", 200, 300, BWIDTH, BHEIGHT, color=(0, 0, 0))
            else:
                pygame.draw.rect(window, (221, 235, 247), (200, 300, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (200, 300, 90, 80), 1)
                button("6", 200, 300, BWIDTH, BHEIGHT, color=(0, 0, 0))
            if x >= 290 and x <= 380 and y >= 300 and y <= 380:
                pygame.draw.rect(window, (165, 165, 165), (290, 300, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (290, 300, 90, 80), 1)
                add("-")
                button("-", 290, 300, BWIDTH, BHEIGHT, color=(0, 0, 0))
            else:
                pygame.draw.rect(window, (255, 199, 206), (290, 300, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (290, 300, 90, 80), 1)
                button("-", 290, 300, BWIDTH, BHEIGHT, color=(0, 0, 0))
            # 4
            if x >= 20 and x <= 110 and y >= 380 and y <= 460:
                pygame.draw.rect(window, (165, 165, 165), (20, 380, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (20, 380, 90, 80), 1)
                add("1")
                button("1", 20, 380, BWIDTH, BHEIGHT, color=(0, 0, 0))
            else:
                pygame.draw.rect(window, (221, 235, 247), (20, 380, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (20, 380, 90, 80), 1)
                button("1", 20, 380, BWIDTH, BHEIGHT, color=(0, 0, 0))
            if x >= 110 and x <= 200 and y >= 380 and y <= 460:
                pygame.draw.rect(window, (165, 165, 165), (110, 380, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (110, 380, 90, 80), 1)
                add("2")
                button("2", 110, 380, BWIDTH, BHEIGHT, color=(0, 0, 0))
            else:
                pygame.draw.rect(window, (221, 235, 247), (110, 380, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (110, 380, 90, 80), 1)
                button("2", 110, 380, BWIDTH, BHEIGHT, color=(0, 0, 0))
            if x >= 200 and x <= 290 and y >= 380 and y <= 460:
                pygame.draw.rect(window, (165, 165, 165), (200, 380, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (200, 380, 90, 80), 1)
                add("3")
                button("3", 200, 380, BWIDTH, BHEIGHT, color=(0, 0, 0))
            else:
                pygame.draw.rect(window, (221, 235, 247), (200, 380, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (200, 380, 90, 80), 1)
                button("3", 200, 380, BWIDTH, BHEIGHT, color=(0, 0, 0))
            if x >= 290 and x <= 380 and y >= 380 and y <= 540:
                pygame.draw.rect(window, (165, 165, 165), (290, 380, 90, 160), 0)
                pygame.draw.rect(window, (60, 60, 60), (290, 380, 90, 160), 1)
                calculate()
                button("=", 290, 380, BWIDTH, 160, color=(0, 0, 0))
            else:
                pygame.draw.rect(window, (255, 204, 153), (290, 380, 90, 160), 0)
                pygame.draw.rect(window, (60, 60, 60), (290, 380, 90, 160), 1)
                button("=", 290, 380, BWIDTH, 160, color=(0, 0, 0))
            # 5
            if x >= 20 and x <= 200 and y >= 460 and y <= 540:
                pygame.draw.rect(window, (165, 165, 165), (20, 460, 180, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (20, 460, 180, 80), 1)
                add("0")
                button("0", 20, 460, 160, BHEIGHT, color=(0, 0, 0))
            else:
                pygame.draw.rect(window, (217, 225, 242), (20, 460, 180, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (20, 460, 180, 80), 1)
                button("0", 20, 460, 160, BHEIGHT, color=(0, 0, 0))
            if x >= 200 and x <= 290 and y >= 460 and y <= 540:
                pygame.draw.rect(window, (165, 165, 165), (200, 460, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (200, 460, 90, 80), 1)
                add(".")
                button(".", 200, 460, BWIDTH, BHEIGHT, color=(0, 0, 0))
            else:
                pygame.draw.rect(window, (255, 235, 156), (200, 460, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (200, 460, 90, 80), 1)
                button(".", 200, 460, BWIDTH, BHEIGHT, color=(0, 0, 0))
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos
            if x >= 20 and x <= 110 and y >= 140 and y <= 220:
                pygame.draw.rect(window, (252, 228, 214), (20, 140, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (20, 140, 90, 80), 1)
                button("C", 20, 140, BWIDTH, BHEIGHT, color=(101, 0, 49))
            if x >= 110 and x <= 200 and y >= 140 and y <= 220:
                pygame.draw.rect(window, (255, 199, 206), (110, 140, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (110, 140, 90, 80), 1)
                button("DEL", 110, 140, BWIDTH, BHEIGHT, color=(156, 45, 117))
            if x >= 200 and x <= 290 and y >= 140 and y <= 220:
                pygame.draw.rect(window, (255, 199, 206), (200, 140, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (200, 140, 90, 80), 1)
                button("/", 200, 140, BWIDTH, BHEIGHT, color=(156, 45, 117))
            if x >= 290 and x <= 380 and y >= 140 and y <= 220:
                pygame.draw.rect(window, (255, 199, 206), (290, 140, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (290, 140, 90, 80), 1)
                button("*", 290, 140, BWIDTH, BHEIGHT, color=(156, 45, 117))
            # 2
            if x >= 20 and x <= 110 and y >= 220 and y <= 300:
                pygame.draw.rect(window, (221, 235, 247), (20, 220, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (20, 220, 90, 80), 1)
                button("7", 20, 220, BWIDTH, BHEIGHT, color=(0, 0, 0))
            if x >= 110 and x <= 200 and y >= 220 and y <= 300:
                pygame.draw.rect(window, (221, 235, 247), (110, 220, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (110, 220, 90, 80), 1)
                button("8", 110, 220, BWIDTH, BHEIGHT, color=(0, 0, 0))
            if x >= 200 and x <= 290 and y >= 220 and y <= 300:
                pygame.draw.rect(window, (221, 235, 247), (200, 220, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (200, 220, 90, 80), 1)
                button("9", 200, 220, BWIDTH, BHEIGHT, color=(0, 0, 0))
            if x >= 290 and x <= 380 and y >= 220 and y <= 300:
                pygame.draw.rect(window, (255, 199, 206), (290, 220, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (290, 220, 90, 80), 1)
                button("+", 290, 220, BWIDTH, BHEIGHT, color=(0, 0, 0))
            # 3
            if x >= 20 and x <= 110 and y >= 300 and y <= 380:
                pygame.draw.rect(window, (221, 235, 247), (20, 300, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (20, 300, 90, 80), 1)
                button("4", 20, 300, BWIDTH, BHEIGHT, color=(0, 0, 0))
            if x >= 110 and x <= 200 and y >= 300 and y <= 380:
                pygame.draw.rect(window, (221, 235, 247), (110, 300, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (110, 300, 90, 80), 1)
                button("5", 110, 300, BWIDTH, BHEIGHT, color=(0, 0, 0))
            if x >= 200 and x <= 290 and y >= 300 and y <= 380:
                pygame.draw.rect(window, (221, 235, 247), (200, 300, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (200, 300, 90, 80), 1)
                button("6", 200, 300, BWIDTH, BHEIGHT, color=(0, 0, 0))
            if x >= 290 and x <= 380 and y >= 300 and y <= 380:
                pygame.draw.rect(window, (255, 199, 206), (290, 300, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (290, 300, 90, 80), 1)
                button("-", 290, 300, BWIDTH, BHEIGHT, color=(0, 0, 0))
            # 4
            if x >= 20 and x <= 110 and y >= 380 and y <= 460:
                pygame.draw.rect(window, (221, 235, 247), (20, 380, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (20, 380, 90, 80), 1)
                button("1", 20, 380, BWIDTH, BHEIGHT, color=(0, 0, 0))
            if x >= 110 and x <= 200 and y >= 380 and y <= 460:
                pygame.draw.rect(window, (221, 235, 247), (110, 380, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (110, 380, 90, 80), 1)
                button("2", 110, 380, BWIDTH, BHEIGHT, color=(0, 0, 0))
            if x >= 200 and x <= 290 and y >= 380 and y <= 460:
                pygame.draw.rect(window, (221, 235, 247), (200, 380, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (200, 380, 90, 80), 1)
                button("3", 200, 380, BWIDTH, BHEIGHT, color=(0, 0, 0))
            if x >= 290 and x <= 380 and y >= 380 and y <= 540:
                pygame.draw.rect(window, (255, 204, 153), (290, 380, 90, 160), 0)
                pygame.draw.rect(window, (60, 60, 60), (290, 380, 90, 160), 1)
                button("=", 290, 380, BWIDTH, 160, color=(0, 0, 0))
            # 5
            if x >= 20 and x <= 200 and y >= 460 and y <= 540:
                pygame.draw.rect(window, (217, 225, 242), (20, 460, 180, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (20, 460, 180, 80), 1)
                button("0", 20, 460, 160, BHEIGHT, color=(0, 0, 0))
            if x >= 200 and x <= 290 and y >= 460 and y <= 540:
                pygame.draw.rect(window, (255, 235, 156), (200, 460, 90, 80), 0)
                pygame.draw.rect(window, (60, 60, 60), (200, 460, 90, 80), 1)
                button(".", 200, 460, BWIDTH, BHEIGHT, color=(0, 0, 0))
    pygame.display.update()

# pyinstaller -F -i 图标文件 py文件