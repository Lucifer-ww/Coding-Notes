#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: K_liu
import pygame
from pygame.locals import *
from sys import exit

pygame.init()
# Configuration file
window_size = (1280, 750)
screen = pygame.display.set_mode(window_size, 0, 32)
pygame.display.set_caption('Message Box Test')


def LoginPage():
    message_box = []  # Create a message box
    back_image = pygame.image.load('logo2.jpg').convert()
    while True:
        break_switch = False
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            screen.fill((255, 255, 255))  # background color
            screen.blit(back_image, (400, 100))
            # message box .....................................................................
            screen.set_clip(470, 300, 300, 50)  # message box's location
            screen.fill((47, 79, 79))  # message box's color
            x, y = pygame.mouse.get_pos()
            if 500 < x < 800 and 300 < y < 350:
                # print('mouse in the box')
                if event.type == KEYDOWN:
                    key_num = event.key
                    # print(key_num)
                    if key_num == 49:
                        message_box.append('1')  # get the value of keyboard
                    elif key_num == 50:
                        message_box.append('2')  # get the value of keyboard
                    elif key_num == 51:
                        message_box.append('3')  # get the value of keyboard
                    elif key_num == 52:
                        message_box.append('4')  # get the value of keyboard
                    elif key_num == 53:
                        message_box.append('5')  # get the value of keyboard
                    elif key_num == 54:
                        message_box.append('6')  # get the value of keyboard
                    elif key_num == 55:
                        message_box.append('7')  # get the value of keyboard
                    elif key_num == 56:
                        message_box.append('8')  # get the value of keyboard
                    elif key_num == 57:
                        message_box.append('9')  # get the value of keyboard
                    elif key_num == 48:
                        message_box.append('0')  # get the value of keyboard
                    elif key_num == 46:
                        message_box.append('.')  # get the value of keyboard
                    elif key_num == 8 and len(message_box) is not 0:
                        message_box.pop()  # delete the last value

            text = ''.join(message_box)  # join the list value to a string
            font_family = pygame.font.SysFont('arial', 26)  # setting the font
            IP_name = ' IP: '
            screen.blit(font_family.render(IP_name, True, (255, 255, 255)), (480, 310))
            screen.blit(font_family.render(text, True, (255, 255, 255)), (560, 310))
            # submit button ...................................................................
            screen.set_clip(470, 370, 300, 50)  # submit button's location
            screen.fill((47, 79, 79))  # submit button's color
            Login_name = 'Login'
            screen.blit(font_family.render(Login_name, True, (255, 255, 255)), (585, 380))
            if 470 < x < 770 and 370 < y < 420 and event.type == MOUSEBUTTONDOWN:
                screen.set_clip(470, 370, 300, 50)  # submit button's location
                screen.fill((84, 255, 159))  # change the submit button color
                print('you clicked the button')
                break_switch = True
        pygame.display.update()
        if break_switch:
            print('break')
            break


if __name__ == '__main__':
    LoginPage()