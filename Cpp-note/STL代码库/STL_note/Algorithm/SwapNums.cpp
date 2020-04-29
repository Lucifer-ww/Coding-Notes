#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
    int a1 = 2, b1 = 3;
	swap(a1, b1);
    cout << a1 << " " << b1 << endl;
    int nums[4] = {0, 1, 2, 3};
    swap(nums[0], nums[3]);
    for (int i = 0; i < 4; i++)
        cout << nums[i] << " ";
    cout << endl;
    return 0;
}