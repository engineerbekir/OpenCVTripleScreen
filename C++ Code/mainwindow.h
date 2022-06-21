#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include "mythread.h"
#include <QMainWindow>
#include <QDebug>
#include <QThread>
#include <iostream>
#include <QImage>
#include <QPixmap>
#include <QStringList>
#include <QLabel>
#include <QLineEdit>
#include <QFileDialog>

#include "opencv2/opencv.hpp"
#include "opencv2/highgui/highgui.hpp"


using namespace cv;

using namespace std;

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

    MyThread* Thread_1 ;
    MyThread* Thread_2 ;
    MyThread* Thread_3 ;

    QFileDialog *fileDlg;

    void LabelPixmap(cv::Mat,int);
    QLabel** labels;
    QLineEdit** LineEdit;

    void OpenFileDialog(int);

private slots:


    void on_startButton_1_toggled(bool checked);
    void on_SearchButton_1_clicked();

    void on_startButton_2_toggled(bool checked);
    void on_SearchButton_2_clicked();

    void on_startButton_3_toggled(bool checked);
    void on_SearchButton_3_clicked();

    void on_toolButton_restore_clicked();

public slots:

    void onNumberChanged_1(cv::Mat);
    void onNumberChanged_2(cv::Mat);
    void onNumberChanged_3(cv::Mat);

private:
    int count = 0;
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H
