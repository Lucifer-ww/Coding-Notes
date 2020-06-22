# __auth__ link#

import sys

if sys.platform != 'win32':
    print("暂未支持mac系统")
    raise EnvironmentError

if float(sys.winver) < 3.8:
    print('版本过低')
    raise EnvironmentError

import os
import base64
import random
import time
import threading
import tkinter as tk
import tkinter.font as tf
from tkinter.filedialog import askopenfile

import pywintypes
import requests
from win32.lib.win32con import (CF_UNICODETEXT, SW_SHOWMINIMIZED, SW_SHOWNORMAL, SW_SHOW, HWND_TOPMOST, SWP_SHOWWINDOW,
                                WM_PASTE,
                                WM_KEYDOWN, VK_RETURN, WM_KEYUP, KEYEVENTF_KEYUP)

import win32api
import win32gui
import win32clipboard as w

from icon import img

tmp = open("tmp.ico", "wb+")
tmp.write(base64.b64decode(img))
tmp.close()


# 删掉临时文


def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(CF_UNICODETEXT, aString)
    w.CloseClipboard()


def generate_nmsl():
    url = ['https://nmsl.shadiao.app/api.php?lang=zh_cn', 'https://nmsl.shadiao.app/api.php?level=min&lang=zh_cn']
    headers = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
    }
    url = random.choice(url)
    res = requests.get(url, headers=headers)
    res = res.content.decode('utf-8')
    return res


class BombQQ:
    def __init__(self, mode, window_title, num=1, text=None, sleep=0):
        self.window_title = window_title
        self.text = text
        self.num = num
        self.m = mode
        self.sleep = sleep

    def _action(self):
        if h := win32gui.FindWindow(0, self.window_title):
            win32gui.ShowWindow(h, SW_SHOWMINIMIZED)
            win32gui.ShowWindow(h, SW_SHOWNORMAL)
            win32gui.ShowWindow(h, SW_SHOW)
            win32gui.SetForegroundWindow(h)
            win32gui.SetWindowPos(h, HWND_TOPMOST, 300, 100, 300, 300, SWP_SHOWWINDOW)

            while self.num > 0:
                # win32gui.SetWindowPos(h, HWND_TOPMOST, 100, 100, 300, 300, SWP_SHOWWINDOW)
                win32api.SendMessage(h, WM_PASTE, 0, 0)
                time.sleep(self.sleep)
                win32api.SendMessage(h, WM_KEYDOWN, VK_RETURN, 0)
                win32api.SendMessage(h, WM_KEYUP, VK_RETURN, 0)
                self.num -= 1

        else:
            # print("未找到qq聊天窗口")

            return "未找到qq聊天窗口"

    def send(self):
        if self.m == 1:
            self._action()
        elif self.m == 2:
            for c in self.text:
                self.num = 1
                setText(c)
                self._action()
            self._action()
        elif self.m == 3:
            count = self.num
            while count > 0:
                self.num = 1
                nmsl = generate_nmsl()
                setText(nmsl)
                self._action()
                count -= 1


class BombWeChat:
    def __init__(self, mode=1, window_title="微信", num=1, text=None, sleep=0):
        self.window_title = window_title
        self.text = text
        self.num = num
        self.sleep = sleep
        self.m = mode

    def _action(self):
        if h := win32gui.FindWindow(0, self.window_title):
            win32gui.ShowWindow(h, SW_SHOWMINIMIZED)
            win32gui.ShowWindow(h, SW_SHOWNORMAL)
            win32gui.ShowWindow(h, SW_SHOW)
            win32gui.SetForegroundWindow(h)
            # win32gui.SetWindowPos(h, HWND_TOPMOST, 300, 100, 300, 300, SWP_SHOWWINDOW)
            while self.num > 0:
                # win32gui.ShowWindow(h, SW_SHOW)

                time.sleep(self.sleep / 2)
                self.ctrlV()
                time.sleep(self.sleep / 2)
                self.altS()
                self.num -= 1
        else:
            # print("未找到微信窗口")
            return "未找到微信窗口"

    def send(self):
        if self.m == 1:
            self._action()
        elif self.m == 2:
            for c in self.text:
                self.num = 1
                setText(c)
                self._action()
            self._action()
        elif self.m == 3:
            count = self.num
            while count > 0:
                self.num = 1
                nmsl = generate_nmsl()
                setText(nmsl)
                self._action()
                count -= 1

    def click(self):
        pass

    def ctrlV(self):
        win32api.keybd_event(17, 0, 0, 0)  # ctrl键位码是17
        win32api.keybd_event(86, 0, 0, 0)  # v键位码是86
        win32api.keybd_event(86, 0, KEYEVENTF_KEYUP, 0)  # 释放按键
        win32api.keybd_event(17, 0, KEYEVENTF_KEYUP, 0)

    def altS(self):
        win32api.keybd_event(18, 0, 0, 0)  # Alt键位码
        win32api.keybd_event(83, 0, 0, 0)  # s键位码
        win32api.keybd_event(18, 0, KEYEVENTF_KEYUP, 0)  # 释放按键
        win32api.keybd_event(83, 0, KEYEVENTF_KEYUP, 0)


