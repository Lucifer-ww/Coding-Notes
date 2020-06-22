import pygame
import sys
import traceback
from pygame.locals import *
import myplane
import enemy
import bullet
import supply
from random import *
##############
import tkinter as tk
import tkinter.messagebox
import pickle
pygame.init()
bg_size = width, height = 1000, 700
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("飞机大战---星空")

background = pygame.image.load("images/background.png").convert()

BLACK = (0,0,0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255,255,255)
#时间模块
clock = pygame.time.Clock()

#载入游戏音乐
pygame.mixer.music.load("sound/game_music.wave")
pygame.mixer.music.set_volume(0.2)
bullet_sound = pygame.mixer.Sound("sound/bullet.wav")
bullet_sound.set_volume(0.2)
bomb_sound = pygame.mixer.Sound("sound/use_bomb.wav")
bomb_sound.set_volume(0.2)
supply_sound = pygame.mixer.Sound("sound/supply.wav")
supply_sound.set_volume(0.2)
get_bomb_sound = pygame.mixer.Sound("sound/get_bomb.wav")
get_bomb_sound.set_volume(0.2)
get_bullet_sound = pygame.mixer.Sound("sound/get_bullet.wav")
get_bullet_sound.set_volume(0.2)
upgrade_sound = pygame.mixer.Sound("sound/upgrade.wav")
upgrade_sound.set_volume(0.2)
enemy3_fly_sound = pygame.mixer.Sound("sound/enemy3_flying.wav")
enemy3_fly_sound.set_volume(0.2)
enemy1_down_sound = pygame.mixer.Sound("sound/enemy1_down.wav")
enemy1_down_sound.set_volume(0.2)
enemy2_down_sound = pygame.mixer.Sound("sound/enemy2_down.wav")
enemy2_down_sound.set_volume(0.2)
enemy3_down_sound = pygame.mixer.Sound("sound/enemy3_down.wav")
enemy3_down_sound.set_volume(0.5)
me_down_sound = pygame.mixer.Sound("sound/me_down.wav")
me_down_sound.set_volume(0.2)

######################################################################################
menu_sound = pygame.mixer.Sound("sound/mune.wav")#选择菜单时的音效
menu_sound.set_volume(0.2)


# "关于"界面
def About():
    # 娱乐图片
    about_fun_img = pygame.image.load("images/about_fun.JPG")
    about_fun_rect = about_fun_img.get_rect()
    # 娱乐图片
    about_fun2_img = pygame.image.load("images/about_fun2.png")
    about_fun2_rect = about_fun2_img.get_rect()

    # 返回按钮
    comeback1_img = pygame.image.load("images/comeback1.png").convert_alpha()  # 返回按钮
    comeback2_img = pygame.image.load("images/comeback2.png").convert_alpha()
    comeback_img = comeback1_img  # 设置默认图片
    comeback_rect = comeback1_img.get_rect()
    comeback_rect.left, comeback_rect.top = 1000 - 100, 700 - 100

    about_font = pygame.font.Font("font/font.TTF", 35)
    Author_text = about_font.render("Author: HuangJiahuan", True, WHITE)
    Email_text = about_font.render("E-mail: 1776833181@163.com", True, WHITE)
    Language_text = about_font.render("Language: Python", True, WHITE)
    Bgm_text = about_font.render("Bgm: 《Into The Battlefield》", True, WHITE)
    # This book is for academic exchanges and research learning, Do not used for commercial purposes.
    Attention1_text = about_font.render("Attention: This game is for academic exchanges ", True, WHITE)
    Attention2_text = about_font.render("and research learning. Please do not", True, WHITE)
    Attention3_text = about_font.render("used for commercial purposes.", True, WHITE)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEMOTION:
                # 返回按钮
                if comeback_rect.collidepoint(event.pos):
                    comeback_img = comeback1_img
                else:
                    comeback_img = comeback2_img

            elif event.type == MOUSEBUTTONDOWN:
                # collidepoint(event.pos),自动检测鼠标是否停留在pos内，如果是则返回True
                if event.button == 1 and comeback_rect.collidepoint(event.pos):
                    menu_sound.play()
                    Menu()

        screen.blit(background, (0, 0))
        screen.blit(about_fun2_img, about_fun2_rect)
        screen.blit(comeback_img, comeback_rect)
        screen.blit(Author_text, (10, 90))
        screen.blit(Email_text, (10, 140))
        screen.blit(Language_text, (10, 190))
        screen.blit(Bgm_text, (10, 240))
        screen.blit(Attention1_text, (10, 290))
        screen.blit(Attention2_text, (205, 340))
        screen.blit(Attention3_text, (205, 390))
        screen.blit(about_fun_img, (0, 700 - about_fun_rect.height))

        pygame.display.flip()

        clock.tick(60)


