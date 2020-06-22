from time import sleep
from threading import Thread

#小明要下载10个视频
tasks = ['movie1', 'movie2', 'movie3','movie4','movie5','movie6','movie7','movie8','movie9', 'movie10']

def download(movie):
	print(f'start downloading {movie}')
	sleep(2) #模拟下载电影需要的时间
	print(f'finished download {movie}')

#守护线程，当主线程执行完成后，马上就终止当前的任务，不管是否完成
for task in tasks:
	t = Thread(target=download, name=task, args=(task,), daemon=True) #创建线程
	t.start() #启动线程
	print(f'{t.name} is daemon: {t.daemon}')

print('finished downloading')

