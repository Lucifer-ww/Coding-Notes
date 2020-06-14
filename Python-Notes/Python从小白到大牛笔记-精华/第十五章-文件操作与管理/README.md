仓库：<https://github.com/Github-Programer/Coding-Notes/>
[这个笔记的位置]("https://github.com/Github-Programer/Coding-Notes/tree/master/Python-Notes/%E7%AC%AC%E5%8D%81%E4%BA%94%E7%AB%A0-%E6%96%87%E4%BB%B6%E6%93%8D%E4%BD%9C%E4%B8%8E%E7%AE%A1%E7%90%86")
这么长的文章怎么能不点赞呢？
### <font color=skyblue>:books:文件操作与管理目录</font>

+ 文件操作
+ 打开文件
    + file参数
        + mode参数
        + buffering参数
        + encoding参数和errors参数
        + newline参数
        + closfd和opener参数
    + 关闭文件
    + 文本文件读写
+ os模块
+ os模块函数文档

大家可以根据上面的目录，在博客右边目录中查找

### 打开文件

&emsp;文件对象可以通过open()函数获得。open()函数是Python内置函数，它屏蔽了创建文件对象的细节，使得创建文件对象变得简单。open函数语法如下：

```python
	open(file, node='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```

open有8个参数，其中`file`和`mode`最常用，其他很少使用

#### file参数

file参数是要打开的文件，可以是字符串或整数。如果file是字符串表示文件名，文件名可以是相对当前目录的路径，也可以是绝对路径里如果file是整数表示文件描述符，文件描述符指向一个已经打开的文件。

#### mode参数

设置文件打开模式，二进制文件要设置rb、wb、xb、ab，如果是文本文件需要设置rt、wt、xt、at，由于t是默认模式，所以可以省略为r、w、x、a。

<table border="1" width="100%" bordercolor=tomato>
    <tr><td><caption>文件打开方式</caption></td></tr>
	<tr align="center">
		<th>字符串</th>
        <th>说明</th>
	</tr>
    <tr>
        <td>r</td>
        <td>只读模式打开文件（默认）</td>
    </tr>
    <tr>
        <td>w</td>
        <td>写入模式打开文件，会<font color=red>覆盖</font>已经存在的文件</td>
    </tr>
    <tr>
        <td>x</td>
        <td>独占创建模式，文件不存在时创建并以写入模式打开，如果文件已存在则<font color=red>抛出异常</font></td>
    </tr>
    <tr>
        <td>a</td>
        <td>追加模式，如果文件存在则写入内容追加到文件末尾</td>
    </tr>
    <tr>
        <td>b</td>
        <td>二进制模式</td>
    </tr>
    <tr>
        <td>t</td>
        <td>文本模式（默认）</td>
    </tr>
    <tr>
        <td>+</td>
        <td>更新模式</td>
    </tr>
</table>


+必须与r、w、x或a组合使用来设置文件为读写模式

#### buffering参数

buffering函数是设置缓冲区，默认值为-1，目前不用知道。

#### encoding和errors参数

encoding参数是指定文件打开时的编码设置，errors参数是指定编码发生错误时的策略

#### newline参数

设置换行格式

#### closfd和opener参数

贼file参数为文件描述符时使用，不用管。

____

实例代码：

```python
# -*-coding: UTF-8 -*-
#!/usr/bin/python3

f = open('test.txt', 'w+')
f.write('World')

f = open('test.txt', 'r+')
f.write('Hello')

f = open('test.txt', 'a')
f.write(' ')

fname = r'E:\王一涵programThomas\王一涵PythonThomas\Python-Learned\第十五章-文件操作与管理\文件操作代码01\test.txt'
f = open(fname, 'a+')
f.write('World');
```

最后文件中的文档是：

```txt
Hello World
```

提示：文件路径中的`\`字符会转义，所以加上`r`可以定为原字符串，防止转义，或者改成`/`或`\\`都可以防止转义
例：原路径：`‘C:\Users\33924\Documents\test.txt'`，防止转义的方式有如下三种

+ `r'C:\Users\33924\Documents\test.txt'`
+ `‘C:\\Users\\33924\\Documents\\test.txt’`
+ `‘C:/Users/33924/Documents/test.txt’`

### 关闭文件

一定要记住这里，关闭文件很重要，当使用open()函数打开文件后，若不再使用文件应该调用文件对象的close()方法关闭文件，文件的操作往往会抛出异常，为了保证文件操作无论正常结束还是异常结束都能够关闭文件，调用close()方法应该放在异常处理的finally代码块中。

