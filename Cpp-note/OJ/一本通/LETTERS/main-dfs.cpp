#include <iostream>
using namespace std;
int b[1001] = {0};           //用来判断字母有没有被使用
int c[1001] = {-1, 1, 0, 0}; //带动x的位置变化
int d[1001] = {0, 0, -1, 1}; //带动y的位置变化
char a[1001][1001];
int r, s, maxx = 0;
void search(int, int, int);
int main()
{
    cin >> r >> s;
    for (int i = 0; i < r; i++)
        for (int j = 0; j < s; j++)
            cin >> a[i][j];
    b[a[0][0] - 'A'] = 1;
    search(0, 0, 1); //从第一个字母开始搜索
    cout << maxx << endl;
    return 0;
}
void search(int x, int y, int k)  // k是步数
{
    if (x < 0 || x >= r || y < 0 || y >= s)
        return; // 越界检测
    if (k >= maxx)
        maxx = k;
    for (int i = 0; i <= 3; i++)
    {
        int nx = x + c[i], ny = y + d[i];
        if (x + c[i] >= 0 && y + d[i] >= 0 && x + c[i] < r && y + d[i] < s && b[a[x + c[i]][y + d[i]] - 'A'] == 0) //数组位置合法且该字母没有被使用
        {
            b[a[x + c[i]][y + d[i]] - 'A'] = 1; //使该字母被禁用
            search(nx, ny, k + 1);              //搜索下一种字母
            // 到头返回时释放
            b[a[x + c[i]][y + d[i]] - 'A'] = 0; //让此位置上的字母可以被使用
        }
    }
}
