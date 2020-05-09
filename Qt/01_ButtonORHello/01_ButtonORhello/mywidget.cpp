#include "mywidget.h"
#include "ui_mywidget.h"
#include <QPushButton>

myWidget::myWidget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::myWidget)
{

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

}

myWidget::~myWidget()
{
    delete ui;
}