实例代码：

```python
# -*- coding: UTF-8 -*-
#!/usr/bin/python3

# 使用finally关闭文件
f_name = 'test.txt'
try:
    f = open(f_name)
except OSError as e:
    print('打开文件失败')
else:
    print('打开文件成功')
    try:
        content = f.read()
        print(content)
    except OSError as e:
        print('处理OSError异常')
    finally:
        f.close()

# 使用with as自动资源管理
with open(f_name, 'r') as f:
    content = f.read()
    print(content)
```

输出：

```txt
打开文件成功
hello world
hello world
```

文件内容（test.txt）

```txt
hello world
```

C++同样，打开之后一定要关闭，否则很容易混淆。

### 文本文件读写

文本文件读写的单位是字符，而且字符是有编码的，比如中文的编码就要用Unicode或GBK等

主要方法有以下几种

+ read(size=-1)：从文件中读取字符串，size限制最多读取的字符数，size=-1时没有限制
+ readline(size=-1)：读取到换行符或文件尾并返回单行字符串，size是限制，等于-1没有限制
+ readlines(hint=-1)：读取一个字符串列表，每一行是列表的一个单元，hint是限制几行，等于-1没有限制
+ write(s)：写入一个字符串s，并返回写入的字符数
+ writelines(lines)：向文件写入一个列表，不添加行分隔符
+ flush()：刷新写缓冲区

实例代码：

```python
# -*- coding: UTF-8 -*-
#!/usr/bin/python3

f_name = 'test.txt'

with open(f_name, 'r', encoding='UTF-8') as f:
    lines = f.readlines()
    print(lines)
    print('lines的类型是:', type(lines))
    copy_f_name = 'copy.txt'
    with open(copy_f_name, 'w', encoding='utf-8') as copy_f:
        copy_f.writelines(lines)
        print('文件复制成功')
```

输出：

```
['hello world\n', 'hello world\n', 'hello world']
lines的类型是: <class 'list'>
文件复制成功
```

test.txt文件：

```
hello world
hello world
hello world
```

copy.txt文件：

```
hello world
hello world
hello world
```

打开文件时需要指定文件编码，比如UTF-8

### os模块

Python对文件的操作是通过文件对象实现的，文件对象属于Python的io模块。如果通过Python程序管理文件或目录，如删除文件、修改文件名、创建目录、删除目录和遍历目录等，可以通过Python的os模块实现。
注：目录就是文件夹

常用函数：

