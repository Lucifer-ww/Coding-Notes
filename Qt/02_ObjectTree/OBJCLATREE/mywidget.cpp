#include "mywidget.h"
#include "ui_mywidget.h"
#include <QPushButton>
#include <mypushbutton.h>

myWidget::myWidget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::myWidget)
{
    ui->setupUi(this);
    //创建一个按钮
    QPushButton * btn = new QPushButton;
    //显示按钮
    //btn->show();顶层弹出
    btn->setParent(this);
    btn->setText("第一个按钮");

    QPushButton * btn2 = new QPushButton("第二个按钮", this);
    //移动btn2
    btn2->move(100, 100);
    //setFixedSize

    setFixedSize(600, 400);

    //title

    setWindowTitle("hello Qt");


    //========================================
    //========================================
    //创建一个我自己的按钮
    myPushButton * mybtn = new myPushButton;
    mybtn -> move(300, 300);
    mybtn -> setParent(this);
}

myWidget::~myWidget()
{
    delete ui;
}

