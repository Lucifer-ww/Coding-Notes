# 从文件加载数据

很多时候，我们想要绘制文件中的数据。 有许多类型的文件，以及许多方法，你可 以使用它们从文件中提取数据来图形化。 在这里，我们将展示几种方法。 首先， 我们将使用内置的 csv 模块加载CSV文件，然后我们将展示如何使用 NumPy（第 三方模块）加载文件。

```python
import matplotlib.pyplot as plt
import csv
x = [] y = []

with open('example.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0])) 
        y.append(int(row[1]))

plt.plot(x,y, label='Loaded from file!') plt.xlabel('x') 
plt.ylabel('y') plt.title('Interesting Graph\nCheck it out') 
plt.legend()
plt.show()
```

![image-20200708134228406](F:\Coding-Thomas\Coding-Notes\Python-Notes\例程\##matplotlib\PDF教程\DOC\image-20200708134228406.png)



这里，我们打开样例文件，包含以下数据：（ `example.txt` ）
```
1,5
2,3
3,4
4,7
5,4
6,3
7,5
8,7
9,4
10,4
```

接下来，我们使用 `csv` 模块读取数据。 `csv` 读取器自动按行分割文件，然后使用我们选择的分隔符分割文件中的数据。 在我们的例子中，这是一个逗号。 注意： csv 模块和 csv reader 不需要文件在字面上是一个`.csv`文件。 它可以是任何具有分隔数据的简单的文本文件。一旦我们这样做了，我们将索引为 0 的元素存储到 x 列表，将索引为 1 的元素存储到 y 列表中。 之后，我们都设置好了，准备绘图，然后显示数据。

虽然使用 `CSV` 模块是完全正常的，但使用 `NumPy` 模块来加载我们的文件和数据，可能对我们更有意义。 如果你没有 NumPy，你需要按下面的步骤来获取它。为了了解安装模块的更多信息，请参阅 [pip](http://pythonprogramming.net/using-pip-install-for-python-modules/) 教程。 大多数人应该都能打开命令行，并执行 `pip install numpy` 。如果不能，请参阅链接中的教程。一旦你安装了 NumPy，你可以编写如下代码：

```python
import matplotlib.pyplot as plt
import numpy as np
x, y = np.loadtxt('example.txt', delimiter=',', unpack=True)
plt.plot(x,y, label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
```

结果应该是相同的图表。 稍后，当我们加载数据时，我们可以利用 NumPy 为我们做一些更多的工作，但这是教程未来的内容。 就像 `csv` 模块不需要一个特地的 `.csv` 一样， `loadtxt` 函数不要求文件是一个 `.txt` 文件，它可以是一个 `.csv` ，它甚至可以是一个 python 列表对象。

