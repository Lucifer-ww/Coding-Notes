#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct List
{
    int data;
    struct List *next;
}; //构建链表

void getInput(struct List *book)
{
    printf("输入数据：");
    scanf("%s", book->data);
}

void addData(struct List **head)
{
    struct List *list, *temp;
    list = (struct List *)malloc(sizeof(struct List));
    //动态分配内存
    //检测内存是否分配失败
    if (list == NULL)
    {
        printf("内存分配失败了\n");
        exit(1);
    }

    getInput(list);

    if (*head != NULL)
    { //非空链表插入
        temp = *head;
        *head = list;
        list->next = temp;
    }
    else
    { //空链表插入
        *head = list;
        list->next = NULL;
    }
    return;
}

void printList(struct List * head)
{
    struct List * list;
    int count = 1;

    list = head; //将头指针给链表

    while (list != NULL)
    {
        printf("id:%d", count);
        printf("data:%d\n", list->data);
        list = list->next; //赋值为下一个节点
        count++; //计数器加一
    }
}

int main()
{
    struct List *head;
    head = NULL;
    addData(&head);
    addData(&head);
    addData(&head);
    printList(head);
    return 0;
}