class Alarm(object):
    # def __new__(cls, msg):
    #     if not hasattr(cls, 'instance'):
    #         cls.instance = super(Alarm, cls).__new__(cls)
    #     return cls.instance

    def __init__(self):
        # 参数初始化
        self.file_text = None
        # 初始化win tk menu
        self.win = tk.Tk()
        self.tk = tk
        self.menu = tk.Menu(self.win, tearoff=0)
        # 字体设定
        ft = tf.Font(family='黑体', size=12)
        # win设置
        self.win.title('bomb!')
        self.win.geometry("500x550")

        self.win.iconbitmap("tmp.ico")
        os.remove("tmp.ico")
        self.win.configure(background='white')
        # 说明标签
        label_desc = self.tk.Label(self.win,
                                   text="工具说明:\nQQ,Tim,微信PC版,打开单独的窗口,输入窗口名称,即可发送信息。\n"
                                        "操作说明:\n1.点击`查找窗口` 把需要的窗口复制到`目标窗口`\n"
                                        "2.设定发送次数\n"
                                        "3.设定发送模式\n"
                                        "4.点击bomb",
                                   font=ft, justify='left')

        label_desc.pack(side="top", padx=10, pady=10, fill="both")

        # 窗口列表
        text_list_frm = self.tk.Frame(self.win)
        text_list_frm.pack(side="left", padx=10, pady=5, fill="both")
        text_button = self.tk.Button(text_list_frm, text='查找窗口', command=self.get_windows_list)
        text_button.pack(side="top", padx=5, pady=5)
        text_list = self.tk.Listbox(text_list_frm, width=30, height=50)
        text_list.pack(side="top", padx=5, pady=5)
        text_list.bind("<Button-3>", lambda x: self.rightKey(x, text_list))
        self.text_list = text_list

        # 选择qq或微信
        select_frm = self.tk.Frame(self.win)
        select_frm.pack(side="top", padx=10, pady=5, fill="both")
        self.select = self.tk.IntVar()
        self.select.set(1)
        s1 = self.tk.Radiobutton(select_frm, text="QQ", value=1, variable=self.select)
        s2 = self.tk.Radiobutton(select_frm, text="微信", value=2, variable=self.select)

        s1.pack(side="left", padx=5, pady=0)
        s2.pack(side="left", padx=5, pady=0)

        # 目标窗口
        target_window_frm = self.tk.Frame(self.win)
        target_window_frm.pack(side="top", padx=10, pady=5, fill="both")
        target_label = self.tk.Label(target_window_frm, text="目标窗口")
        target_label.pack(side="left", padx=10, pady=5)
        target_entry = self.tk.Entry(target_window_frm, width=20)
        target_entry.pack(side="left", padx=10, pady=5)
        target_entry.bind("<Button-3>", lambda x: self.rightKey(x, target_entry))
        self.target_entry = target_entry
        # 发送次数
        nums_frm = self.tk.Frame(self.win)
        nums_frm.pack(side="top", padx=10, pady=5, fill="both")
        nums_label = self.tk.Label(nums_frm, text="发送次数")
        nums_label.pack(side="left", padx=10, pady=5)
        nums_entry = self.tk.Entry(nums_frm, width=20)
        nums_entry.pack(side="left", padx=10, pady=5)
        self.nums_entry = nums_entry

        # 发送间隔
        time_frm = self.tk.Frame(self.win)
        time_frm.pack(side="top", padx=10, pady=5, fill="both")
        time_label = self.tk.Label(time_frm, text="发送时间间隔(秒)")
        time_label.pack(side="left", padx=10, pady=5)
        time_scale = self.tk.Scale(time_frm, from_=0, to=10, orient='horizontal')
        time_scale.pack(side="left", padx=10, pady=5)
        self.time_scale = time_scale
        # 模式选择框
        mode_frm = self.tk.Frame(self.win)
        mode_frm.pack(side="top", padx=10, pady=5, fill="both")
        self.v = self.tk.IntVar()
        self.v.set(1)
        r1 = self.tk.Radiobutton(mode_frm, text="模式一:发送剪贴板内容", value=1, variable=self.v, command=self.mode)
        r2 = self.tk.Radiobutton(mode_frm, text="模式二:发送文件内容", value=2, variable=self.v, command=self.mode)
        r3 = self.tk.Radiobutton(mode_frm, text="模式三:自动祖安模式", value=3, variable=self.v, command=self.mode)
        r1.pack(side="top", padx=5, pady=0)
        r2.pack(side="top", padx=5, pady=0)
        r3.pack(side="top", padx=5, pady=0)

        # 显示剪贴板内容
        clipboard_frm = self.tk.Frame(self.win)
        clipboard_frm.pack(side="top", padx=10, pady=5, fill="both")
        clipboard_label = self.tk.Label(clipboard_frm, text="当前剪贴板内容为")
        clipboard_label.pack(side="top", padx=10, pady=0)
        clipboard_list = self.tk.Text(clipboard_frm, width=32, height=3)
        clipboard_list.pack(side="left", padx=10, pady=5)
        self.clipboard_frm = clipboard_frm
        self.clipboard_list = clipboard_list
        # 打开文件内容
        file_frm = self.tk.Frame(self.win)
        file_frm.pack(side="top", padx=10, pady=5, fill="both")
        file_button = self.tk.Button(file_frm, text='打开文件', command=self.read_file)
        file_button.pack(side="left", padx=10, pady=5)
        file_label = self.tk.Label(file_frm, text="")
        file_label.pack(side="left", padx=10, pady=5)
        self.file_frm = file_frm
        self.file_label = file_label

        # bomb
        bomb_frm = self.tk.Frame(self.win)
        bomb_frm.pack(side="bottom", padx=10, pady=5, fill="both")
        bomb_button = self.tk.Button(bomb_frm, text='bomb', command=self.start_bomb)
        bomb_button.pack(side="top", padx=10, pady=5)
        self.mode()
        self.start_thread()
        self.win.mainloop()

    def start_bomb(self):
        mode = self.v.get()
        target_window = self.target_entry.get()
        nums = self.nums_entry.get()
        sleep = self.time_scale.get()
        content = self.file_text
        s = self.select.get()
        if s == 1:
            qq = BombWeChat(mode=mode, num=int(nums) if nums else 0, text=content, window_title=target_window,
                            sleep=sleep)
            t = threading.Thread(target=qq.send, daemon=True)
            t.start()

        if s == 2:
            chat = BombWeChat(mode=mode, num=int(nums) if nums else 0, text=content, window_title=target_window,
                              sleep=sleep)
            t = threading.Thread(target=chat.send, daemon=True)
            t.start()

    def mode(self):
        v = self.v.get()
        if v == 1:
            self.file_frm.pack_forget()
            self.clipboard_frm.pack(side="top", padx=10, pady=5, fill="both")
            self.nums_entry.pack(side="left", padx=10, pady=5)
        if v == 2:
            self.file_frm.pack(side="top", padx=10, pady=5, fill="both")
            self.clipboard_frm.pack_forget()
            self.nums_entry.pack_forget()
        if v == 3:
            self.file_frm.pack_forget()
            self.clipboard_frm.pack_forget()
            self.nums_entry.pack(side="left", padx=10, pady=5)

    def read_file(self):
        with askopenfile(title="读取文件", initialdir="d:", filetypes=[("文本文件", ".txt")]) as f:
            try:
                content = f.readlines()
                self.file_text = [c.replace("\n", "") for c in content]

                self.file_label.config(text="读取成功")

            except Exception as e:

                self.file_label.config(text="读取失败")

    def get_windows_list(self):
        hwnd_title = dict()

        def get_all_hwnd(hwnd, mouse):
            if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
                hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})

        win32gui.EnumWindows(get_all_hwnd, 0)
        self.text_list.delete(0, 'end')
        for h, t in hwnd_title.items():
            if t != "":
                self.text_list.insert('end', t)

    def rightKey(self, event, editor):
        def cut(editor, event=None):
            editor.event_generate("<<Cut>>")

        def copy(editor, f, event=None):
            editor.event_generate("<<Copy>>")
            text = f.clipboard_list.clipboard_get()
            f.target_entry.delete(0, 'end')
            f.target_entry.insert('end', text)

        def paste(editor, event=None):
            editor.event_generate("<<Paste>>")

        self.menu.delete(0, self.tk.END)
        # self.menu.add_command(label='剪切', command=lambda: cut(editor))
        self.menu.add_command(label='复制', command=lambda: copy(editor, self))
        self.menu.add_command(label='粘贴', command=lambda: paste(editor))
        self.menu.post(event.x_root, event.y_root)

    def get_clipboard_data(self):
        active = ""
        while True:
            w.OpenClipboard()
            try:
                text = w.GetClipboardData()
                if text == "":
                    text = "图片或文件"
            except:
                text = "图片或文件"
            w.CloseClipboard()
            # print("out active", active)
            # print(active != text)
            if active != text:
                self.clipboard_list.delete('1.0', 'end')
                self.clipboard_list.insert('end', str(text))
                active = text
                # print("in",active)
            # except:
            #     pass

            time.sleep(2)

    def start_thread(self):
        th = threading.Thread(target=self.get_clipboard_data, daemon=True)
        th.start()


if __name__ == '__main__':
    a = Alarm()
    # qq = BombWeChat(mode=1, num=int(2), text="sss", window_title="戲說", sleep=1)
    # qq.send()
    # chat = BombWeChat(mode=1, num=int(2), text="sss", window_title="微信", sleep=1)
    # chat.send()