# 帮助界面
def Help():
    # 背景图片
    help_fun_img = pygame.image.load("images/help_fun.jpg")
    help_fun_rect = help_fun_img.get_rect()
    # 返回按钮
    comeback1_img = pygame.image.load("images/comeback1.png").convert_alpha()  # 返回按钮
    comeback2_img = pygame.image.load("images/comeback2.png").convert_alpha()
    comeback_img = comeback1_img  # 设置默认图片
    comeback_rect = comeback1_img.get_rect()
    comeback_rect.left, comeback_rect.top = 1000 - 100, 700 - 100

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEMOTION:
                # 返回按钮
                if comeback_rect.collidepoint(event.pos):
                    comeback_img = comeback1_img
                else:
                    comeback_img = comeback2_img

            elif event.type == MOUSEBUTTONDOWN:
                # collidepoint(event.pos),自动检测鼠标是否停留在pos内，如果是则返回True
                if event.button == 1 and comeback_rect.collidepoint(event.pos):
                    menu_sound.play()
                    Menu()

        screen.blit(background, (0, 0))
        screen.blit(help_fun_img, (0, 0))
        screen.blit(comeback_img, comeback_rect)

        pygame.display.flip()

        clock.tick(60)


# 菜单界面
def Menu():
    # 娱乐图片1
    menu_fan_img = pygame.image.load("images/menu_fun.png").convert_alpha()  # 娱乐图片
    menu_fan_rect = menu_fan_img.get_rect()
    menu_fan_rect.left, menu_fan_rect.top = 0, 0
    # 娱乐图片2
    menu_fan2_img = pygame.image.load("images/menu_fun2.png").convert_alpha()  # 娱乐图片
    menu_fan2_rect = menu_fan2_img.get_rect()
    menu_fan2_rect.left, menu_fan2_rect.top = 1000 - menu_fan2_rect.width, 0

    # 开始游戏按钮
    begin_game1_img = pygame.image.load("images/begin_game1.png").convert_alpha()  # 开始游戏按钮
    begin_game2_img = pygame.image.load("images/begin_game2.png").convert_alpha()
    begin_game_img = begin_game1_img
    begin_game_rect = begin_game1_img.get_rect()
    begin_game_rect.left, begin_game_rect.top = 264 + 350, 486 - 200

    # 帮助按钮
    help1_img = pygame.image.load("images/help1.png").convert_alpha()  # 帮助按钮
    help2_img = pygame.image.load("images/help2.png").convert_alpha()
    help_img = help1_img
    help_rect = help1_img.get_rect()
    help_rect.left, help_rect.top = 264 + 350, 424 + 0

    # 关于按钮
    about1_img = pygame.image.load("images/about1.png").convert_alpha()  # 关于按钮
    about2_img = pygame.image.load("images/about2.png").convert_alpha()
    about_img = about1_img
    about_rect = about1_img.get_rect()
    about_rect.left, about_rect.top = 264 + 350, 424 + 150

    # 鼠标解除按钮音效
    is_sound = True

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # 检测鼠标是否移动到暂停游戏按钮
            elif event.type == MOUSEMOTION:
                # 开始游戏按钮
                if begin_game_rect.collidepoint(event.pos):
                    begin_game_img = begin_game2_img
                else:
                    begin_game_img = begin_game1_img
                # 帮助按钮
                if help_rect.collidepoint(event.pos):
                    help_img = help1_img
                else:
                    help_img = help2_img
                # 关于按钮
                if about_rect.collidepoint(event.pos):
                    about_img = about1_img
                else:
                    about_img = about2_img

            elif event.type == MOUSEBUTTONDOWN:
                # collidepoint(event.pos),自动检测鼠标是否停留在pos内，如果是则返回True
                if event.button == 1 and about_rect.collidepoint(event.pos):
                    menu_sound.play()
                    About()
                elif event.button == 1 and begin_game_rect.collidepoint(event.pos):
                    menu_sound.play()
                    main()
                elif event.button == 1 and help_rect.collidepoint(event.pos):
                    menu_sound.play()
                    Help()

        screen.blit(background, (0, 0))
        screen.blit(menu_fan2_img, menu_fan2_rect)
        screen.blit(menu_fan_img, (0, 0))
        screen.blit(begin_game_img, begin_game_rect)
        screen.blit(help_img, help_rect)
        screen.blit(about_img, about_rect)

        pygame.display.flip()

        clock.tick(60)
