#ifndef MYPUSHBUTTON_H
#define MYPUSHBUTTON_H

#include <QPushButton>

class myPushButton : public QWidget
{
    Q_OBJECT
public:
    explicit myPushButton(QWidget *parent = nullptr);

    ~myPushButton();
signals:

};

#endif // MYPUSHBUTTON_H
