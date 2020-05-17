# JSON笔记

JSON是一种数据交换格式，可以存储较多的数据，相对于txt文本文件会好得多，可以自定义标签，JSON可以直接被JS转化，JSON的全称叫做**J**ava**S**cript **O**bject **N**otation（故称为JSON）。

学习Python进展到了数据交换格式这一章，书中提供了三种数据格式，JSON是最后一种，但是我打算先学这一种，为什么？（共有CSV、XML和JSON）

CSV只能用`,`逗号分隔，功能不够强，而JSON可以实现这一点，XML也可以但是有点类似HTML，写起来十分麻烦（写过前端的人就知道），但是可以自定义标签，但是XML的几乎所有功能JSON都支持，而且我经常用VScode写的代码，VScode提供一个插件可以直接把XML转成JSON，JSON支持字典、列表、类等格式，而且JSON相对于XML很简单，XML每次都要写`<>`但是JSON不用，格式不复杂，只要在大括号的包围中就行。

来看一个简单的实例：

**1、JSON**
```json
{
    "company": Volkswagen,
    "name": "Vento",
    "price": 800000
}
```

**2、XML**
```xml
<car>
   <company>Volkswagen</company>
   <name>Vento</name>
   <price>800000</price>
</car>
```