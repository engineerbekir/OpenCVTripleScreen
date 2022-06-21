#include "mythread.h"
#include <QtCore>


MyThread::MyThread(QObject *parent)
    : QThread{parent}
{

    this->flag =flag;
}
void MyThread:: run()
{

    VideoCapture cap(path.toStdString());
    qDebug()<< path;
    //namedWindow("pencere",WINDOW_AUTOSIZE);
    while (true){
        try{
            QMutex mutex;
            mutex.lock();
            if (this->flag==false) break;
            mutex.unlock();
            if (!cap.isOpened())
            {
                cout << "Video file not loaded!" << endl;
                break;
            }
            else{

            cap.read(frame);
            resize(frame,frame,Size(420,320));

            emit NumberChange(frame);
            msleep(25);
            }
        }
        catch(QString hata){
            qDebug()<<hata;
        }
    }
}
bool MyThread::Stop()
{
    this->flag = false;

    return this->flag;
}
