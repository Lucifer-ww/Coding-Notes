# 饼图

饼图通常以%为单位，但是matplotlib可以自动处理，我们只需要提供数值

实例代码：

```python
import matplotlib.pyplot as plt
slices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','b']
plt.pie(slices,
labels=activities,
colors=cols,
startangle=90,
shadow= True,
explode=(0,0.1,0,0),
autopct='%1.1f%%')
plt.title('Interesting Graph\nCheck it out')
plt.show()
```

运行结果：

![image-20200707143049857](F:\Coding-Thomas\Coding-Notes\Python-Notes\例程\##matplotlib\PDF教程\DOC\image-20200707143049857.png)

详细解释：

+ `slices`用来存储切片大小，睡觉占7份，玩占13份
+ `activities`列表存储名称，最后放到标签中
+ `cols`存储颜色名称，标记每一片的颜色。matplotlib中的颜色还可以是一个字母的，也可以是全称，也可以是十六进制，但是单个字母不全也不好记，在文章最后给一个参考图
+ `shadow`就是阴影，`True`为开启，`False`为关闭
+ `explode`可以拉出一个切片，样例中`(0,0.1,0,0)`设置第二个切片就是eating部分拉出0.1距离。
+ `autopct`最后将百分比放置在切片上



颜色表：

![img](https://upload-images.jianshu.io/upload_images/7017253-6edec09676cc466d.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)