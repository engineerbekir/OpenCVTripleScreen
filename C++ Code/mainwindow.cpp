#include "mainwindow.h"
#include "ui_mainwindow.h"


MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    labels = new QLabel* [3] {ui->labelImg_1,ui->labelImg_2,ui->labelImg_3};
    // Thread = new MyThread* [3];
    LineEdit = new QLineEdit* [3] {ui->lineEdit_1,ui->lineEdit_2,ui->lineEdit_3};

    fileDlg=new QFileDialog(this);

    this->count = count;

}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::onNumberChanged_1(cv::Mat Frame){
    LabelPixmap(Frame,0);
}

void MainWindow::onNumberChanged_2(cv::Mat Frame){
    LabelPixmap(Frame,1);
}
void MainWindow::onNumberChanged_3(cv::Mat Frame){
    LabelPixmap(Frame,2);
}



void MainWindow::OpenFileDialog(int ID){

    QString path= fileDlg->getOpenFileName(this,"Open an image","/home/Desktop", tr("MP4 file (*.mp4);;JPEG file (*.jpg);;JPEG file (*.jpg);;PNG file (*.png)"));
    LineEdit[ID]->setText(path); ;

}



void MainWindow::LabelPixmap(cv::Mat Frame,int ID)
{

    cv::Mat converted;
    cv::cvtColor(Frame, converted,  COLOR_BGR2RGB);
    QImage result = QImage((const unsigned char*)(converted.data),
                           converted.cols, converted.rows, QImage::Format_RGB888);
    labels[ID]->setPixmap(QPixmap::fromImage(result));
    labels[ID]->setAlignment(Qt::AlignCenter);
}


void MainWindow::on_startButton_1_toggled(bool checked)
{
    if (checked==true){
        QString Path = LineEdit[0]->text();

        Thread_1 = new MyThread (this);
        Thread_1->path=Path;
        connect(Thread_1,SIGNAL(NumberChange(cv::Mat)),this,SLOT(onNumberChanged_1(cv::Mat)));
        Thread_1->start();
    }
    else if(checked==false){
        Thread_1->Stop();
    }
}


void MainWindow::on_startButton_2_toggled(bool checked)
{
    if (checked==true){
        QString Path = LineEdit[1]->text();

        Thread_2 = new MyThread (this);
        Thread_2->path=Path;
        connect(Thread_2,SIGNAL(NumberChange(cv::Mat)),this,SLOT(onNumberChanged_2(cv::Mat)));
        Thread_2->start();
    }
    else if(checked==false){
        Thread_2->Stop();
    }

}

void MainWindow::on_startButton_3_toggled(bool checked)
{
    if (checked==true){
        QString Path = LineEdit[2]->text();

        Thread_3 = new MyThread (this);
        Thread_3->path=Path;
        connect(Thread_3,SIGNAL(NumberChange(cv::Mat)),this,SLOT(onNumberChanged_3(cv::Mat)));
        Thread_3->start();
    }
    else if(checked==false){
        Thread_3->Stop();

        labels[2]->setPixmap(QPixmap("/icons/icons8-no-camera-48.png"));

    }
}


void MainWindow::on_SearchButton_1_clicked()
{
    OpenFileDialog(0);
}


void MainWindow::on_SearchButton_2_clicked()
{
    OpenFileDialog(1);
}


void MainWindow::on_SearchButton_3_clicked()
{
    OpenFileDialog(2);
}




void MainWindow::on_toolButton_restore_clicked()
{
    if (this->count==0){

        this->showFullScreen();
        this->count+=1;

    }
    else if(this->count==1){

        this->showNormal();
        this->count=0;

    }


}