#####################################################################################

def add_small_enemies(group1, group2, num):
    for i in range(num):
        e1 = enemy.SmallEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)

def add_mid_enemies(group1, group2, num):
    for i in range(num):
        e1 = enemy.MidEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)

def add_big_enemies(group1, group2, num):
    for i in range(num):
        e1 = enemy.BigEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)

def inc_speed(target, inc):
    for each in target:
        each.speed += inc

def main():
    pygame.mixer.music.play(-1)
    
    clock = pygame.time.Clock()

    # 中弹图片索引
    e1_destroy_index = 0
    e2_destroy_index = 0
    e3_destroy_index = 0
    me_destroy_index = 0

    me = myplane.MyPlane(bg_size)
    
    enemies = pygame.sprite.Group()

    # 生成敌方小型飞机
    small_enemies = pygame.sprite.Group()
    add_small_enemies(small_enemies, enemies, 15)

    mid_enemies = pygame.sprite.Group()
    add_mid_enemies(mid_enemies, enemies, 5)

    big_enemies = pygame.sprite.Group()
    add_big_enemies(big_enemies, enemies, 1)

    running = True
    switch_image = True
    delay = 100
    score = 0
    score_font = pygame.font.Font("font/font.ttf", 36)
    
    bullets = []

    # 生成普通子弹
    bullet1 = []
    bullet1_index = 0
    BULLET1_NUM = 4
    for i in range(BULLET1_NUM):
        bullet1.append(bullet.Bullet1(me.rect.midtop))

    # 生命数量
    life_image = pygame.image.load("images/life.png").convert_alpha()
    life_rect = life_image.get_rect()
    life_num = 3

    # 游戏结束画面
    gameover_font = pygame.font.Font("font/font.ttf", 48)
    again_image = pygame.image.load("images/again.png").convert_alpha()
    again_rect = again_image.get_rect()
    gameover_image = pygame.image.load("images/gameover.png").convert_alpha()
    gameover_rect = gameover_image.get_rect()

    DOUBLE_BULLET_TIME = USEREVENT + 1

    # 解除我方飞机无敌状态
    INVINCEBLE_TIME = USEREVENT + 2


    # 生成超级子弹
    bullet2 = []
    bullet2_index = 0
    BULLET2_NUM = 8
    for i in range(BULLET2_NUM//2):
        bullet2.append(bullet.Bullet2((me.rect.centerx - 33, me.rect.centery)))
        bullet2.append(bullet.Bullet2((me.rect.centerx + 30, me.rect.centery)))

    # 标记是否使用超级子弹
    is_double_bullet = False

    level = 1

    # 全屏炸弹
    bomb_image = pygame.image.load("images/bomb.png").convert_alpha()
    bomb_rect = bomb_image.get_rect()
    bomb_font = pygame.font.Font("font/font.ttf", 48)
    bomb_num = 3

    # 每30秒发放一个补给包
    bullet_supply = supply.Bullet_Supply(bg_size)
    bomb_supply = supply.Bomb_Supply(bg_size)
    SUPPLY_TIME = USEREVENT
    pygame.time.set_timer(SUPPLY_TIME, 30 *1000)

    # 阻止重复读取成绩记录文件
    recorded = False

    # 标志是否暂停游戏
    paused = False
    #######################
    stopping_img = pygame.image.load("images/stopping.png").convert_alpha()
    stopping_rect = stopping_img.get_rect()
    stopping_rect.left, stopping_rect.top = width / 2 - stopping_rect.width / 2, height / 2 - stopping_rect.height / 2
    #########################
    paused_nor_image = pygame.image.load("images/pause_nor.png").convert_alpha()
    pause_pressed_image = pygame.image.load("images/pause_pressed.png").convert_alpha()
    resume_nor_image = pygame.image.load("images/resume_nor.png").convert_alpha()
    resume_pressed_image = pygame.image.load("images/resume_pressed.png").convert_alpha()
    paused_rect = paused_nor_image.get_rect()
    paused_rect.left, paused_rect.top = width - paused_rect.width -10, 10
    paused_image = paused_nor_image
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and paused_rect.collidepoint(event.pos):
                    paused = not paused
                    if paused:
                        pygame.time.set_timer(SUPPLY_TIME, 0)
                        pygame.mixer.music.pause()
                        pygame.mixer.pause()
                        paused_image = resume_pressed_image
                    else:
                        pygame.time.set_timer(SUPPLY_TIME, 30 * 1000)
                        pygame.mixer.music.unpause()
                        pygame.mixer.unpause()
                        paused_image = pause_pressed_image
            elif event.type == MOUSEMOTION:
                if paused_rect.collidepoint(event.pos):
                    if paused:
                        paused_image = resume_pressed_image
                    else:
                        paused_image = pause_pressed_image
                else:
                    if paused:
                        paused_image = resume_nor_image
                    else:
                        paused_image = paused_nor_image
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if bomb_num:
                        bomb_num -= 1
                        bomb_sound.play()
                        for each in enemies:
                            if each.rect.bottom > 0:
                                each.active = False
            elif event.type == SUPPLY_TIME:
                supply_sound.play()
                if choice([True, False]):
                    bomb_supply.reset()
                else:
                    bullet_supply.reset()
            elif event.type == DOUBLE_BULLET_TIME:
                is_double_bullet = False
                pygame.time.set_timer(DOUBLE_BULLET_TIME, 0)
            elif event.type == INVINCEBLE_TIME:
                me.invincible = False
                pygame.time.set_timer(INVINCEBLE_TIME, 0)


        # 根据用户的得分增加难度
        if level == 1 and score > 30000:
            level = 2
            upgrade_sound.play()
            add_small_enemies(small_enemies, enemies, 3)
            add_mid_enemies(mid_enemies, enemies, 2)
            add_big_enemies(big_enemies, enemies, 1)
            inc_speed(small_enemies, 1)
        elif level == 2 and score > 100000:
            level = 3
            upgrade_sound.play()

            add_small_enemies(small_enemies, enemies, 5)
            add_mid_enemies(mid_enemies, enemies, 3)
            add_big_enemies(big_enemies, enemies, 2)
            inc_speed(small_enemies, 1)
            inc_speed(mid_enemies, 1)
        elif level == 3 and score > 500000:
            level = 4
            upgrade_sound.play()
            add_small_enemies(small_enemies, enemies, 5)
            add_mid_enemies(mid_enemies, enemies, 3)
            add_big_enemies(big_enemies, enemies, 2)
            inc_speed(small_enemies, 1)
            inc_speed(mid_enemies, 1)
        elif level == 4 and score > 1000000:
            level = 5
            upgrade_sound.play()
            add_small_enemies(small_enemies, enemies, 5)
            add_mid_enemies(mid_enemies, enemies, 3)
            add_big_enemies(big_enemies, enemies, 2)
            inc_speed(small_enemies, 1)
            inc_speed(mid_enemies, 1)

        screen.blit(background, (0,0))
        if life_num and not paused:
            # 绘制全屏炸弹补给并检测是否获得
            if bomb_supply.active:
                bomb_supply.move()
                screen.blit(bomb_supply.image, bomb_supply.rect)
                if pygame.sprite.collide_mask(bomb_supply, me):
                    get_bomb_sound.play()
                    if bomb_num < 3:
                        bomb_num += 1
                    bomb_supply.active = False

            #发射子弹
            if not(delay % 10):
                bullet_sound.play()
                if is_double_bullet:
                    bullets = bullet2
                    bullets[bullet2_index].reset((me.rect.centerx - 33, me.rect.centery))
                    bullets[bullet2_index + 1].reset((me.rect.centerx + 33, me.rect.centery))
                    bullet2_index = (bullet2_index + 2) % BULLET2_NUM
                else:
                    bullets = bullet1
                    bullets[bullet1_index].reset(me.rect.midtop)
                    bullet1_index = (bullet1_index + 1) % BULLET1_NUM
            #检测子弹是否击中敌机
            for b in bullets:
                if b.active:
                    b.move()
                    screen.blit(b.image, b.rect)
                    enemy_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                    if enemy_hit:
                        b.active = False
                        for e in enemy_hit:
                            if e in mid_enemies or e in big_enemies:
                                e.hit = True
                                e.energy -= 1
                                if e.energy == 0:
                                    e.active = False
                            else:
                                e.active = False
            
            # 绘制全屏炸弹补给并检测是否获得
            if bullet_supply.active:
                bullet_supply.move()
                screen.blit(bullet_supply.image, bullet_supply.rect)
                if pygame.sprite.collide_mask(bullet_supply, me):
                    get_bullet_sound.play()
                    is_double_bullet = True
                    pygame.time.set_timer(DOUBLE_BULLET_TIME, 18 * 1000)
                    bullet_supply.active = False

            # 绘制大型敌机
            for each in big_enemies:
                if each.active:
                    each.move()
                    if each.hit:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    else:
                        if switch_image:
                            screen.blit(each.image1, each.rect)
                        else:
                            screen.blit(each.image2, each.rect)
                    if each.rect.bottom == -50:
                        enemy3_fly_sound.play(-1)

                    # 绘制血槽
                    pygame.draw.line(screen, BLACK, \
                            (each.rect.left, each.rect.top - 5),\
                            (each.rect.right, each.rect.top - 5), \
                            2)
                    
                    energy_remain = each.energy / enemy.BigEnemy.energy
                    if energy_remain > 0.2:
                        energy_color = GREEN
                    else:
                        energy_color = RED
                    pygame.draw.line(screen, energy_color, \
                            (each.rect.left, each.rect.top -5), \
                            (each.rect.left + each.rect.width * energy_remain, \
                            each.rect.top - 5), \
                            2)

                else:
                    if not(delay % 3):
                        if e3_destroy_index == 0:
                            enemy3_down_sound.play()
                        screen.blit(each.destroy_images[e3_destroy_index], each.rect)
                        e3_destroy_index = (e3_destroy_index+1)%6
                        if e3_destroy_index == 0:
                            me_down_sound.stop()
                            score += 10000
                            each.reset()

            # 绘制中型敌机
            for each in mid_enemies:
                if each.active:
                    each.move()

                    if each.hit:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    else:
                        screen.blit(each.image1, each.rect)

                    # 绘制血槽
                    pygame.draw.line(screen, BLACK, \
                            (each.rect.left, each.rect.top - 5),\
                            (each.rect.right, each.rect.top - 5), \
                            2)
                    
                    energy_remain = each.energy / enemy.MidEnemy.energy
                    if energy_remain > 0.2:
                        energy_color = GREEN
                    else:
                        energy_color = RED
                    pygame.draw.line(screen, energy_color, \
                            (each.rect.left, each.rect.top -5), \
                            (each.rect.left + each.rect.width * energy_remain, \
                            each.rect.top - 5), \
                            2)
                else:
                    if not(delay % 3):
                        if e2_destroy_index ==0:
                            enemy2_down_sound.play()
                        screen.blit(each.destroy_images[e2_destroy_index], each.rect)
                        e2_destroy_index = (e2_destroy_index+1)%4
                        if e2_destroy_index == 0:
                            score += 5000
                            each.reset()

            # 绘制小型敌机
            for each in small_enemies:
                if each.active:
                    each.move()
                    screen.blit(each.image1, each.rect)
                else:
                    if not(delay % 3):
                        if e1_destroy_index ==0:
                            enemy1_down_sound.play()
                        screen.blit(each.destroy_images[e1_destroy_index], each.rect)
                        e1_destroy_index = (e1_destroy_index+1)%4
                        if e1_destroy_index == 0:
                            score += 1000
                            each.reset()


            key_pressed = pygame.key.get_pressed()
            if key_pressed[K_w] or key_pressed[K_UP]:
                me.moveUp()
            if key_pressed[K_s] or key_pressed[K_DOWN]:
                me.moveDown()
            if key_pressed[K_a] or key_pressed[K_LEFT]:
                me.moveLeft()
            if key_pressed[K_d] or key_pressed[K_RIGHT]:
                me.moveRight()

            # 检测我方飞机是否被撞
            enemies_down = pygame.sprite.spritecollide(me, enemies, False, pygame.sprite.collide_mask)
            if enemies_down and not me.invincible:
                me.active = False
                for e in enemies_down:
                    e.active = False

            # 绘制我方飞机
            if me.active:
                if switch_image:
                    screen.blit(me.image1, me.rect)
                else:
                    screen.blit(me.image2, me.rect)
            else:
                me_down_sound.play()
                if not(delay % 3):
                    screen.blit(each.destroy_images[me_destroy_index], each.rect)
                    me_destroy_index = (me_destroy_index+1)%4
                    # 剩余生命数量
                    if me_destroy_index == 0:
                        life_num -= 1
                        me.reset()
                        pygame.time.set_timer(INVINCEBLE_TIME, 3 * 1000)

             # 绘制剩余炸弹数量
            bomb_text = bomb_font.render("x %d" % bomb_num, True, WHITE)
            text_rect = bomb_text.get_rect()
            screen.blit(bomb_image, (10, height-10 - bomb_rect.height))
            screen.blit(bomb_text, (20 + bomb_rect.width, height - 5 - text_rect.height))


            if life_num:
                for i in range(life_num):
                    screen.blit(life_image,\
                        (width - 10 - (i+1)*life_rect.width, \
                        height - 10 - life_rect.height))
            
            score_text = score_font.render(str("Score: %s" % score), True, WHITE)
            screen.blit(score_text, (10,5))
        elif life_num == 0:
            pygame.mixer.music.stop()
            pygame.mixer.stop()

            # 停止发放补给
            pygame.time.set_timer(SUPPLY_TIME, 0)

            if not recorded:
                recorded = True
                # 读取历史最高分
                #################################################
                #################################################
                with open("record.txt", "r") as f:
                    record_score = int(f.read())
                with open("recordname.txt", "r") as f:
                    record_name=str(f.read())
                if score > record_score:
                    with open("record.txt", "w") as f:
                        f.write(str(score))
                    with open("records.txt", "r") as f:
                        record_bestname=str(f.read())
                    with open("recordname.txt", "w") as f:
                        f.write(str(record_bestname))
            # 绘制结束画面
            record_score_text = score_font.render("Best: %d User_Name:%s" % (record_score,record_name),True,WHITE)
            screen.blit(record_score_text, (50,50))
            
            gameover_text1 = gameover_font.render("Your Score: ", True, WHITE)
            gameover_text1_rect = gameover_text1.get_rect()
            gameover_text1_rect.left, gameover_text1_rect.top = \
                                (width - gameover_text1_rect.width) // 2, height // 2
            screen.blit(gameover_text1, gameover_text1_rect)

            
            gameover_text2 = gameover_font.render(str(score), True, WHITE)
            gameover_text2_rect = gameover_text2.get_rect()
            gameover_text2_rect.left, gameover_text2_rect.top = \
                                (width - gameover_text2_rect.width) // 2, \
                                gameover_text1_rect.bottom + 10
            screen.blit(gameover_text2, gameover_text2_rect)

            again_rect.left, again_rect.top = \
                        (width - again_rect.width) // 2,\
                        gameover_text2_rect.bottom + 50
            screen.blit(again_image, again_rect)

            gameover_rect.left, gameover_rect.top = \
                        (width - again_rect.width) // 2, \
                        again_rect.bottom + 10
            screen.blit(gameover_image, gameover_rect)

            # 检测用户的鼠标操作
            # 如果用户按下鼠标左键
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if again_rect.left < pos[0] < again_rect.right and \
                   again_rect.top < pos[1] < again_rect.bottom:
                    main()
                elif gameover_rect.left < pos[0] < gameover_rect.right and \
                     gameover_rect.top < pos[1] < gameover_rect.bottom:
                     pygame.quit()
                     sys.exit()

        screen.blit(paused_image, paused_rect)

        # 切换图片
        if not(delay % 5):
            switch_image = not switch_image

        delay -= 1
        if not delay:
            delay = 100

        pygame.display.flip()
        clock.tick(60)
######################
window = tk.Tk()
window.title('欢迎来到飞机大战')
window.geometry('450x300')
 #创建一个200X500的画布
canvas =  tk.Canvas(window,height = 300,width = 500)
#logo的路径
image_file = tk.PhotoImage(file = 'images/window.png')
#什么位置插入logo图片
image = canvas.create_image(0,0,anchor = 'nw',image = image_file)
canvas.pack(side = 'top')
tk.Label(window,text='用户名:').place(x=100,y=150)
tk.Label(window,text='密码:').place(x=100,y=190)
#用户名输入框
var_usr_name=tk.StringVar()
entry_usr_name=tk.Entry(window,textvariable=var_usr_name)
entry_usr_name.place(x=160,y=150)
#密码输入框
var_usr_pwd=tk.StringVar()
entry_usr_pwd=tk.Entry(window,textvariable=var_usr_pwd,show='*')
entry_usr_pwd.place(x=160,y=190)


# 登录函数
def usr_log_in():
    # 输入框获取用户名密码
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    # 从本地字典获取用户信息，如果没有则新建本地数据库
    try:
        with open('usr_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usr_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usr_file)
    # 判断用户名和密码是否匹配
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name] and __name__ == "__main__":
            tk.messagebox.showinfo(title='welcome',
                                   message='欢迎您：' + usr_name)
            with open("records.txt", "w") as f:
                f.write(str(usr_name))
            window.destroy()
            try:
                Menu()
            except SystemExit:
                pass
            except:
                traceback.print_exc()
                pygame.quit()
                input()
            window.destroy()
        else:
            tk.messagebox.showerror(message='密码错误')
    # 用户名密码不能为空
    elif usr_name == '' or usr_pwd == '':
        tk.messagebox.showerror(message='用户名或密码为空')
    # 不在数据库中弹出是否注册的框
    else:
        is_signup = tk.messagebox.askyesno('欢迎', '您还没有注册，是否现在注册')
        if is_signup:
            usr_sign_up()


# 注册函数
def usr_sign_up():
    # 确认注册时的相应函数
    def signtowcg():
        # 获取输入框内的内容
        nn = new_name.get()
        np = new_pwd.get()
        npf = new_pwd_confirm.get()

        # 本地加载已有用户信息,如果没有则已有用户信息为空
        try:
            with open('usr_info.pickle', 'rb') as usr_file:
                exist_usr_info = pickle.load(usr_file)
        except FileNotFoundError:
            exist_usr_info = {}

            # 检查用户名存在、密码为空、密码前后不一致
        if nn in exist_usr_info:
            tk.messagebox.showerror('错误', '用户名已存在')
        elif np == '' or nn == '':
            tk.messagebox.showerror('错误', '用户名或密码为空')
        elif np != npf:
            tk.messagebox.showerror('错误', '密码前后不一致')
        # 注册信息没有问题则将用户名密码写入数据库
        else:
            exist_usr_info[nn] = np
            with open('usr_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tk.messagebox.showinfo('欢迎', '注册成功')
            # 注册成功关闭注册框
            window_sign_up.destroy()

    # 新建注册界面
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('注册')
    # 用户名变量及标签、输入框
    new_name = tk.StringVar()
    tk.Label(window_sign_up, text='用户名：').place(x=10, y=10)
    tk.Entry(window_sign_up, textvariable=new_name).place(x=150, y=10)
    # 密码变量及标签、输入框
    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='请输入密码：').place(x=10, y=50)
    tk.Entry(window_sign_up, textvariable=new_pwd, show='*').place(x=150, y=50)
    # 重复密码变量及标签、输入框
    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='请再次输入密码：').place(x=10, y=90)
    tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*').place(x=150, y=90)
    # 确认注册按钮及位置
    bt_confirm_sign_up = tk.Button(window_sign_up, text='确认注册',
                                   command=signtowcg)
    bt_confirm_sign_up.place(x=150, y=130)


# 退出的函数
def usr_sign_quit():
    window.destroy()


# 登录 注册按钮
bt_login = tk.Button(window, text='登录', command=usr_log_in)
bt_login.place(x=140, y=230)
bt_logup = tk.Button(window, text='注册', command=usr_sign_up)
bt_logup.place(x=210, y=230)
bt_logquit = tk.Button(window, text='退出', command=usr_sign_quit)
bt_logquit.place(x=280, y=230)
# 主循环
window.mainloop()
################



    