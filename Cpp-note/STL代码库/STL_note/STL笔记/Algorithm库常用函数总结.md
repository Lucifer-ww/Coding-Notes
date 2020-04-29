[toc]

# Algorithm库常用函数总结

可以去[cplusplus]("https://www.cplusplus.com")官方网站查询，地址<http://www.cplusplus.com/reference/algorithm/>

:cloud:algorithm是C++中Stl的标准模板库，&lt;algorithm>专门设计用于元素范围范围是可以通过迭代器或指针(例如数组或某些STL容器的实例)访问的任何对象序列。但是请注意，算法通过迭代器直接对这些值进行操作，不以任何方式影响任何可能的容器的结构(它从不影响容器的大小或存储分配)。

## Functions in &lt;algorithm>所有函数

:arrow_down_small:不想看可以跳过这一段列表，这里介绍Algorithm的所有操作，每个函数都有一个链接，点击即可到官网查看:arrow_down_small:

<a href=#demo>向下传送门</a>:arrow_left:

Non-modifying sequence operations:

+ [**all_of** ](http://www.cplusplus.com/reference/algorithm/all_of/)

    Test condition on all elements in range (function template )

+ [**any_of** ](http://www.cplusplus.com/reference/algorithm/any_of/)

    Test if any element in range fulfills condition (function template )

+ [**none_of** ](http://www.cplusplus.com/reference/algorithm/none_of/)

    Test if no elements fulfill condition (function template )

+ [**for_each**](http://www.cplusplus.com/reference/algorithm/for_each/)

    Apply function to range (function template )

+ [**find**](http://www.cplusplus.com/reference/algorithm/find/)

    Find value in range (function template )

+ [**find_if**](http://www.cplusplus.com/reference/algorithm/find_if/)

    Find element in range (function template )

+ [**find_if_not** ](http://www.cplusplus.com/reference/algorithm/find_if_not/)

    Find element in range (negative condition) (function template )

+ [**find_end**](http://www.cplusplus.com/reference/algorithm/find_end/)

    Find last subsequence in range (function template )

+ [**find_first_of**](http://www.cplusplus.com/reference/algorithm/find_first_of/)

    Find element from set in range (function template )

+ [**adjacent_find**](http://www.cplusplus.com/reference/algorithm/adjacent_find/)

    Find equal adjacent elements in range (function template )

+ [**count**](http://www.cplusplus.com/reference/algorithm/count/)

    Count appearances of value in range (function template )

+ [**count_if**](http://www.cplusplus.com/reference/algorithm/count_if/)

    Return number of elements in range satisfying condition (function template )

+ [**mismatch**](http://www.cplusplus.com/reference/algorithm/mismatch/)

    Return first position where two ranges differ (function template )

+ [**equal**](http://www.cplusplus.com/reference/algorithm/equal/)

    Test whether the elements in two ranges are equal (function template )

+ [**is_permutation** ](http://www.cplusplus.com/reference/algorithm/is_permutation/)

    Test whether range is permutation of another (function template )

+ [**search**](http://www.cplusplus.com/reference/algorithm/search/)

    Search range for subsequence (function template )

+ [**search_n**](http://www.cplusplus.com/reference/algorithm/search_n/)

    Search range for elements (function template )


**Modifying sequence operations**:

+ [**copy**](http://www.cplusplus.com/reference/algorithm/copy/)

    Copy range of elements (function template )

+ [**copy_n** ](http://www.cplusplus.com/reference/algorithm/copy_n/)

    Copy elements (function template )

+ [**copy_if** ](http://www.cplusplus.com/reference/algorithm/copy_if/)

    Copy certain elements of range (function template )

+ [**copy_backward**](http://www.cplusplus.com/reference/algorithm/copy_backward/)

    Copy range of elements backward (function template )

+ [**move** ](http://www.cplusplus.com/reference/algorithm/move/)

    Move range of elements (function template )

+ [**move_backward** ](http://www.cplusplus.com/reference/algorithm/move_backward/)

    Move range of elements backward (function template )

+ [**swap**](http://www.cplusplus.com/reference/algorithm/swap/)

    Exchange values of two objects (function template )

+ [**swap_ranges**](http://www.cplusplus.com/reference/algorithm/swap_ranges/)

    Exchange values of two ranges (function template )

+ [**iter_swap**](http://www.cplusplus.com/reference/algorithm/iter_swap/)

    Exchange values of objects pointed to by two iterators (function template )

+ [**transform**](http://www.cplusplus.com/reference/algorithm/transform/)

    Transform range (function template )

+ [**replace**](http://www.cplusplus.com/reference/algorithm/replace/)

    Replace value in range (function template )

+ [**replace_if**](http://www.cplusplus.com/reference/algorithm/replace_if/)

    Replace values in range (function template )

+ [**replace_copy**](http://www.cplusplus.com/reference/algorithm/replace_copy/)

    Copy range replacing value (function template )

+ [**replace_copy_if**](http://www.cplusplus.com/reference/algorithm/replace_copy_if/)

    Copy range replacing value (function template )

+ [**fill**](http://www.cplusplus.com/reference/algorithm/fill/)

    Fill range with value (function template )

+ [**fill_n**](http://www.cplusplus.com/reference/algorithm/fill_n/)

    Fill sequence with value (function template )

+ [**generate**](http://www.cplusplus.com/reference/algorithm/generate/)

    Generate values for range with function (function template )

+ [**generate_n**](http://www.cplusplus.com/reference/algorithm/generate_n/)

    Generate values for sequence with function (function template )

+ [**remove**](http://www.cplusplus.com/reference/algorithm/remove/)

    Remove value from range (function template )

+ [**remove_if**](http://www.cplusplus.com/reference/algorithm/remove_if/)

    Remove elements from range (function template )

+ [**remove_copy**](http://www.cplusplus.com/reference/algorithm/remove_copy/)

    Copy range removing value (function template )

+ [**remove_copy_if**](http://www.cplusplus.com/reference/algorithm/remove_copy_if/)

    Copy range removing values (function template )

+ [**unique**](http://www.cplusplus.com/reference/algorithm/unique/)

    Remove consecutive duplicates in range (function template )

+ [**unique_copy**](http://www.cplusplus.com/reference/algorithm/unique_copy/)

    Copy range removing duplicates (function template )

+ [**reverse**](http://www.cplusplus.com/reference/algorithm/reverse/)

    Reverse range (function template )

+ [**reverse_copy**](http://www.cplusplus.com/reference/algorithm/reverse_copy/)

    Copy range reversed (function template )

+ [**rotate**](http://www.cplusplus.com/reference/algorithm/rotate/)

    Rotate left the elements in range (function template )

+ [**rotate_copy**](http://www.cplusplus.com/reference/algorithm/rotate_copy/)

    Copy range rotated left (function template )

+ [**random_shuffle**](http://www.cplusplus.com/reference/algorithm/random_shuffle/)

    Randomly rearrange elements in range (function template )

+ [**shuffle** ](http://www.cplusplus.com/reference/algorithm/shuffle/)

    Randomly rearrange elements in range using generator (function template )


**Partitions**:

+ [**is_partitioned** ](http://www.cplusplus.com/reference/algorithm/is_partitioned/)

    Test whether range is partitioned (function template )

+ [**partition**](http://www.cplusplus.com/reference/algorithm/partition/)

    Partition range in two (function template )

+ [**stable_partition**](http://www.cplusplus.com/reference/algorithm/stable_partition/)

    Partition range in two - stable ordering (function template )

+ [**partition_copy** ](http://www.cplusplus.com/reference/algorithm/partition_copy/)

    Partition range into two (function template )

+ [**partition_point** ](http://www.cplusplus.com/reference/algorithm/partition_point/)

    Get partition point (function template )


**Sorting**:

+ [**sort**](http://www.cplusplus.com/reference/algorithm/sort/)

    Sort elements in range (function template )

+ [**stable_sort**](http://www.cplusplus.com/reference/algorithm/stable_sort/)

    Sort elements preserving order of equivalents (function template )

+ [**partial_sort**](http://www.cplusplus.com/reference/algorithm/partial_sort/)

    Partially sort elements in range (function template )

+ [**partial_sort_copy**](http://www.cplusplus.com/reference/algorithm/partial_sort_copy/)

    Copy and partially sort range (function template )

+ [**is_sorted** ](http://www.cplusplus.com/reference/algorithm/is_sorted/)

    Check whether range is sorted (function template )

+ [**is_sorted_until** ](http://www.cplusplus.com/reference/algorithm/is_sorted_until/)

    Find first unsorted element in range (function template )

+ [**nth_element**](http://www.cplusplus.com/reference/algorithm/nth_element/)

    Sort element in range (function template )


**Binary search** (operating on partitioned/sorted ranges):

+ [**lower_bound**](http://www.cplusplus.com/reference/algorithm/lower_bound/)

    Return iterator to lower bound (function template )

+ [**upper_bound**](http://www.cplusplus.com/reference/algorithm/upper_bound/)

    Return iterator to upper bound (function template )

+ [**equal_range**](http://www.cplusplus.com/reference/algorithm/equal_range/)

    Get subrange of equal elements (function template )

+ [**binary_search**](http://www.cplusplus.com/reference/algorithm/binary_search/)

    Test if value exists in sorted sequence (function template )


**Merge** (operating on sorted ranges):

+ [**merge**](http://www.cplusplus.com/reference/algorithm/merge/)

    Merge sorted ranges (function template )

+ [**inplace_merge**](http://www.cplusplus.com/reference/algorithm/inplace_merge/)

    Merge consecutive sorted ranges (function template )

+ [**includes**](http://www.cplusplus.com/reference/algorithm/includes/)

    Test whether sorted range includes another sorted range (function template )

+ [**set_union**](http://www.cplusplus.com/reference/algorithm/set_union/)

    Union of two sorted ranges (function template )

+ [**set_intersection**](http://www.cplusplus.com/reference/algorithm/set_intersection/)

    Intersection of two sorted ranges (function template )

+ [**set_difference**](http://www.cplusplus.com/reference/algorithm/set_difference/)

    Difference of two sorted ranges (function template )

+ [**set_symmetric_difference**](http://www.cplusplus.com/reference/algorithm/set_symmetric_difference/)

    Symmetric difference of two sorted ranges (function template )


**Heap**:

+ [**push_heap**](http://www.cplusplus.com/reference/algorithm/push_heap/)

    Push element into heap range (function template )

+ [**pop_heap**](http://www.cplusplus.com/reference/algorithm/pop_heap/)

    Pop element from heap range (function template )

+ [**make_heap**](http://www.cplusplus.com/reference/algorithm/make_heap/)

    Make heap from range (function template )

+ [**sort_heap**](http://www.cplusplus.com/reference/algorithm/sort_heap/)

    Sort elements of heap (function template )

+ [**is_heap** ](http://www.cplusplus.com/reference/algorithm/is_heap/)

    Test if range is heap (function template )

+ [**is_heap_until** ](http://www.cplusplus.com/reference/algorithm/is_heap_until/)

    Find first element not in heap order (function template )


**Min/max**:

+ [**min**](http://www.cplusplus.com/reference/algorithm/min/)

    Return the smallest (function template )

+ [**max**](http://www.cplusplus.com/reference/algorithm/max/)

    Return the largest (function template )

+ [**minmax** ](http://www.cplusplus.com/reference/algorithm/minmax/)

    Return smallest and largest elements (function template )

+ [**min_element**](http://www.cplusplus.com/reference/algorithm/min_element/)

    Return smallest element in range (function template )

+ [**max_element**](http://www.cplusplus.com/reference/algorithm/max_element/)

    Return largest element in range (function template )

+ [**minmax_element** ](http://www.cplusplus.com/reference/algorithm/minmax_element/)

    Return smallest and largest elements in range (function template )


**Other**:

+ [**lexicographical_compare**](http://www.cplusplus.com/reference/algorithm/lexicographical_compare/)

    Lexicographical less-than comparison (function template )

+ [**next_permutation**](http://www.cplusplus.com/reference/algorithm/next_permutation/)

    Transform range to next permutation (function template )

+ [**prev_permutation**](http://www.cplusplus.com/reference/algorithm/prev_permutation/)

    Transform range to previous permutation (function template )
<p id=demo></p>
## 常用的函数

<p><big><font color=orangered>注意：给大家提供一个在线编译器。叫做C++ Shell。此编译器是cplusplus官网配套协作的编译器，方便大家看完文档写代码，给大家链接<a>http://cpp.sh/</a>很好用</font></big></p>

### 1、max()、min()、abs()比较数字

这个在math头文件也可以，<font color=red>浮点型的绝对值要用math的fabs</font>

```cpp
#include <iostream>
using namespace std;
int main()
{
    int a, b;
    cin >> a >> b;
    cout << max(a, b) << endl;
    cout << min(a, b) << endl;
    cout << abs(a - b) << endl;
    return 0;
}
```



### 2、&#42;max_element()、&#42;min_element()比较容器（数组、字符串等）

上面的max、min函数只能比较数字，如果比较<font color=red>数组等容器</font>怎么办，就用&#42;..._element()方法

```cpp
// min_element/max_element example
#include <iostream>     // std::cout
#include <algorithm>    // std::min_element, std::max_element

bool myfn(int i, int j) { return i<j; }

struct myclass {
  bool operator() (int i,int j) { return i<j; }
} myobj;

int main () {
  int myints[] = {3,7,2,5,6,4,9};

  // using default comparison:
  std::cout << "The smallest element is " << *std::min_element(myints,myints+7) << '\n';
  std::cout << "The largest element is "  << *std::max_element(myints,myints+7) << '\n';

  // using function myfn as comp:
  std::cout << "The smallest element is " << *std::min_element(myints,myints+7,myfn) << '\n';
  std::cout << "The largest element is "  << *std::max_element(myints,myints+7,myfn) << '\n';

  // using object myobj as comp:
  std::cout << "The smallest element is " << *std::min_element(myints,myints+7,myobj) << '\n';
  std::cout << "The largest element is "  << *std::max_element(myints,myints+7,myobj) << '\n';

  return 0;
}
```

运行结果

```
The smallest element is 2
The largest element is 9
The smallest element is 2
The largest element is 9
The smallest element is 2
The largest element is 9
```

注意，min_element和max_element要加星号&#42;，因为iterator迭代器，就加上就行了
下面是比较动态数组伪代码

```cpp
std::vector<int>v;
v.push_back(10);
v.push_back(20);
v.push_back(30);
std::cout << *max_element(v.begin(), v.end()) << std::endl;
```

### 3、swap()交换值

这个一般不用algorithm库也可以实现swap函数，但还是比较常用

```cpp
#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
    int a, b;
	swap(a, b);
    cout << a << " " << b << endl;
    int nums[4] = {0, 1, 2, 3};
    swap(nums[0], nums[3]);
    for (int i = 0; i < 3; i++)
        cout << nums[i] << " ";
    cout << endl;
    return 0;
}
```

### 4、reverse()翻转容器

reverse()函数可以将一个容器直接翻转，例如数组、动态数组和字符串等

```cpp
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
int main()
{
    vector<int>array;//动态数组
    for (int i = 0; i < 5; i++)
    {
        int t;
        cin >> t;
        array.push_back(t);
    }
    reverse(array.begin(), array.end());
    for (int i = 0; i < array.size(); i++)
        cout << array[i] << " ";
    cout << endl;
    cout << "--------" << endl;
    string str = "hello world";//字符串
    reverse(str.begin(), str.end());
    cout << str << endl;
    cout << "--------" << endl;
    int arr1[101]; //数组
    for (int i = 0; i < 5; i++)
    {
        cin >> arr1[i];
    }
    reverse(arr1, arr1 + 5);
    for (int i = 0; i < 5; i++)
    {
        cout << arr1[i] << " ";
    }
    cout << endl;
    return 0;
}
```

输出结果：

```
1 2 3 4 5
5 4 3 2 1
--------
dlrow olleh
--------
5 2 6 4 5
5 4 6 2 5
```

### 5、快速排序——sort函数

快速排序，时间超短！
实例：

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
    vector<int> sortv; //动态数组
    for (int i = 0; i < 5; i++)
    {
        int t;
        cin >> t;
        sortv.push_back(t);
    }
    sort(sortv.begin(), sortv.end());
    for (int i = 0; i < 5; i++)
    {
        cout << sortv[i] << endl;
    }
    //数组
    int sortnums[6];
    for (int i = 0; i < 5; i++)
        cin >> sortnums[i];
    sort(sortnums, sortnums + 5);
    for (int i = 0; i < 5; i++)
        cout << sortnums[i] << endl;
    //此sort是升序排序
    return 0;
}
```

运行结果：

```
1 5 4 3 8
1
3
4
5
8
1 5 6 4 8
1
4
5
6
8
```

怎么把sort函数改成降序呢？
在命名空间下方添加一个函数——cmp（名字任意）

```cpp
bool cmp(int a, int b)
{
    return a > b;
}
```

sort函数改成这样

```cpp
sort(v.begin(), v.end(), cmp);
```

就可以了。