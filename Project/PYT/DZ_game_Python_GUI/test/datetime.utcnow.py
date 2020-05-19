import datetime
filename = r"E:\ProgramThomas\Coding-Notes\Project\PYT\打字游戏Python的GUI界面\test\log\datetimeUtcnow.log"
fff=open(filename, 'a+')
for i in range(1, 100):
    fff.write('\n'+str(datetime.datetime.utcnow()))