#coding=utf-8
import time
#TODO:调用时间模块
mytimes = time.time()
#TODO:输出时间
print(mytimes) #从1970年开始到现在过去了几秒？
#TODO:输出并强制类型转换为int
print("从1970年到现在过去了：", int(mytimes), '秒')

#TODO:计算时分秒
tt = int(mytimes)
seconds = tt % 60 # 秒
hours = tt // 3600 #小时  用地板除法
mins = tt - tt // 3600 * 3600
print("从1970年到现在过去了：",\
        hours, '时',\
        mins, '分',\
        seconds, '秒')