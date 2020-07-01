# Matplotlib 图例、标题、标签

在本教程中，我们将讨论 Matplotlib 中的图例，标题和标签。 很多时候，图形可以不言自明，但是图形带有标题，轴域上的标签和图例，来解释每一行是什么非常必要。

```python
import matplotlib.pyplot as plt
x = [1,2,3]
y = [5,7,4]
x2 = [1,2,3]
y2 = [10,14,12]
```

这样子可以创建两条线，接下来放置并添加标签：

```python
plt.plot(x, y, label='First Line')
plt.plot(x2, y2, label='Second Line')
```

在这里，我们绘制了我们已经看到的东西，但这次我们添加另一个参数 label 。这允许我们为线条指定名称，我们以后可以在图例中显示它。 我们的其余代码为：

```python
plt.xlabel('Plot Number')
plt.ylabel('Important var')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
```

`xlabel`的意思是x轴的标签，`ylabel`的意思是y轴的标签，`title`是图表的标题，`legend`是生成默认图例，最后将其显示。

运行：

![image-20200628140712506](E:\ProgramThomas\Coding-Notes\Python-Notes\例程\##matplotlib\PDF教程\DOC\image-20200628140712506.png)

点击保存按钮，将图表位置保存，其他都去掉

![](E:\ProgramThomas\Coding-Notes\Python-Notes\例程\##matplotlib\PDF教程\DOC\01-添加图例_标题_标签.png)

哇，特别酷，和excel有一拼了，下一节讲条形图和直方图