+ os.rename(src, dst)：修改文件名，src是源文件，dst是目标文件，它们都可以是相对当前路径或绝对路径表示的文件
+ os.remove(path)：删除path所指的文件，如果path是目录，抛出异常<font color=red>OSError</font>
```py
# -*-coding: UTF-8 -*-
#!/usr/bin/python3
import os

os.rename(r"E:\王一涵programThomas\Coding-Notes\Python-Notes\第十五章-文件操作与管理\OS_Module\1.rename_remove\test.txt",
          r"E:\王一涵programThomas\Coding-Notes\Python-Notes\第十五章-文件操作与管理\OS_Module\1.rename_remove\last.txt")
'''
rename文档：
---
rename(src: _PathType, dst: _PathType, *, src_dir_fd: Optional[int]=..., dst_dir_fd: Optional[int]=...) -> None
param src: _PathType

Rename a file or directory.
If either src_dir_fd or dst_dir_fd is not None, it should be a file
descriptor open to a directory, and the respective path string (src or dst)
should be relative; the path will then be relative to that directory.
src_dir_fd and dst_dir_fd, may not be implemented on your platform.
If they are unavailable, using them will raise a NotImplementedError.
'''

os.remove(r'E:\王一涵programThomas\Coding-Notes\Python-Notes\第十五章-文件操作与管理\OS_Module\1.rename_remove\removeTEST.TXT')
'''
remove文档：
---
remove(path: _PathType, *, dir_fd: Optional[int]=...) -> None
param path: _PathType

Remove a file (same as unlink()).
If dir_fd is not None, it should be a file descriptor open to a directory,
and path should be relative; path will then be relative to that directory.
dir_fd may not be implemented on your platform.
If it is unavailable, using it will raise a NotImplementedError.
'''
```
+ os.mkdir(path)：经典的shell指令，创建文件夹，在path目录中，如果目录已存在，就会抛出异常<font color= red>FileExistsError</font>
+ os.rmdir(path)：删除path路径的目录，如果目录非空，抛出异常<font color=red>OSError</font>
```py
# -*- coding: UTF-8 -*-
#!/usr/bin/python3
import os

os.mkdir(
    r"E:\王一涵programThomas\Coding-Notes\Python-Notes\第十五章-文件操作与管理\OS_Module\2.mkdir_rmdir\MKDIR"
)
'''
mkdir:
---
mkdir(path: _PathType, mode: int=..., *, dir_fd: Optional[int]=...) -> None
param path: _PathType
Create a directory.
If dir_fd is not None, it should be a file descriptor open to a directory,
and path should be relative; path will then be relative to that directory.
dir_fd may not be implemented on your platform.
If it is unavailable, using it will raise a NotImplementedError.
The mode argument is ignored on Windows.
'''

os.rmdir(
    r"E:\王一涵programThomas\Coding-Notes\Python-Notes\第十五章-文件操作与管理\OS_Module\2.mkdir_rmdir\MKDIR"
)
'''
rmdir:
---
rmdir(path: _PathType, *, dir_fd: Optional[int]=...) -> None
param path: _PathType
Remove a directory.
If dir_fd is not None, it should be a file descriptor open to a directory,
and path should be relative; path will then be relative to that directory.
dir_fd may not be implemented on your platform.
If it is unavailable, using it will raise a NotImplementedError.
'''
```
+ os.walk(top)：遍历top所指的目录树，自顶向下遍历目录树，返回值是一个三元组（目录路径，目录名列表，文件名列表）
```py
# -*- coding: UTF-8 -*-
#!/usr/bin/python3
import os
f = open(r"E:\王一涵programThomas\Coding-Notes\Python-Notes\第十五章-文件操作与管理\OS_Module\3.walk\out\outPutOfWalk.log", 'w+', encoding='UTF-8')
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        f.write(os.path.join(root, name))
    for name in dirs:
        f.write(os.path.join(root, name))
```

实例代码全在文件夹中（OS_Module\...\**.py）
Github代码地址：<https://github.com/Github-Programer/Coding-Notes/tree/master/Python-Notes/%E7%AC%AC%E5%8D%81%E4%BA%94%E7%AB%A0-%E6%96%87%E4%BB%B6%E6%93%8D%E4%BD%9C%E4%B8%8E%E7%AE%A1%E7%90%86>

### os模块函数文档
+ rename文档：
rename(src: _PathType, dst: _PathType, *, src_dir_fd: Optional[int]=..., dst_dir_fd: Optional[int]=...) -> None
param src: _PathType
Rename a file or directory.
If either src_dir_fd or dst_dir_fd is not None, it should be a file
descriptor open to a directory, and the respective path string (src or dst)
should be relative; the path will then be relative to that directory.
src_dir_fd and dst_dir_fd, may not be implemented on your platform.
If they are unavailable, using them will raise a NotImplementedError.
+ remove文档：
remove(path: _PathType, *, dir_fd: Optional[int]=...) -> None
param path: _PathType
Remove a file (same as unlink()).
If dir_fd is not None, it should be a file descriptor open to a directory,
and path should be relative; path will then be relative to that directory.
dir_fd may not be implemented on your platform.
If it is unavailable, using it will raise a NotImplementedError.
+ mkdir文档
mkdir(path: _PathType, mode: int=..., *, dir_fd: Optional[int]=...) -> None
param path: _PathType
Create a directory.
If dir_fd is not None, it should be a file descriptor open to a directory,
and path should be relative; path will then be relative to that directory.
dir_fd may not be implemented on your platform.
If it is unavailable, using it will raise a NotImplementedError.
The mode argument is ignored on Windows.
+ rmdir文档：
rmdir(path: _PathType, *, dir_fd: Optional[int]=...) -> None
param path: _PathType
Remove a directory.
If dir_fd is not None, it should be a file descriptor open to a directory,
and path should be relative; path will then be relative to that directory.
dir_fd may not be implemented on your platform.
If it is unavailable, using it will raise a NotImplementedError.

____

参考书目：《Python从小白到大牛》——关东升著
参考文档：
1、<https://www.runoob.com/python/os-walk.html>
2、<https://www.runoob.com/python/os-listdir.html>
3、<https://blog.csdn.net/liangyuannao/article/details/8724686>
联系我：<Thomaswang1h@163.com>:beers:

如有问题请评论