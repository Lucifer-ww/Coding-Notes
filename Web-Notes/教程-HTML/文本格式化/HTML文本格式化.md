[TOC]
### <font color=#ff0000>HTML文本格式化</font>

#### 通用格式

通常标签 &lt;strong> 替换加粗标签 &lt;b> 来使用, &lt;em> 替换 &lt;i>标签使用。<br>然而，这些标签的含义是不同的：<br>&lt;b> 与&lt;i> 定义粗体或斜体文本。<br>&lt;strong> 或者 &lt;em>意味着你要呈现的文本是重要的，所以要突出显示。现今所有主要浏览器都能渲染各种效果的字体。不过，未来浏览器可能会支持更好的渲染效果。

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
</head>
<body>
<b>这个文本是加粗的</b>
<br />
<strong>这个文本是加粗的</strong>
<br />
<big>这个文本字体放大</big>
<br />
<em>这个文本是斜体的</em>
<br />
<i>这个文本是斜体的</i>
<br />
<small>这个文本是缩小的</small>
<br />
这个文本包含
<sub>下标</sub>
<br />
这个文本包含
<sup>上标</sup>
</body>
</html>
```
呈现效果：
___
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
<b>这个文本是加粗的</b>
<br />
<strong>这个文本是加粗的</strong>
<br />
<big>这个文本字体放大</big>
<br />
<em>这个文本是斜体的</em>
<br />
<i>这个文本是斜体的</i>
<br />
<small>这个文本是缩小的</small>
<br />
这个文本包含
<sub>下标</sub>
<br />
这个文本包含
<sup>上标</sup>
</body>
</html>
____


#### 单词缩写格式

```html
<!DOCTYPE html> 
<html>
<head> 
<meta charset="utf-8"> 
</head>
<body>
<abbr title="etcetera">etc.</abbr>
<br />
<acronym title="World Wide Web">WWW</acronym>
<p>在某些浏览器中，当您把鼠标移至缩略词语上时，title 可用于展示表达的完整版本。</p>
<p>仅对于 IE 5 中的 acronym 元素有效。</p>
<p>对于 Netscape 6.2 中的 abbr 和 acronym 元素都有效。</p>
</body>
</html>
```

____

呈现：

<!DOCTYPE html> 
<html>
<head> 
<meta charset="utf-8"> 
</head>
<body>
<abbr title="etcetera">etc.</abbr>
<br />
<acronym title="World Wide Web">WWW</acronym>
<p>在某些浏览器中，当您把鼠标移至缩略词语上时，title 可用于展示表达的完整版本。</p>
<p>仅对于 IE 5 中的 acronym 元素有效。</p>
<p>对于 Netscape 6.2 中的 abbr 和 acronym 元素都有效。</p>
</body>
</html>
____



#### 增加下划线和删除线

```html
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
</head>
<body>

<p>My favorite color is <del>blue</del> <ins>red</ins>!</p>

</body>
</html>
```

呈现效果：
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>

<p>My favorite color is <del>blue</del> <ins>red</ins>!</p>

____

#### 文字顺序

```html
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
</head> 
<body>
<p>该段落文字从左到右显示。</p>  
<p><bdo dir="rtl">该段落文字从右到左显示。</bdo></p>  
</body>
</html>
```

效果：

<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
</head> 
<body>
<p>该段落文字从左到右显示。</p>  
<p><bdo dir="rtl">该段落文字从右到左显示。</bdo></p>  
</body>
</html>
____

#### 预格式文本

此例演示如何使用 pre 标签对空行和空格进行控制。

```html
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
</head>
<body>
<pre>
此例演示如何使用 pre 标签
对空行和    空格
进行控制
</pre>
</body>
</html>
```

呈现效果：

<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
</head>
<body>
<pre>
此例演示如何使用 pre 标签
对空行和    空格
进行控制
</pre>
</body>
</html>
____


#### 总结


&lt;br /> 换行
&lt;strong>&lt;/strong> 加粗
&lt;b>&lt;/b> 加粗
&lt;em>&lt;/em> 斜体
&lt;i>&lt;/i> 斜体
&lt;small>&lt;/small> 字体缩小
&lt;big>&lt;/big> 字体放大
&lt;sub>&lt;/sub> 下标
&lt;sup>&lt;/sup> 上标

&lt;abbr>&lt;/abbr> 缩写
&lt;acronym>&lt;/acronym> 缩写

&lt;del>&lt;/del> 删除线
&lt;ins>&lt;/ins> 下划线

&lt;bdo>&lt;/bdo> 文字顺序

&lt;pre>&lt;/pre> 预格式文本


