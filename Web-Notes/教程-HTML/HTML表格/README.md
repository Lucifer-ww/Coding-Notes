# HTML表格
## HTML 表格实例:

| First Name | Last Name | Points |
| :--------- | :-------- | :----- |
| Jill       | Smith     | 50     |
| Eve        | Jackson   | 94     |
| John       | Doe       | 80     |
| Adam       | Johnson   | 67     |

<pre><font face="Microsoft YAHEI">
每个表格从一个 table 标签开始。 
每个表格行从 tr 标签开始。
每个表格的数据从 td 标签开始。</font>
</pre>
光说不管用，看看代码示例？
```html
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>

<h4>一列:</h4>
<table border="1">
<tr>
  <td>100</td>
</tr>
</table>

<h4>一行三列:</h4>
<table border="1">
<tr>
  <td>100</td>
  <td>200</td>
  <td>300</td>
</tr>
</table>

<h4>两行三列:</h4>
<table border="1">
<tr>
  <td>100</td>
  <td>200</td>
  <td>300</td>
</tr>
<tr>
  <td>400</td>
  <td>500</td>
  <td>600</td>
</tr>
</table>

</body>
</html>
```
结果如下：
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>

<h4>一列:</h4>
<table border="1">
<tr>
  <td>100</td>
</tr>
</table>

<h4>一行三列:</h4>
<table border="1">
<tr>
  <td>100</td>
  <td>200</td>
  <td>300</td>
</tr>
</table>

<h4>两行三列:</h4>
<table border="1">
<tr>
  <td>100</td>
  <td>200</td>
  <td>300</td>
</tr>
<tr>
  <td>400</td>
  <td>500</td>
  <td>600</td>
</tr>
</table>

</body>
</html>

&emsp;表格由 &lt;table> 标签来定义。每个表格均有若干行（由 &lt;tr> 标签定义），每行被分割为若干单元格（由 &lt;td> 标签定义）。字母 td 指表格数据（table data），即数据单元格的内容。数据单元格可以包含文本、图片、列表、段落、表单、水平线、表格等等。
创建一个表格的实例如下（其实上面的也不错）：
```html
<table border="1">
    <tr>
        <td>row 1, cell 1</td>
        <td>row 1, cell 2</td>
    </tr>
    <tr>
        <td>row 2, cell 1</td>
        <td>row 2, cell 2</td>
    </tr>
</table>
```
在浏览器中的结果如下:sunny:
<html>
<head>
<meta charset=UTF-8>
</head>
<body>
<table border="1">
    <tr>
        <td>row 1, cell 1</td>
        <td>row 1, cell 2</td>
    </tr>
    <tr>
        <td>row 2, cell 1</td>
        <td>row 2, cell 2</td>
    </tr>
</table>
</body>
</html>

## HTML 表格和边框属性
如果不定义边框属性，表格将不显示边框。有时这很有用，但是大多数时候，我们希望显示边框。

使用边框属性来显示一个带有边框的表格：
```html
<table border="1">
    <tr>
        <td>Row 1, cell 1</td>
        <td>Row 1, cell 2</td>
    </tr>
</table>
```
## HTML 表格表头
表格的表头使用 &lt;th>(table head) 标签进行定义。

大多数浏览器会把表头显示为粗体居中的文本：
```html
<table border="1">
    <tr>
        <th>Header 1</th>
        <th>Header 2</th>
    </tr>
    <tr>
        <td>row 1, cell 1</td>
        <td>row 1, cell 2</td>
    </tr>
    <tr>
        <td>row 2, cell 1</td>
        <td>row 2, cell 2</td>
    </tr>
</table>
```
浏览器中显示如下
<table border="1">
    <tr>
        <th>Header 1</th>
        <th>Header 2</th>
    </tr>
    <tr>
        <td>row 1, cell 1</td>
        <td>row 1, cell 2</td>
    </tr>
    <tr>
        <td>row 2, cell 1</td>
        <td>row 2, cell 2</td>
    </tr>
</table>

## 更多实例

[没有边框的表格](https://www.runoob.com/try/try.php?filename=tryhtml_tables3)
本例演示一个没有边框的表格。

[表格中的表头(Heading)](https://www.runoob.com/try/try.php?filename=tryhtml_table_headers)
本例演示如何显示表格表头。

[带有标题的表格](https://www.runoob.com/try/try.php?filename=tryhtml_tables2)
本例演示一个带标题 (caption) 的表格

[跨行或跨列的表格单元格](https://www.runoob.com/try/try.php?filename=tryhtml_table_span)
本例演示如何定义跨行或跨列的表格单元格。

[表格内的标签](https://www.runoob.com/try/try.php?filename=tryhtml_table_elements)
本例演示如何显示在不同的元素内显示元素。

:heart:最后给一个漂亮的表格，用菜鸟工具写的:heart:
<iframe width="100%" height="300" src="https://c.runoob.com/iframe/3187" allowfullscreen="allowfullscreen" frameborder="0"></iframe>