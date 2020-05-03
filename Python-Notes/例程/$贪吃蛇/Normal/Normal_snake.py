import random
import pygame
import sys
from pygame.locals import *


# 屏幕大小
Window_Width = 800
Window_Height = 500
# 刷新频率
Display_Clock = 17
# 一块蛇身大小
Cell_Size = 20
assert Window_Width % Cell_Size == 0
assert Window_Height % Cell_Size == 0
Cell_W = int(Window_Width/Cell_Size)
Cell_H = int(Window_Height/Cell_Size)
# 背景颜色
Background_Color = (0, 0, 0)
# 蛇头索引
Head_index = 0


# 关闭游戏界面
def close_game():
	pygame.quit()
	sys.exit()


# 检测玩家的按键
def Check_PressKey():
	if len(pygame.event.get(QUIT)) > 0:
		close_game()
	KeyUp_Events = pygame.event.get(KEYUP)
	if len(KeyUp_Events) == 0:
		return None
	elif KeyUp_Events[0].key == K_ESCAPE:
		close_game()
	return KeyUp_Events[0].key


# 显示当前得分
def Show_Score(score):
	score_Content = Main_Font.render('得分：%s' % (score), True, (255, 255, 255))
	score_Rect = score_Content.get_rect()
	score_Rect.topleft = (Window_Width-120, 10)
	Main_Display.blit(score_Content, score_Rect)


# 获得果实位置
def Get_Apple_Location(snake_Coords):
	flag = True
	while flag:
		apple_location = {'x': random.randint(0, Cell_W-1), 'y': random.randint(0, Cell_H-1)}
		if apple_location not in snake_Coords:
			flag = False
	return apple_location


# 显示果实
def Show_Apple(coord):
	x = coord['x'] * Cell_Size
	y = coord['y'] * Cell_Size
	apple_Rect = pygame.Rect(x, y, Cell_Size, Cell_Size)
	pygame.draw.rect(Main_Display, (255, 0, 0), apple_Rect)


# 显示蛇
def Show_Snake(coords):
	x = coords[0]['x'] * Cell_Size
	y = coords[0]['y'] * Cell_Size
	Snake_head_Rect = pygame.Rect(x, y, Cell_Size, Cell_Size)
	pygame.draw.rect(Main_Display, (0, 80, 255), Snake_head_Rect)
	Snake_head_Inner_Rect = pygame.Rect(x+4, y+4, Cell_Size-8, Cell_Size-8)
	pygame.draw.rect(Main_Display, (0, 80, 255), Snake_head_Inner_Rect)
	for coord in coords[1:]:
		x = coord['x'] * Cell_Size
		y = coord['y'] * Cell_Size
		Snake_part_Rect = pygame.Rect(x, y, Cell_Size, Cell_Size)
		pygame.draw.rect(Main_Display, (0, 155, 0), Snake_part_Rect)
		Snake_part_Inner_Rect = pygame.Rect(x+4, y+4, Cell_Size-8, Cell_Size-8)
		pygame.draw.rect(Main_Display, (0, 255, 0), Snake_part_Inner_Rect)


# 画网格
def draw_Grid():
	# 垂直方向
	for x in range(0, Window_Width, Cell_Size):
		pygame.draw.line(Main_Display, (40, 40, 40), (x, 0), (x, Window_Height))
	# 水平方向
	for y in range(0, Window_Height, Cell_Size):
		pygame.draw.line(Main_Display, (40, 40, 40), (0, y), (Window_Width, y))


# 显示开始界面
def Show_Start_Interface():
	title_Font = pygame.font.Font('simkai.ttf', 100)
	title_content = title_Font.render('贪吃蛇', True, (255, 255, 255), (0, 0, 160))
	angle = 0
	while True:
		Main_Display.fill(Background_Color)
		rotated_title = pygame.transform.rotate(title_content, angle)
		rotated_title_Rect = rotated_title.get_rect()
		rotated_title_Rect.center = (Window_Width/2, Window_Height/2)
		Main_Display.blit(rotated_title, rotated_title_Rect)
		pressKey_content = Main_Font.render('按任意键开始游戏！', True, (255, 255, 255))
		pressKey_Rect = pressKey_content.get_rect()
		pressKey_Rect.topleft = (Window_Width-200, Window_Height-30)
		Main_Display.blit(pressKey_content, pressKey_Rect)
		if Check_PressKey():
			# 清除事件队列
			pygame.event.get()
			return
		pygame.display.update()
		Snake_Clock.tick(Display_Clock)
		angle -= 5


