[toc]
### <font color = #ff0000 id="1">C++中Fstream库的一些用法</font>
&emsp;以前知道一些很基础的方法，比如就用`ifstream`和`ofstream`直接打开文件。但是还有一些打开方式。
#### 打开方法
实例：
```cpp
#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    ifstream fin;
    fin.open("test.txt");
    //打开一个名字叫test的文本文件
    ifstream in("test2.txt");
    return 0;
}
```
注意*istream*或者*ofstream*后面定义的时候，不一定非是*fin*，也可以是in、stream、coffee爱咋咋:smiley_cat:
上面是打开方法
下面看看输入方法
#### 输入方法与输出

##### <font color=#0099ff>输入</font>

1、test.txt文件
```txt
hello world
hello world
```
2、main.cpp文件
```cpp
#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main()
{
    ifstream fin(test.txt);
    string s1, s2;
    fin >> s1 >> s2; //输入两行
    cout << "s1 = " << s1 << "s2 = " << s2 << endl;
    fin.close(); //关闭输入
    return 0;
}
```
**注意：**输入的文件要和代码放在同一个文件夹里，要不然代码识别不出来，只能写具体位置。

**代码解析：**

1. 第7行打开了一个“test.txt”文件，并声明输入标识符为*fin*。
2. 第9行输入两个字符串，从文件输入，当然就是两个`hello world`。
3. 第11行是关闭文件，就代表不输入了，每次输入完都要关闭，最好是关闭。

##### <font color=#0099ff>输出</font>

输入用*ifstream*,代表<ins>in file stream</ins>，那么输出就是*ofstream*了呗，代表<ins>out file stream</ins>。

```CPP
#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    ofstream fout("test.txt");
    fout << "hello world" << endl;
    return 0;
}
```

然后同文件夹里出现了一个*test.txt*文件，打开

```txt
hello world
```

这就是把字符串输出进文件，数字、字符、浮点也可以。

#### 常见的打开模式:

ios::in–打开一个可读取文件
ios::out–打开一个可写入文件
ios:binary –以二进制的形式打开一个文件。
ios::app –写入的所有数据将被追加到文件的末尾
ios::trunk –删除文件原来已存在的内容
ios::nocreate –如果要打开的文件并不存在，那么以此叁数调用open函数将无法进行。
ios:noreplece –如果要打开的文件已存在，试图用open函数打开时将返回一个错误。

```cpp
#include <iostream>
#include <fstream>

using namespace std;

int main(){
    fstream fp("test.txt",ios::in | ios::out);
    if(!fp){
        cout << "open file failed" << endl;
        return 0;
    }
    fp << "WelcomeToMyHome!";
    static char str[100];
    fp.seekg(ios::beg);//使文件指针指向文件头 
    fp >> str;
    cout << str << endl;
    fp.close();
    return 0;
} 
```

<img src="https://img-blog.csdn.net/20180602192350836?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3lhbmcxMDU2MA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt="img" style="zoom: 80%;" />