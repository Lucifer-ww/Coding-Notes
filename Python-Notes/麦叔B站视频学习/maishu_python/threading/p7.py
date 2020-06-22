from time import sleep
from threading import Thread, Lock

#每个下载完后去更新一个计数
count = 0 #记录一共下载了多少视频
thread_tasks = 100000 #每个线程的任务数
thread_num = 100 #线程数

lock = Lock() #一把锁

def download():
	global count
	for i in range(thread_tasks):
		#省掉下载具体步骤
		lock.acquire()
		count += 1
		lock.release()

threads = []
for i in range(thread_num):
	t = Thread(target=download) #创建线程
	t.start() #启动线程
	threads.append(t)

for t in threads:
	t.join() #当前线程等待线程t执行完成后再执行后面的代码

#都下载完成后，能够打印一句话
print(f"应该：{thread_num * thread_tasks}")
print(f"实际：{count}")

