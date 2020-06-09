#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <windows.h>
#include <conio.h>
#include <time.h>
#include <cstdio>
const int H = 25; //地图的高
const int L = 80; //地图的长
int ifinitial = 1;
char GameMap[H + 2][L + 2];                                         //游戏地图
int time0;                                                          //初始时间
int timefinal;                                                      //结束时间
int key;                                                            //按键保存
int sum = 1, over = 0, speed = 0, stoppingtime = 0, speedlevel = 0; //蛇的长度, 游戏结束(自吃或碰墙)
int extrascore = 0;
int dx[4] = {0, 0, -1, 1}; //左、右、上、下的方向
int dy[4] = {-1, 1, 0, 0};
int flagOfyn = 0;
struct Snake //蛇的每个节点的数据类型
{
    int x, y; //左边位置
    int now;  //保存当前节点的方向, 0,1,2,3分别为左右上下
} Snake[H * L];
const int ix = 2, iy = 2;
const char Shead = '@';  //蛇头
const char Sbody = '#';  //蛇身
const char Sfood = '*';  //食物
const char Snode = ' ';  //' '在地图上标示为空
const char Sfood2 = '!'; //2分食物
int Home();
void Initial();                                       //地图的初始化
void Create_Food();                                   //在地图上随机产生食物
void Show();                                          //刷新显示地图
void Button();                                        //取出按键,并判断方向
void Move();                                          //蛇的移动
void Check_Border();                                  //检查蛇头是否越界
void Check_Head(int x, int y);                        //检查蛇头移动后的位置情况
void drawFrame(COORD a, COORD b, char row, char col); //画框
void drawFrame(int x1, int y1, int x2, int y2, char row, char col);
void HideCursor(); //隐藏光标
void drawRow(int y, int x1, int x2, char ch);
void drawCol(int y, int x1, int x2, char ch);
void setxy(HANDLE hOut, int x, int y);         //设置光标位置
HANDLE hOut = GetStdHandle(STD_OUTPUT_HANDLE); //定义显示器句柄变量
int main()
{
    HideCursor();
X:
    speedlevel = Home();
    Initial();
    Show();

    if (flagOfyn == 89 || flagOfyn == 121)
        goto X;
    else if (flagOfyn == 78 || flagOfyn == 110)
    {
        printf("/n/n/n");
        system("pause");
    }
    return 0;
}
int Home()
{
    system("cls");
    system("color 2E");
    HideCursor();
    /*	drawFrame(0, 0, 48, 24, '=', '|');//    draw map frame;  
    drawFrame(49, 0, 79, 4, '-', '|');//        draw output frame  
    drawFrame(49, 4, 79, 9, '-', '|');//        draw score frame  
    drawFrame(49, 9, 79, 20, '-', '|');//   draw operate frame  
    drawFrame(49, 20, 79, 24, '-', '|');//  draw other message frame*/
    setxy(hOut, 50, 1);
    printf("Snakes eating game");
    drawRow(3, 0, 119, '-');
    drawRow(5, 0, 119, '-');
    setxy(hOut, 48, 4);
    printf("up and down and enter");
    setxy(hOut, 35, 10);
    printf("1. level：low");
    setxy(hOut, 35, 12);
    printf("2. level：middle");
    setxy(hOut, 35, 14);
    printf("3. level：high");
    drawRow(20, 0, 119, '-');
    drawRow(22, 0, 119, '-');
    setxy(hOut, 67, 11);
    printf("low level：");
    setxy(hOut, 71, 13);
    printf("low speed");
    setxy(hOut, 44, 21);
    printf("制作人：Platonic hacker");
    int j = 10;
    setxy(hOut, 32, j);
    printf(">>");

    //drawFrame(45, 9, 79, 17, '=', '|');

    while (1)
    {
        if (_kbhit())
        {
            char x = _getch();
            switch (x)
            {
            case 72:
            {
                if (j == 14)
                {
                    setxy(hOut, 32, j);
                    printf("　");
                    j = 12;
                    setxy(hOut, 32, j);
                    printf(">>");
                    setxy(hOut, 71, 13);
                    printf("　　　　　　　　　　　　");
                    setxy(hOut, 67, 11);
                    printf("　　　　　　　　　　　　　　");
                    setxy(hOut, 67, 11);
                    printf("middle level:");
                    setxy(hOut, 71, 13);
                    printf("middle speed");
                    break;
                }
                else if (j == 12)
                {
                    setxy(hOut, 32, j);
                    printf("　");
                    j = 10;
                    setxy(hOut, 32, j);
                    printf(">>");
                    setxy(hOut, 71, 13);
                    printf("　　　　　　　　　　　　");
                    setxy(hOut, 67, 11);
                    printf("　　　　　　　　　　　　　　");
                    setxy(hOut, 67, 11);
                    printf("low level:");
                    setxy(hOut, 71, 13);
                    printf("low speed");
                    break;
                }
                else
                    break;
            }

            case 80:
            {
                if (j == 10)
                {
                    setxy(hOut, 32, j);
                    printf("　");
                    j = 12;
                    setxy(hOut, 32, j);
                    printf(">>");
                    setxy(hOut, 71, 13);
                    printf("　　　　　　　　　　　　　　");
                    setxy(hOut, 67, 11);
                    printf("　　　　　　　　　　　　　　");
                    setxy(hOut, 67, 11);
                    printf("middle level：");
                    setxy(hOut, 71, 13);
                    printf("middle speed");
                    break;
                }

                else if (j == 12)
                {
                    setxy(hOut, 32, j);
                    printf("　");
                    j = 14;
                    setxy(hOut, 32, j);
                    printf(">>");
                    setxy(hOut, 71, 13);
                    printf("　　　　　　　　　　　　　　");
                    setxy(hOut, 67, 11);
                    printf("　　　　　　　　　　　　　　");
                    setxy(hOut, 67, 11);
                    printf("high level：");
                    setxy(hOut, 71, 13);
                    printf("high speed");
                    break;
                }
                else
                    break;
            }
            case 13:
            {
                if (j == 10)
                    return 1;
                else if (j == 12)
                    return 2;
                else
                    return 3;
            }
            }
        }
    }
}

