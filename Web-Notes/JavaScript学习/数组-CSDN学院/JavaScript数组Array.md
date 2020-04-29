### JavaScript数组Array

如果要存储多个数只能用数组

```html
<!DOCTYPE html>
<html>
    <head>
    	<meta charset="UTF-8">
    	<title>数组Array</title>
    </head>
    <body>
        <script type="text/javascript">
            var a = 'mjj';
        </script>
    </body>
</html>
```

数组是一个仓库

数组实例：购物清单

```html
<html>
    <head>
        <meta charset="UFT-8">
        <title>购物清单</title>
    </head>
    <body>
        <script type="text/javascript">
            var shopping = ['香蕉', '苹果', '签字笔', 'U盘'];
            console.log(shopping);
			window.alert(shopping);
        </script>
    </body>
</html>
```

<img src="https://img-blog.csdnimg.cn/20200404194624501.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Nvb2w5OTc4MQ==,size_16,color_FFFFFF,t_70" alt="ALT" style="zoom: 50%;" />

console.log()是输出到控制台

window.alert()是弹出窗口

<img src="https://img-blog.csdnimg.cn/20200404195046763.png" alt="ALT" style="zoom:50%;" />

点击左边的箭头查看详细，方框内有索引和其对照的值，length是长度，下面的不用看，我也不懂

数组可以存储字符串、字符、数字甚至再存储一个数组，也就是二维数组

```html
<html>
    <head>
        <meta charset="UFT-8">
        <title>购物清单</title>
    </head>
    <body>
        <script type="text/javascript">
            var shopping = ['香蕉', '苹果', '签字笔', 'U盘'];
            console.log(shopping);
			window.alert(shopping);
            
            var rr = ['tree', '123', 123, shopping];
            console.log(shopping);
        </script>
    </body>
</html>
```

<img src="https://img-blog.csdnimg.cn/20200404195619434.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Nvb2w5OTc4MQ==,size_16,color_FFFFFF,t_70" alt="ALT" style="zoom:50%;" />

数组rr中包含了数组shopping，就是二维数组

除外，数组还可以访问、修改

**访问**

```js
var rr = ['a', 'b'];
var item1 = rr[0]; //item1获取第一个元素
console.log(item1);
```

输出的是a，为什么？因为item1取的是rr的0号下标

**修改**

```js
var rr = ['a', 'b'];
rr[0] = 'c';
console.log(rr);
```

输出的不是a，b，为什么？因为修改了rr[0]的值

