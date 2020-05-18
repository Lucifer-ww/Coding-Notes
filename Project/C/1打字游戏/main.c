#include <stdio.h>
#include <string.h>
#include <time.h>
#include <conio.h>
#include <stdlib.h>

//输出字符串并且打印，同时统计所用时间和正确率
void userWord(char *str, int len)
{
    int i = 0;
    char ch;
    double T_len = 0.0; //用来记录正确输入的的字符数
    time_t start_time, end_time;
    printf("\t本次游戏所列字符串为：\n");
    printf("%s\n", str);
    start_time = time(NULL); //起始时间
    for (; i < len - 1; i++)
    {
        ch = _getch();
        if (*(str + i) == ch)
        {
            printf("%c", ch);
            ++T_len;
        }
        else
            printf("%c", '_');
    }
    end_time = time(NULL); //终止时间
    putchar('\n');
    printf("\t总共花了：%ds\n", end_time - start_time);
    printf("\t正确率：%.2lf%%\n", (T_len / len) * 100.0);
    //需要头文件#include <time.h>
}

int main(void)
{

    char buf0[50];
    char num;
    int i, len;
    puts("\t-------------------------");
    puts("\t**                    **");
    puts("\t**欢迎使用打字小游戏  **");
    puts("\t-------------------------");
    len = sizeof(buf0);
    srand((unsigned int)time(NULL));
    memset(buf0, 0, sizeof(buf0));
    for (i = 0; i < len - 1; i++) //0----
    {
        num = 'a' + rand() % 26;
        buf0[i] = num;
    }

    printf("\t字符串中长度 = %d\n", len);
    userWord(buf0, len);
    puts("\t**                    **");
    puts("\t-------------------------");
    system("pause");
    return 0;
}