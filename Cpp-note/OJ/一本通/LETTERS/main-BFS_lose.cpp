// 3 6
// HFDFFB
// AJHGDH
// DGAGEH 

#include <iostream>
using namespace std;
struct note{  // 创建一个note结构体队列
    int x;  // X坐标
    int y;  // Y坐标
    int step; // 步数
};
int main()
{
    // 基础输入部分
    int width, height;
    cin >> width >> height;
    char matrix[25][25];
    for (int i = 0; i < width; i++)
    {
        for (int j = 0; j < height; j++)
        {
            cin >> matrix[i][j];
        }
    }
    //----------
    int next = {{0, 1},   // 向右
                {1, 0},   // 向下
                {0, -1},  // 向左
                {-1, 0}}; // 向上
    int head, tail;
    int book[1001] = {0};  // 和matrix是同一个地图
    int chrs[27] = {0};
    note que[1001];
    const int STARTX = 0, STARTY = 0;
    head = 0;
    tail = 0; // 队列初始化

    que[tail].x = 0;
    que[tail].y = 0;
    que[tail].step = 0;
    tail++;
    book[0][0] = 1;
    // 如果队列不为空遍历
    while (head < tail)
    {
        // 枚举4个方向
        for (int i = 0; i <= 3; i++)
        {
            // 拿出下一个点坐标
            int tx = que[head].x + next[i][0];
            int ty = que[head].y + next[i][1];
            // 越界探测
            if (tx < 0 || tx > height - 1 || ty < 0 || ty > width - 1)
                continue;
            if (chrs && book[])
        }
    }
    return 0;
}