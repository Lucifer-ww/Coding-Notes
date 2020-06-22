from time import sleep
import threading

#小明要下载10个视频
tasks = ['movie1', 'movie2', 'movie3','movie4','movie5','movie6','movie7','movie8','movie9', 'movie10']

def download(movie):
	print(f'{threading.current_thread().ident} - start downloading {movie}')
	sleep(2) #模拟下载电影需要的时间
	print(f'{threading.current_thread().ident} - finished download {movie}')

t = threading.current_thread()
print(f'{t.name}-{t.ident}')

for task in tasks:
	t = threading.Thread(target=download, name=task, args=(task,)) #创建线程
	t.start() #启动线程

#循环打印所有的线程的ID
for t in threading.enumerate():
	print(f'{t.ident}')
