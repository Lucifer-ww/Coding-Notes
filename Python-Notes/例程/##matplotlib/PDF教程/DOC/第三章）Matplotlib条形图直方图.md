# Matplotlib条形图

这个教程中我们会涉及条形图和直方图。我们先来看条形图：

函数是`plt.bar`，提示一下，`import matplotlib.pyplot as plt`这一句和`from matplotlib import pyplot as plt`是一样的，使用函数时两个列表是两组坐标，第一个列表是x轴，第二个是y轴

```python
import matplotlib.pyplot as plt
plt.bar([1,3,5,7,9],[5,2,7,8,2], label="Example one")
plt.bar([2,4,6,8,10],[8,6,2,5,6], label="Example two", color='g')
plt.legend()
plt.xlabel('bar number')
plt.ylabel('bar height')
plt.title('Epic Graph\nAnother Line! Whoa')
plt.show()
```

`plt.bar` 为我们创建条形图。 如果你没有明确选择一种颜色，那么虽然做了多个图，所有的条看起来会一样。 这让我们有机会使用一个新的 Matplotlib 自定义选项。 你可以在任何类型的绘图中使用颜色，例如 `g` 为绿色， `b` 为蓝色， `r` 为红色，等等。 你还可以使用十六进制颜色代码，如 `#191970` 。

![image-20200702122952092](E:\ProgramThomas\Coding-Notes\Python-Notes\例程\##matplotlib\PDF教程\DOC\image-20200702122952092.png)

# Matplotlib直方图

接下来，我们会讲解直方图。 直方图非常像条形图，倾向于通过将区段组合在一起来显示分布。 这个例子可能是年龄的分组，或测试的分数。 我们并不是显示每一组的年龄，而是按照 20 ~ 25，25 ~ 30... 等等来显示年龄。 这里有一个例子：

```python
import matplotlib.pyplot as plt
population_ages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,1
21,122,130,111,115,112,80,75,65,54,44,43,42,48]
bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
```

对于 plt.hist ，你首先需要放入所有的值，然后指定放入哪个桶或容器。 在我们的例子中，我们绘制了一堆年龄，并希望以 10 年的增量来显示它们。 我们将条形的宽度设为 0.8，但是如果你想让条形变宽，或者变窄，你可以选择其他的宽度。