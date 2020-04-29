# 学会Python的time模块
&emsp;Python用import可以引入关于时间的模块**time**
## 输出从1970年到今天过了多少秒？
```python
import time
mytimes = time.time()
print("从1970年到今天过了：", mytimes, "秒")
```
但是我们会发现输出了一个小数，这是一个浮点数，所以强制类型转换就行
```python
import time
mytimes = time.time()
print("从1970年到今天过了：", int(mytimes), "秒")
```
输出来的就是整形了
## 计算时分秒
```python
import time
mytimes = time.time()
tt = int(mytimes)
seconds = tt % 60 # 秒
hours = tt // 3600 #小时  用地板除法
mins = tt - tt // 3600 * 3600
print("从1970年到现在过去了：",\
        hours, '时',\
        mins, '分',\
        seconds, '秒')   
```
其中用到的知识点<br>
1、import引入<br>2、强制类型转换
<br>3、地板除法<br>4、输出控制`\`符号