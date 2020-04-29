# HTML &lt;head>

&lt;head> 元素包含了所有的头部标签元素。在 &lt;head>元素中你可以插入脚本（scripts）, 样式文件（CSS），及各种meta信息。

可以添加在头部区域的元素标签为: &lt;title>, &lt;style>, &lt;meta>, &lt;link>, &lt;script>, &lt;noscript>, and &lt;base>.

## HTML &lt;title> 元素

&lt;title> 标签定义了不同文档的标题。

&lt;title> 在 HTML/XHTML 文档中是必须的。

&lt;title> 元素:

+ 定义了浏览器工具栏的标题
+ 当网页添加到收藏夹时，显示在收藏夹中的标题
+ 显示在搜索引擎结果页面的标题

## HTML &lt;style> 元素

&lt;style> 标签定义了HTML文档的样式文件引用地址.

在&lt;style> 元素中你也可以直接添加样式来渲染 HTML 文档:

```
<head>
<style type="text/css">
body {background-color:yellow}
p {color:blue}
</style>
</head>
```

## HTML &lt;meta> 元素

meta标签描述了一些基本的元数据。

&lt;meta> 标签提供了元数据.元数据也不显示在页面上，但会被浏览器解析。

META 元素通常用于指定网页的描述，关键词，文件的最后修改时间，作者，和其他元数据。

元数据可以使用于浏览器（如何显示内容或重新加载页面），搜索引擎（关键词），或其他Web服务。

&lt;meta> 一般放置于 &lt;head> 区域

为搜索引擎定义关键词:

```html
<meta name="keywords" content="HTML, CSS, XML, XHTML, JavaScript">
```

为网页定义描述内容:

```html
<meta name="description" content="免费 Web & 编程 教程">
```

定义网页作者:

```html
<meta name="author" content="Runoob">
```

每30秒钟刷新当前页面:

```html
<meta http-equiv="refresh" content="30">
```

## HTML &lt;script> 元素

&lt;script>标签用于加载脚本文件，如： JavaScript。

&lt;script> 元素在以后的章节中会详细描述。