void Initial() //地图的初始化
{

    stoppingtime = 0;
    ifinitial = 1; //时间每次初始
    system("cls");
    sum = 1, over = 0, extrascore = 0;
    int i, j;
    int hx, hy;
    system("title Gluttonous Snake");      //控制台的标题
    memset(GameMap, ' ', sizeof(GameMap)); //初始化地图全部为空' '
    for (i = 0; i < H + 2; i++)
    {
        GameMap[i][0] = '|';
        GameMap[i][L + 1] = '|';
    }
    for (j = 0; j < L + 2; j++)
    {
        GameMap[0][j] = '_';
        GameMap[H + 1][j] = '-';
    }

    srand(time(0));      //随机种子
    hx = rand() % H + 1; //产生蛇头
    hy = rand() % L + 1;
    GameMap[hx][hy] = Shead;
    Snake[0].x = hx;
    Snake[0].y = hy;
    Snake[0].now = -1;
    for (int i = 0; i < 25; i++)
    { //随机产生25个食物
        Create_Food();
    }
    for (i = 0; i < H + 2; i++) //地图显示
    {
        for (j = 0; j < L + 2; j++)
            if (GameMap[i][j] != ' ')
            {
                setxy(hOut, j + ix, i + iy);
                printf("%c", GameMap[i][j]);
            }

        printf("\n");
    }
    drawRow(2, 84, 113, '_');
    drawRow(9, 84, 113, '-');
    drawRow(28, 84, 113, '-');
    drawCol(113, 3, 27, '|');
    setxy(hOut, 85, 3);
    printf("speedlevel is %d", speedlevel);
    setxy(hOut, 85, 4);
    printf("your score is 0");
    setxy(hOut, 85, 5);
    printf("the time you have survived:");
    setxy(hOut, 89, 7);
    printf("0  minutes 0  seconds");
    setxy(hOut, 85, 10);
    printf("Made by Thomas");
    setxy(hOut, 85, 12);
    printf("click any direction button");
    setxy(hOut, 85, 13);
    printf("to start the game");
    getch();  //先接受一个按键,使蛇开始往该方向走
    Button(); //取出按键,并判断方向
}
void Create_Food() //在地图上随机产生食物
{
    int fx, fy, foodlevel, x;

    while (1)
    {
        foodlevel = rand() % 10;
        fx = rand() % H + 1;
        fy = rand() % L + 1;

        if (GameMap[fx][fy] == ' ') //不能出现在蛇所占有的位置
        {
            if (foodlevel >= 3)
            {
                GameMap[fx][fy] = Sfood;
                break;
            }
            else
            {
                GameMap[fx][fy] = Sfood2;
                break;
            }
        }
    }
}
void Show() //刷新显示地图
{
    int i = 0, j = 0, speed = 0;
    flagOfyn = 0;
    if (speedlevel == 1)
        speed = 100; //设置速度
    else if (speedlevel == 2)
        speed = 50;
    else if (speedlevel == 3)
        speed = 10;

    if (ifinitial == 1)
    {
        ifinitial = 0;
        time0 = time(0); //设置初始时间
    }
    int ifchange = 0;
    int leveltime = 0;
    int leveltime0 = time0;
    while (1)
    {
        leveltime = time(0) - leveltime0;
        if (speedlevel == 3)
        {
            if (Snake[0].now == 2 || Snake[0].now == 3)
                speed = 20;
            else if (Snake[0].now == 0 || Snake[0].now == 1)
                speed = 10;
        }
        else if (speedlevel == 2)
        {
            if (Snake[0].now == 2 || Snake[0].now == 3)
                speed = 100;
            else if (Snake[0].now == 0 || Snake[0].now == 1)
                speed = 50;
        }
        else if (speedlevel == 1)
        {
            if (Snake[0].now == 2 || Snake[0].now == 3)
                speed = 200;
            else if (Snake[0].now == 0 || Snake[0].now == 1)
                speed = 100;
        }

        Sleep(speed); //延迟半秒(1000为1s),即每speed秒刷新一次地图
        Button();     //先判断按键在移动
        Move();
        int score = sum + extrascore - 1;
        timefinal = time(0);
        if (over) //自吃或碰墙即游戏结束
        {
            system("cls");
            drawFrame(33, 7, 83, 20, '=', '|');
            setxy(hOut, 54, 9);
            printf("Game Over");
            setxy(hOut, 52, 12);
            printf("Your score:%d", score);
            setxy(hOut, 43, 16);
            printf(" Do you want to play again(y/n)");
            setxy(hOut, 37, 18);
            printf("the time you survive: %d minutes %d seconds", (timefinal - time0 - stoppingtime) / 60, (timefinal - time0 - stoppingtime) % 60);
            while (flagOfyn != 89 && flagOfyn != 121 && flagOfyn != 78 && flagOfyn != 110)
                flagOfyn = getch();
            break;
        }

        setxy(hOut, 99, 4);
        printf("%d", score);
        setxy(hOut, 100, 7);
        printf("  ");
        setxy(hOut, 100, 7);
        printf("%d", (timefinal - time0 - stoppingtime) % 60);
        setxy(hOut, 89, 7);
        printf("%d", (timefinal - time0 - stoppingtime) / 60);
        setxy(hOut, 99, 3);
        printf("%d", speedlevel);
        for (i = 1; i < H + 1; i++)
        {
            for (j = 1; j < L + 1; j++)
                if (GameMap[i][j] == '#' || GameMap[i][j] == '-' || GameMap[i][j] == '_' || GameMap[i][j] == '|' || GameMap[i][j] == '*' || GameMap[i][j] == '@' || GameMap[i][j] == '!' || GameMap[i + 1][j] == '#' && GameMap[i - 1][j] != '#' && GameMap[i][j + 1] != '#' && GameMap[i][j - 1] != '#' || GameMap[i - 1][j] == '#' && GameMap[i + 1][j] != '#' && GameMap[i][j + 1] != '#' && GameMap[i][j - 1] != '#' || GameMap[i][j + 1] == '#' && GameMap[i - 1][j] != '#' && GameMap[i + 1][j] != '#' && GameMap[i][j - 1] != '#' || GameMap[i][j - 1] == '#' && GameMap[i + 1][j] != '#' && GameMap[i - 1][j] != '#' && GameMap[i][j + 1] != '#' || GameMap[i][j] == ' ' && GameMap[i + 1][j] == '@' && GameMap[i + 2][j] != '#' || GameMap[i][j] == ' ' && GameMap[i - 1][j] == '@' && GameMap[i - 2][j] != '#' || GameMap[i][j] == ' ' && GameMap[i][j - 1] == '@' && GameMap[i][j - 2] != '#' || GameMap[i][j] == ' ' && GameMap[i][j + 1] == '@' && GameMap[i][j + 2] != '#')
                { //此处仅为判断是否是蛇尾之后的那个空格，如果是则刷新
                    setxy(hOut, j + ix, i + iy);
                    if (GameMap[i][j] == '@' || GameMap[i][j] == '#')
                        printf("%c", GameMap[i][j]);
                    else
                        printf("%c", GameMap[i][j]);
                }
            printf("\n");
        }
        if (leveltime >= 60 && speedlevel != 3)
        {
            speedlevel++;
            leveltime = 0;
            leveltime0 += 60;
        }
    }
}
void Button() //取出按键,并判断方向
{
    if (kbhit() != 0) //检查当前是否有键盘输入，若有则返回一个非0值，否则返回0
    {
        while (kbhit() != 0) //可能存在多个按键,要全部取完,以最后一个为主
            key = getch();   //将按键从控制台中取出并保存到key中
        switch (key)
        { //左
        case 75:
            if (Snake[0].now != 1)
                Snake[0].now = 0;
            break;
        //右
        case 77:
            if (Snake[0].now != 0)
                Snake[0].now = 1;
            break;
        //上
        case 72:
            if (Snake[0].now != 3)
                Snake[0].now = 2;
            break;
        //下
        case 80:
            if (Snake[0].now != 2)
                Snake[0].now = 3;
            break;
        case 27:
            over = 1;
            break;
        case 32:
            int stoptime0 = time(0);
            while (getch() != 32)
            {
                Sleep(200);
            }
            stoppingtime += time(0) - stoptime0;
            break;
        }
    }
}
void Move() //蛇的移动
{
    int i, x, y;
    int t = sum; //保存当前蛇的长度
    //记录当前蛇头的位置,并设置为空,蛇头先移动
    x = Snake[0].x;
    y = Snake[0].y;
    GameMap[x][y] = ' ';
    Snake[0].x = Snake[0].x + dx[Snake[0].now];
    Snake[0].y = Snake[0].y + dy[Snake[0].now];
    Check_Border();               //蛇头是否越界
    Check_Head(x, y);             //蛇头移动后的位置情况,参数为: 蛇头的开始位置
    if (sum == t)                 //未吃到食物即蛇身移动哦
        for (i = 1; i < sum; i++) //要从蛇尾节点向前移动哦,前一个节点作为参照
        {
            if (i == 1) //尾节点设置为空再移动
                GameMap[Snake[i].x][Snake[i].y] = ' ';
            if (i == sum - 1) //为蛇头后面的蛇身节点,特殊处理
            {
                Snake[i].x = x;
                Snake[i].y = y;
                Snake[i].now = Snake[0].now;
            }
            else //其他蛇身即走到前一个蛇身位置
            {
                Snake[i].x = Snake[i + 1].x;
                Snake[i].y = Snake[i + 1].y;
                Snake[i].now = Snake[i + 1].now;
            }
            GameMap[Snake[i].x][Snake[i].y] = '#'; //移动后要置为'#'蛇身
        }
}
void Check_Border() //检查蛇头是否越界
{
    if (Snake[0].x < 1 || Snake[0].x >= H + 2 || Snake[0].y < 1 || Snake[0].y >= L + 2)
        over = 1;
}
void Check_Head(int x, int y) //检查蛇头移动后的位置情况
{

    if (GameMap[Snake[0].x][Snake[0].y] == ' ') //为空
        GameMap[Snake[0].x][Snake[0].y] = '@';
    else if (GameMap[Snake[0].x][Snake[0].y] == '*') //为食物
    {
        GameMap[Snake[0].x][Snake[0].y] = '@';
        Snake[sum].x = x; //新增加的蛇身为蛇头后面的那个
        Snake[sum].y = y;
        Snake[sum].now = Snake[0].now;
        GameMap[Snake[sum].x][Snake[sum].y] = '#';
        sum += speedlevel;
        Create_Food(); //食物吃完了马上再产生一个食物
    }
    else if (GameMap[Snake[0].x][Snake[0].y] == '!') //为食物2
    {
        Create_Food();
        GameMap[Snake[0].x][Snake[0].y] = '@';
        Snake[sum].x = x; //新增加的蛇身为蛇头后面的那个
        Snake[sum].y = y;
        Snake[sum].now = Snake[0].now;
        GameMap[Snake[sum].x][Snake[sum].y] = '#';
        sum += speedlevel;
        extrascore += speedlevel;
        //食物吃完了马上再产生一个食物
    }

    else
        over = 1;
}
void drawFrame(COORD a, COORD b, char row, char col)
{
    drawRow(a.Y, a.X + 1, b.X - 1, row);
    drawRow(b.Y, a.X + 1, b.X - 1, row);
    drawCol(a.X, a.Y + 1, b.Y - 1, col);
    drawCol(b.X, a.Y + 1, b.Y - 1, col);
}
void drawFrame(int x1, int y1, int x2, int y2, char row, char col)
{
    COORD a = {x1, y1};
    COORD b = {x2, y2};
    drawFrame(a, b, row, col);
}
void HideCursor()
{
    CONSOLE_CURSOR_INFO cursor_info = {1, 0};
    SetConsoleCursorInfo(GetStdHandle(STD_OUTPUT_HANDLE), &cursor_info);
}
void setxy(HANDLE hOut, int x, int y)
{
    COORD pos;
    pos.X = x; //横坐标
    pos.Y = y; //纵坐标
    SetConsoleCursorPosition(hOut, pos);
}
void drawRow(int y, int x1, int x2, char ch)
{
    setxy(hOut, x1, y);
    for (int i = 0; i <= (x2 - x1); i++)
        printf("%c", ch);
}
void drawCol(int x, int y1, int y2, char ch)
{
    int y = y1;
    while (y != y2 + 1)
    {
        setxy(hOut, x, y);
        printf("%c", ch);
        y++;
    }
}
