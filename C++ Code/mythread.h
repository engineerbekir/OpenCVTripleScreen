#ifndef MYTHREAD_H
#define MYTHREAD_H


#include <QThread>
#include <QObject>
#include <QDebug>
#include <iostream>

#include "opencv2/opencv.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"

using namespace cv;
using namespace std;


class MyThread : public QThread
{
    Q_OBJECT


private:
    bool flag = true;

public:
    Mat frame;
    explicit MyThread(QObject *parent = nullptr);
    void run();
    bool Stop();
    QString path;

signals:

    cv::Mat NumberChange(cv::Mat);
public slots:

};

#endif // MYTHREAD_H
