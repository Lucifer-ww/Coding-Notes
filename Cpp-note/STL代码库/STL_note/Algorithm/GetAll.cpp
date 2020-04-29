#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
int main()
{
    int a, b;
    cin >> a >> b;
    cout << max(a, b) << endl;
    cout << min(a, b) << endl;
    cout << abs(a - b) << endl;
    cout << "-----" << endl;
    vector<int>v;
    v.push_back(10);
    v.push_back(20);
    v.push_back(30);
    cout << *max_element(v.begin(), v.end()) << endl;
    
    int a1 = 2, b1 = 3;
	swap(a1, b1);
    cout << a1 << " " << b1 << endl;
    int nums[4] = {0, 1, 2, 3};
    swap(nums[0], nums[3]);
    for (int i = 0; i < 4; i++)
        cout << nums[i] << " ";
    cout << endl;

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