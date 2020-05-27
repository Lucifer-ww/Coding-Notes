#include <stdio.h>
#include <string.h>
typedef struct DTC {
    int id;
    char *ac;
}jxx;
int main(void)
{
    #if 0
    jxx ch[101];
    char accp[101];
    int idx;
    scanf("%d", &idx);
    ch[0].id = idx;
    scanf("%s", accp);
    ch[0].ac = accp;
    printf("%d  %s\n", ch[0].id, ch[0].ac);
    delete[] &accp;
    printf("删除...%s，如果输出即代表未删除\n", accp);
    #endif
    char *test = new char[101];
    scanf("%s", test);
    printf("%s\n", test);
    //delete[]test; 在动态分配的情况下，delete[]可行
    memset(test, 0, sizeof(test));
    scanf("%s", test);
    printf("%s\n", test);

    char test2[101] = {"test strcpy and hello world!"};
    char test2_1[101] = {""};
    char test2_2[101] = {""};
    strcpy(test2_1, test2);
    strcpy(test2_2, "hhstrcpy");
    printf("test2:%s\ntest2_1:%s\ntest2_2:%s\n", test2, test2_1, test2_2);
}