# 显示结束界面
def Show_End_Interface():
	title_Font = pygame.font.Font('simkai.ttf', 100)
	title_game = title_Font.render('Game', True, (233, 150, 122))
	title_over = title_Font.render('Over', True, (233, 150, 122))
	game_Rect = title_game.get_rect()
	over_Rect = title_over.get_rect()
	game_Rect.midtop = (Window_Width/2, 70)
	over_Rect.midtop = (Window_Width/2, game_Rect.height+70+25)
	Main_Display.blit(title_game, game_Rect)
	Main_Display.blit(title_over, over_Rect)
	pressKey_content = Main_Font.render('按任意键开始游戏！', True, (255, 255, 255))
	pressKey_Rect = pressKey_content.get_rect()
	pressKey_Rect.topleft = (Window_Width-200, Window_Height-30)
	Main_Display.blit(pressKey_content, pressKey_Rect)
	pygame.display.update()
	pygame.time.wait(500)
	# 清除事件队列
	Check_PressKey()
	while True:
		if Check_PressKey():
			pygame.event.get()
			return


# 运行游戏
def Run_Game():
	# 蛇出生地
	start_x = random.randint(5, Cell_W-6)
	start_y = random.randint(5, Cell_H-6)
	snake_Coords = [{'x': start_x, 'y': start_y},
					{'x': start_x-1, 'y': start_y},
					{'x': start_x-2, 'y': start_y}]
	direction = 'right'
	apple_location = Get_Apple_Location(snake_Coords)
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				close_game()
			elif event.type == KEYDOWN:
				if (event.key == K_LEFT) and (direction != 'right'):
					direction = 'left'
				elif (event.key == K_RIGHT) and (direction != 'left'):
					direction = 'right'
				elif (event.key == K_UP) and (direction != 'down'):
					direction = 'up'
				elif (event.key == K_DOWN) and (direction != 'up'):
					direction = 'down'
				elif event.key == K_ESCAPE:
					close_game()
		# 碰到墙壁或者自己则游戏结束
		if (snake_Coords[Head_index]['x'] == -1) or (snake_Coords[Head_index]['x'] == Cell_W) or \
		   (snake_Coords[Head_index]['y'] == -1) or (snake_Coords[Head_index]['y'] == Cell_H):
			return
		if snake_Coords[Head_index] in snake_Coords[1:]:
			return
		if (snake_Coords[Head_index]['x'] == apple_location['x']) and (snake_Coords[Head_index]['y'] == apple_location['y']):
			apple_location = Get_Apple_Location(snake_Coords)
		else:
			del snake_Coords[-1]
		if direction == 'up':
			newHead = {'x': snake_Coords[Head_index]['x'],
					   'y': snake_Coords[Head_index]['y']-1}
		elif direction == 'down':
			newHead = {'x': snake_Coords[Head_index]['x'],
					   'y': snake_Coords[Head_index]['y']+1}
		elif direction == 'left':
			newHead = {'x': snake_Coords[Head_index]['x']-1,
					   'y': snake_Coords[Head_index]['y']}
		elif direction == 'right':
			newHead = {'x': snake_Coords[Head_index]['x']+1,
					   'y': snake_Coords[Head_index]['y']}
		snake_Coords.insert(0, newHead)
		Main_Display.fill(Background_Color)
		draw_Grid()
		Show_Snake(snake_Coords)
		Show_Apple(apple_location)
		Show_Score(len(snake_Coords)-3)
		pygame.display.update()
		Snake_Clock.tick(Display_Clock)


# 主函数
def main():
	global Main_Display, Main_Font, Snake_Clock
	pygame.init()
	Snake_Clock = pygame.time.Clock()
	Main_Display = pygame.display.set_mode((Window_Width, Window_Height))
	Main_Font = pygame.font.Font('simkai.ttf', 18)
	pygame.display.set_caption('Normal_snake')
	Show_Start_Interface()
	while True:
		Run_Game()
		Show_End_Interface()



if __name__ == '__main__':
	main()