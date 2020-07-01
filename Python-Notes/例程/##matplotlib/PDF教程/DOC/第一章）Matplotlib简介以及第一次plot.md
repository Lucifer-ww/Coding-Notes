# Matplotlib

matplotlib是Python中很知名的一个数据可视化库，功能异常丰富，所以学完需要很久，其支持2D图，折线、条形、饼图、散装图、直方图，也可以画3D图。虽然matplotlib强大，但是文档很少，下面是Matplotlib教程，也是我的学习笔记。

一下均使用Python3+版本

# Install

首先需要安装matplotlib，使用pip安装更方便

```powershell
pip install matplotlib
```

或者，你可以前往 Matplotlib.org 并通过访问下载页面下载适当的版本进行安装。请记住，因为你的操作系统为 64 位，你不一定需要 64 位版本的 Python。 如果你不打算尝试 64 位，你可以使用 32 位。 打开 IDLE 并阅读顶部。 如果它说你是 64位，你就是 64 位，如果它说是 32 位，那么你就是 32 位。 一旦你安装了Python，你就做好了准备，你可以编写任何你想要的逻辑。 我喜欢使用 IDLE 来编程，但你可以随意使用任何你喜欢的东西。

# import

首先导入库

```python
import matplotlib.pyplot as plt
```

这样子简化少打几个字母

# First Picture

我们来做第一个matplotlib图像，在matplotlib中，`plot`函数负责绘制，我们先来创建一些线条

```python
plt.plot([1,2,3],[5,7,4])
```

接下来，我们调用 plot 的 .plot 方法绘制一些坐标。 这个 `.plot` 需要许多参数，但前两个是 'x' 和 'y' 坐标，我们放入列表。 这意味着，根据这些列表我们拥有 3 个坐标： [1, 5] [2, 7] 和 [3, 4] 。

绘制完成将其显示

```python
plt.show()
```

完整代码：

```python
# coding: utf-8
import matplotlib.pyplot as plt
plt.plot([1,2,3],[5,7,4])
plt.show()
```

# Results analysis

结果是弹出一个窗口，然后有一个折线

![image-20200627212618462](E:\ProgramThomas\Coding-Notes\Python-Notes\例程\##matplotlib\PDF教程\DOC\image-20200627212618462.png)

这是一个集成窗口了，图表我们不说，几个点可以看出来，底下的按钮我们需要说一下。可能不同版本的matplotlib的图标不同，但是功能一样。

## Home（主页）

![image-20200627212741813](E:\ProgramThomas\Coding-Notes\Python-Notes\例程\##matplotlib\PDF教程\DOC\image-20200627212741813.png)

一旦你开始浏览你的图表，主页按钮会帮助你。 如果你想要返回原始视图，可以单击它。 在浏览图表之前单击此按钮将不会生效。

## Forward/Back（前进/后退）

![image-20200627212814658](E:\ProgramThomas\Coding-Notes\Python-Notes\例程\##matplotlib\PDF教程\DOC\image-20200627212814658.png)

这些按钮可以像浏览器中的前进和后退按钮一样使用。 你可以单击这些来移回到你之前的位置，或再次前进。

## Pan（平移）

![image-20200627212901453](E:\ProgramThomas\Coding-Notes\Python-Notes\例程\##matplotlib\PDF教程\DOC\image-20200627212901453.png)

你可以点击平移按钮，之后点击并拖拽你的图表。

## Zoom（缩放）

![image-20200627212938598](E:\ProgramThomas\Coding-Notes\Python-Notes\例程\##matplotlib\PDF教程\DOC\image-20200627212938598.png)

缩放按钮可让你单击它，然后单击并拖动出要放大的方形区域。 放大需要左键单击并拖动。 你也可以右键单击并拖动来缩小。

## Configure subplots（配置子图）

![image-20200627213023310](E:\ProgramThomas\Coding-Notes\Python-Notes\例程\##matplotlib\PDF教程\DOC\image-20200627213023310.png)

此按钮允许你对图形和绘图配置各种间距选项。 点击它会弹出：

![image-20200627213059132](E:\ProgramThomas\Coding-Notes\Python-Notes\例程\##matplotlib\PDF教程\DOC\image-20200627213059132.png)

每个蓝色条形都是一个滑块，它允许你调整内边距。 其中有些现在没有任何效果，因为没有任何其他子图。 前四个值调整图形到窗口边缘的边距。 之后 wspace 和 hspace 对应于当你绘制多个子图时，它们的水平或竖直间距。

## Save（保存）

![image-20200627213204710](E:\ProgramThomas\Coding-Notes\Python-Notes\例程\##matplotlib\PDF教程\DOC\image-20200627213204710.png)

此按钮允许你以各种形式保存图形。所以这是 matplotlib 的快速介绍，我们之后会涉及更多。