# JSON语法

来源-编程狮W3Cschool：<https://www.w3cschool.cn/json/json-syntax.html>

在使用JSON之前来学习一下JSON的语法

+ 数据使用名/值对表示。
+ 使用大括号保存对象，每个名称后面跟着一个 ':'（冒号），名/值对使用 ,（逗号）分割。
+ 使用方括号保存数组，数组值使用 ,（逗号）分割。

实例：
```json
{
    "book": [
        {
            "id":"01",
            "language": "Java",
            "edition": "third",
            "author": "Herbert Schildt"
        },
        {
            "id":"07",
            "language": "C++",
            "edition": "second"
            "author": "E.Balagurusamy"
    }]
}
```
JSON 支持以下两种数据结构：

+ **名/值对集合：** 这一数据结构由不同的编程语言支持。
+ **有序的值列表：** 包括数组，列表，向量或序列等等。

## JSON 语法规则

JSON 语法是 JavaScript 对象表示法语法的子集。

JSON 语法规则不复杂，它参考了 C 语言家族的一些习惯，学习起来并不会感到陌生。

+ 数据在名称/值对中
+ 数据由逗号分隔
+ 花括号保存对象
+ 方括号保存数组

------

## JSON 名称/值对

JSON 数据的书写格式是：名称/值对。

名称/值对包括字段名称（在双引号中），后面写一个冒号，然后是值：      

`"firstName" : "John"`

这很容易理解，等价于这条 JavaScript 语句：      

`firstName = "John"`

------

## JSON 值

JSON 值可以是：

+ 数字（整数或浮点数）
+ 字符串（在双引号中）
+ 逻辑值（true 或 false）
+ 数组（在方括号中）
+ 对象（在花括号中）
+ null

------

## JSON 对象

JSON 对象在花括号（{}）中书写：

对象可以包含多个名称/值对：        

`{ "firstName":"John" , "lastName":"Doe" }`

这一点也容易理解，与这条 JavaScript 语句等价：        
```
firstName = "John"       
lastName = "Doe"
```


------

## JSON 数组

JSON 数组在方括号中书写：

数组可包含多个对象：        
```json
{      
"employees": [        
{ "firstName":"John" , "lastName":"Doe" },        
{ "firstName":"Anna" , "lastName":"Smith" },        
{ "firstName":"Peter" , "lastName":"Jones" }        
]        
}
```
在上面的例子中，对象 "employees" 是包含三个对象的数组。每个对象代表一条关于某人（有姓和名）的记录。



------

## JSON 布尔值

JSON 布尔值可以是 true 或者 false：   
```
{ "flag":true }
```
------

## JSON null

JSON 可以设置 null 值：    
```
{ "runoob":null }
```
------

## JSON 使用 JavaScript 语法

因为 JSON 使用 JavaScript 语法，所以无需额外的软件就能处理 JavaScript 中的 JSON。

通过 JavaScript，您可以创建一个对象数组，并像这样进行赋值：

## 实例
```json
var employees = [
{ "firstName":"John" , "lastName":"Doe" },
{ "firstName":"Anna" , "lastName":"Smith" },
{ "firstName":"Peter" , "lastName": "Jones" }
];
```
可以像这样访问 JavaScript 对象数组中的第一项：

`employees[0].lastName;`

返回的内容是：

`Doe`

可以像这样修改数据：

`employees[0].firstName = "Jonatan";`


[尝试一下 »](https://www.w3cschool.cn/tryrun/showhtml/tryjson_objectarray)

 

在下面的章节，您将学到如何把 JSON 文本转换为 [JavaScript 对象](https://www.w3cschool.cn/javascript/js-objects.html)。

------

## JSON 文件

+ JSON 文件的文件类型是 ".json"
+ JSON 文本的 MIME 类型是 "application/json"

在下节内容中，我们将介绍如何使用JSON把文本转换为JavaScript对象。