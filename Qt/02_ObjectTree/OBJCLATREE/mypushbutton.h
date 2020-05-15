#ifndef MYPUSHBUTTON_H
#define MYPUSHBUTTON_H

#include <QPushButton>

class myPushButton : public QWidget
{
    Q_OBJECT
public:
    explicit myPushButton(QWidget *parent = nullptr);

signals:
    ~myPushButton();

};

#endif // MYPUSHBUTTON_H
