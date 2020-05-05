>News:
>我的编程学习笔记仓库已经出炉上线，正在快速维护中……
>地址：<https://github.com/Github-Programer/LeetCode-Notes>

学习HTML去网上搜索，&lt;div>标签和&lt;span>标签都没有详细解释，我仔细看了W3Cschool和菜鸟教程才明白，我来说一下

<font size=5 color=skyblue>Div和Span目录：</font>
+ [&lt;div>](#1)
+ [&lt;span>](#2)

<h1 id=1>&lt;div>标签</h1>
菜鸟教程中这一章叫做‘区块’，第一反应是区块链，第二次看才明白是设定区域

大多数 HTML 元素被定义为块级元素或内联元素。

块级元素在浏览器显示时，通常会以新行来开始（和结束）。

实例: <br>
文档中的一个区域将显示为蓝色：
```html
<div style="color:#0000FF">
  <h3>这是一个在 div 元素中的标题。</h3>
  <p>这是一个在 div 元素中的文本。</p>
</div>
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200505200636796.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Nvb2w5OTc4MQ==,size_16,color_FFFFFF,t_70)
div标签的浏览器支持<br>
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200505200713806.png)
再来一个实例：
```html
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>

<div id="container" style="width:500px">

<div id="header" style="background-color:#FFA500;">
<h1 style="margin-bottom:0;">主要的网页标题</h1></div>

<div id="menu" style="background-color:#FFD700;height:200px;width:100px;float:left;">
<b>菜单</b><br>
HTML<br>
CSS<br>
JavaScript</div>

<div id="content" style="background-color:#EEEEEE;height:200px;width:400px;float:left;">
内容在这里</div>

<div id="footer" style="background-color:#FFA500;clear:both;text-align:center;">
版权 © runoob.com</div>

</div>
 
</body>
</html>
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200505202505913.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Nvb2w5OTc4MQ==,size_16,color_FFFFFF,t_70)

<h1 id=2>&lt;span>标签</h1>
实例：<br>
使用 &lt;span> 元素对文本中的一部分进行着色：

```html
<p>我的母亲有 <span style="color:blue">蓝色</span> 的眼睛。</p>
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200505202527535.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Nvb2w5OTc4MQ==,size_16,color_FFFFFF,t_70)