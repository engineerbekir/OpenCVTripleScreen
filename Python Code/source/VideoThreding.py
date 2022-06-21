import threading
import time
import cv2
from PyQt5.QtCore import pyqtSignal,pyqtSlot
from cv2 import imshow
import numpy as np
from PyQt5.QtCore import pyqtSignal,  QThread,QObject

    
class VideoCapture(threading.Thread,QObject):
    change_pixmap_signal = pyqtSignal(np.ndarray)
    def __init__(self,threadID, path):

        threading.Thread.__init__(self)
        QObject.__init__(self)

        self.threadID=int(threadID)
        self.Flag=True

        if len(path)<2:
            self.path=int(path)
        else :
            self.path=path
        
       
        
    def run(self):

        cap = cv2.VideoCapture(self.path)
        print(self.path)
        try:
            while (self.Flag):
                ret, Frame = cap.read() 
                if ret:
                   
                    Frame=cv2.resize(Frame,(360,240))
                    self.change_pixmap_signal.emit(Frame)
                    time.sleep(0.025)
                      
                else :
                    pass
        except:
            pass
    
    def stop(self):

        self.Flag=False
        return self.Flag




