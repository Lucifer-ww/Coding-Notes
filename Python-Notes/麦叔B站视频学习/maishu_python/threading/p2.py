from time import sleep
from threading import Thread

#小明要下载10个视频
tasks = ['movie1', 'movie2', 'movie3','movie4','movie5','movie6','movie7','movie8','movie9', 'movie10']

def download(movie):
	#print(f'start downloading {movie}')
	sleep(2) #模拟下载电影需要的时间
	#print(f'finished download {movie}')

threads = []

for task in tasks:
	t = Thread(target=download, name=task, args=(task,)) #创建线程
	#print(f'thread {t.name}, {t.ident}')
	t.start() #启动线程
	#print(f'thread {t.name}, {t.ident}')
	threads.append(t)

for t in threads:
	print(f"{t.name} - {t.ident}: {t.is_alive()}")

#1. 线程的构造函数
#2. 属性和方法