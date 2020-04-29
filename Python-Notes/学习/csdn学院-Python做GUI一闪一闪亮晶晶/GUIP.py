#-*-coding=utf-8-*-
import win32con
import win32gui
import time

QQ = win32gui.FindWindow("TXGuiFoundation", "QQ")
for num in range(120):
    time.sleep(1)
    if num % 2 == 0:
        win32gui.ShowWindow(QQ, win32con.SW_HIDE)
    else:
        win32gui.ShowWindow(QQ, win32con.SW_SHOW)