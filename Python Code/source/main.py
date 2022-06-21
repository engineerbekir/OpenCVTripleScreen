import sys,cv2

sys.path.insert(1, './user_interface')
from MultiCam import Ui_MainWindow

from VideoThreding import VideoCapture # Video Threading Oparation Class

from PyQt5.QtWidgets import QMainWindow,QApplication,QFileDialog
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import pyqtSlot
import numpy as np
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore,QtGui
import time

class MultiCam(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
        self.CamId=0



        self.ui.toolButton_exit.clicked.connect(self.close)
      
        #Window restore

        self.ui.toolButton_restore.clicked.connect(self.Restore)
        self.count=0

        # Button Status

        self.Play_Pause_B1=None
        self.Play_Pause_B2=None
        self.Play_Pause_B3=None

        self.Play_Pause_ButtonStatus=[self.Play_Pause_B1,self.Play_Pause_B2,self.Play_Pause_B3]

        # Video MultiThread

        self.VideoThread_1=None
        self.VideoThread_2=None
        self.VideoThread_3=None


        self.VideoThread =[self.VideoThread_1,self.VideoThread_2,self.VideoThread_3]
        
        # Video Screens
        self.Screens = [self.ui.Screen_1,self.ui.Screen_2,self.ui.Screen_3]
        
        # Video Paths
        self.VideoPaths = [self.ui.lineEdit_1,self.ui.lineEdit_2,self.ui.lineEdit_3,]     

        #Cam 1

        self.ui.SearchButton_1.clicked.connect(lambda x:self.SelectVideoPath(self.ui.SearchButton_1))
        self.ui.Button_Play_Pause_1.toggled['bool'].connect(self.Play_Pause_Screen_1)

        #Cam 2

        self.ui.SearchButton_2.clicked.connect(lambda x:self.SelectVideoPath(self.ui.SearchButton_2))
        self.ui.Button_Play_Pause_2.toggled['bool'].connect(self.Play_Pause_Screen_2)

        #Cam 3

        self.ui.SearchButton_3.clicked.connect(lambda x:self.SelectVideoPath(self.ui.SearchButton_3))
        self.ui.Button_Play_Pause_3.toggled['bool'].connect(self.Play_Pause_Screen_3) 

    @pyqtSlot(np.ndarray)  
    def Screen_1(self,Frame):
       
        rgb_Frame=Frame
        h, w ,ch = rgb_Frame.shape
        img = QImage(rgb_Frame, w, h, rgb_Frame.strides[0], QImage.Format_BGR888)
        self.ui.Screen_1.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.Screen_1.setPixmap(QPixmap.fromImage(img)) 
        
        if self.Play_Pause_B1==False:
            time.sleep(0.01)
            self.ui.Screen_1.setPixmap(QtGui.QPixmap(":/icons/icons8-no-camera-48.png"))

    @pyqtSlot(np.ndarray)  
    def Screen_2(self,Frame):

        rgb_Frame=Frame
        h, w ,ch = rgb_Frame.shape
        img = QImage(rgb_Frame, w, h, rgb_Frame.strides[0], QImage.Format_BGR888)
        self.ui.Screen_2.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.Screen_2.setPixmap(QPixmap.fromImage(img)) 
        
        if self.Play_Pause_B2==False:
            time.sleep(0.01)
            self.ui.Screen_2.setPixmap(QtGui.QPixmap(":/icons/icons8-no-camera-48.png"))  

    @pyqtSlot(np.ndarray)  
    def Screen_3(self,Frame):

        rgb_Frame=Frame
        h, w ,ch = rgb_Frame.shape
        img = QImage(rgb_Frame, w, h, rgb_Frame.strides[0], QImage.Format_BGR888)
        self.ui.Screen_3.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.Screen_3.setPixmap(QPixmap.fromImage(img)) 
        
        if self.Play_Pause_ButtonStatus[self.CamId]==False:
            time.sleep(0.01)
            self.ui.Screen_3.setPixmap(QtGui.QPixmap(":/icons/icons8-no-camera-48.png"))              

    
    def Play_Pause_Screen_1(self,State):
        self.CamId=0
        self.runThread(State)
    
    def Play_Pause_Screen_2(self,State):
        self.CamId=1
        self.runThread(State)
    
    def Play_Pause_Screen_3(self,State):
        self.CamId=2
        self.runThread(State)
   
    def runThread(self,st):
        Screens=[self.Screen_1,self.Screen_2,self.Screen_3]
        if st==True:  

            self.Play_Pause_ButtonStatus[self.CamId]=True
             
            Path = self.VideoPaths[self.CamId].text()
            self.LogPrint("CamID :",self.CamId,"Path :",Path)

            self.VideoThread[self.CamId] = VideoCapture(self.CamId,Path)
            self.VideoThread[self.CamId].change_pixmap_signal.connect(Screens[self.CamId])
            self.VideoThread[self.CamId].start()

        elif st==False:

            self.Play_Pause_ButtonStatus[self.CamId]=False
            self.VideoThread[self.CamId].stop()

    # Select Video Path Method

    def SelectVideoPath(self,ButtonID):
      
        self.CamId=int(ButtonID.objectName().split('_')[1])-1
        self.LogPrint("ButtonID : ",ButtonID.objectName()," CamID :",self.CamId)
        fname = QFileDialog.getOpenFileName(self, 'Open file', 
        '/home',"Image files (*.jpg *.mp4)")
        
        self.VideoPaths[self.CamId].setText(fname[0])
          

    def Restore(self):

        if (self.count==0):
            self.showNormal()
            self.count+=1

        elif (self.count==1):
            self.showFullScreen()
            self.count=0

    def LogPrint(*argv):
        pass
        print(argv[1:])        

app = QApplication([])
window = MultiCam()
window.showFullScreen()
app.exec_()
