#coding:UTF-8
import time
filename = r"E:\ProgramThomas\Coding-Notes\Project\PYT\打字游戏Python的GUI界面\test\log\time.time.log"
fff = open(filename, 'a+')
for i in range(1, 500):
    fff.write('\n'+str(time.time()))