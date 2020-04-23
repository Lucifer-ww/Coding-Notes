#-*-coding=utf-8-*-
import win32con
import win32gui
import time
import random

QQ = win32gui.FindWindow("TXGuiFoundation", "QQ")
for num in range(1):
    time.sleep(1)
    if num % 2 == 0:
        win32gui.ShowWindow(QQ, win32con.SW_HIDE)
    else:
        win32gui.ShowWindow(QQ, win32con.SW_SHOW)

# 恶作剧2：使窗体不断的变换大小
while True:
    time.sleep(1)
    x = random.randrange(900)
    y = random.randrange(900)
    win32gui.SetWindowPos(QQ,win32con.HWND_TOPMOST,100,100,
                      x,y,win32con.SWP_SHOWWINDOW)
