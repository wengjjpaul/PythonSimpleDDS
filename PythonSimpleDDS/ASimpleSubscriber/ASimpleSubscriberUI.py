import socket
import time
import xml.etree.ElementTree as ET
import Subscriber
import atexit
from PyQt4 import QtCore, QtGui, uic
from pyqtsubscriber import Ui_PyQtSubscriber
import sys
import threading

#test
import signal, os

def onDataAvailableTopicOne(aData):
    print(aData)
def exit_handler():
    firstSubscriber.unSubscribe()

#==========================================UI CLASS==========================================#
class StartQt4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        #Initialise UI class
        self.ui = Ui_PyQtSubscriber()
        self.ui.setupUi(self)

        #initialise objects
        self.mText = self.ui.textBrowser
        self.mText.append("Hello")

        #Variable to store subscriber
        self.mSubscriber = MySubscriber()
        
        #signal
        
        UIthread1 = threading.Thread(target=self.mSubscriber.thread_Operator)
        UIthread1.start()
#edit text function
    def edit_Text(self, aString):
        self.mText.clear()
        self.mText.append(aString)

#Shutdown function
    def closeEvent(self, event):
        pass
    #register Subscriber
    def registerSubscriber(self, aSubscriber):
        self.mSubscriber = aSubscriber

    #test
    def testText():
        self.edit_Text("AAA")

#==========================================UI CLASS==========================================#
#==========================================Subscriber Class==================================#
class MySubscriber():
    def __init__(self):
        
        pass
    def thread_Operator(self):
        while 1:
            signal.alarm(1)
            time.sleep(2)

#Begin Main Code here
if __name__ == "__main__":
    applicationBase = QtGui.QApplication(sys.argv)
    ASimpleSubscriberApp = StartQt4()
    ASimpleSubscriberApp.move(300, 300)
    ASimpleSubscriberApp.setWindowTitle('ASimpleSubscriber') 

    #Create Subscriber and give Subscriber access to UI application for displaying
    UISubscriber = MySubscriber(ASimpleSubscriberApp)
    #Register subscriber to allow UI to use subscriber methods
    ASimpleSubscriberApp.registerSubscriber(UISubscriber)

    #use thread to start subscriber
    
    
    ASimpleSubscriberApp.show()
    sys.exit(applicationBase.exec_())    

    tree = ET.parse('DDSConfigFile.xml')
    SubscriberHostIPV4 = tree.find("ServerInformation").find("SubscriberHostIPV4").text
    SubscriberHostPort = int(tree.find("ServerInformation").find("SubscriberHostPort").text)

    firstSubscriber = Subscriber.Subscriber(SubscriberHostIPV4, SubscriberHostPort)
    firstSubscriber.subscribeTo("topicOne", onDataAvailableTopicOne)

    atexit.register(exit_handler)
    print(firstSubscriber.getTopic())

    while 1:
        time.sleep(1)
        pass

    print("End of program")

