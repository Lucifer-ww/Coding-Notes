#ifndef MYPUSHBUTTON_H
#define MYPUSHBUTTON_H

#include <QPushButton>

class myPushButton : public QWidget
{
public:
    explicit myPushButton(QWidget *parent = nullptr);

signals:
    myPushButton();
    ~myPushButton();

};

#endif // MYPUSHBUTTON_H
