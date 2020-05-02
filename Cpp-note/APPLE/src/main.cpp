#include <iostream>
#include <string>
#include <windows.h>
#include <fstream>
#include <vector>

using namespace std;

void gotoxy(unsigned char x, unsigned char y)
{
    //COORD是Windows API中定义的一种结构，表示一个字符在控制台屏幕上的坐标
    COORD cor;
    //句柄
    HANDLE hout;
    //设定我们要定位到的坐标
    cor.X = x;
    cor.Y = y;
    //GetStdHandle函数获取一个指向特定标准设备的句柄，包括标准输入，标准输出和标准错误。
    //STD_OUTPUT_HANDLE正是代表标准输出（也就是显示屏）的宏
    hout = GetStdHandle(STD_OUTPUT_HANDLE);
    //SetConsoleCursorPosition函数用于设置控制台光标的位置
    SetConsoleCursorPosition(hout, cor);
}

int main()
{
    ifstream fin("E:\\王一涵programThomas\\Coding-Notes\\Cpp-note\\APPLE\\file\\map.txt");
    char map[101][101];
    for (int i = 0; i < 20; i++)
        for (int j = 0; j < 50; j++)
            fin >> map[i][j];
    for (int i = 0; i < 20; i++)
        for (int j = 0; j < 50; j++)
            cout << map[i][j];

    system("pause");
    char startx = 20, starty = 25;
    gotoxy(startx, starty);
    cout << " ";
    gotoxy(startx, starty + 1);
    cout << "♀";
    system("pause");
    return 0;
}