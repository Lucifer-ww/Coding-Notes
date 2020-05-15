#include "mypushbutton.h"
#include <QDebug>

myPushButton::myPushButton(QWidget *parent) : QWidget(parent)
{
    qDebug() << "我的按钮类构造调用";
}

myPushButton::~myPushButton()
{
    qDebug() << "我的按钮类析构";
}
