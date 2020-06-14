##### Python中的字符串类型Unicode字符

```python
'Hello World'
"Hello World"
'\u0048\u0065\u006c\u006c\u006f\u0020\u0057\u006f\u0072\u006c\uoo64'
"\u0048\u0065\u006c\u006c\u006f\u0020\u0057\u006f\u0072\u006c\uoo64"
```



​	Python中的字符不同于c++字符，Python使用Unicode编码，所以字符串可以包含中文等亚洲字符。

代码第①行和第②行的字符串使用Unicode编码表示的字符串，事实上它表示的也是Hello World字符串，

可通过print（）函数将Unicode编码表示的字符串输出到控制台上，就会看到Hello World字符串。

Python Shell运行实例：

```python
>>>s = 'Hello World'
>>>print(s)
Hello World
>>>s = "Hello World"
>>>print(s)
Hello World
>>>s = '\u0048\u0065\u006c\u006c\u006f\u0020\u0057\u006f\u0072\u006c\uoo64'
>>>print(s)
Hello World
>>>s = "\u0048\u0065\u006c\u006c\u006f\u0020\u0057\u006f\u0072\u006c\uoo64"
>>>print(s)
Hello World
```

