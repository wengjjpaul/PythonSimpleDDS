import socket
import time
import xml.etree.ElementTree as ET
import Subscriber
import atexit
from PyQt4 import QtCore, QtGui, uic
from pyqtsubscriber import Ui_PyQtSubscriber
import sys
import threading


#==========================================UI CLASS==========================================#
class StartQt4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        #Initialise UI class
        self.ui = Ui_PyQtSubscriber()
        self.ui.setupUi(self)

        ###initialise objects
        #Text used to display current topic data
        self.mText = self.ui.textBrowserForCurrentTopic
        self.mText.append("Hello")
        #Listview to show all available topics (To do)
        self.mListView = self.ui.listViewOfTopics
        #Push button to select topic to display
        self.mButton = self.ui.pushButton
        self.connect(self.mButton, QtCore.SIGNAL("clicked()"), self.updateTopic)
        #textEdit to input topic
        self.mInputTopic = self.ui.textEdit
        self.mSubscriberThread = None
#update topic function
    def updateTopic(self):
        if(self.mSubscriberThread):
            self.mSubscriberThread.clearUp()
        self.mSubscriberThread = SubscriberThread()
        self.connect(self.mSubscriberThread, QtCore.SIGNAL("printToText(QString)"), self.edit_Text)
        self.connect(self.mSubscriberThread, QtCore.SIGNAL("updateTopicList(QString)"), self.updateTopicList)
        self.mSubscriberThread.subscribeTo(self.mInputTopic.toPlainText())
        self.mSubscriberThread.start()
#update topic view list
    def updateTopicList(self):
        pass
#edit text function
    def edit_Text(self, aString):
        self.mText.clear()
        self.mText.append(aString)

#Shutdown function
    def closeEvent(self, event):
        self.mSubscriberThread.clearUp()
        #Need a better way to kill thread
        self.mSubscriberThread = SubscriberThread()
        pass
#==========================================UI CLASS==========================================#
#===================================UI Thread for Subscriber=================================#
class SubscriberThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)
        self.tree = ET.parse('DDSConfigFile.xml')
        self.SubscriberHostIPV4 = self.tree.find("ServerInformation").find("SubscriberHostIPV4").text
        self.SubscriberHostPort = int(self.tree.find("ServerInformation").find("SubscriberHostPort").text)
        self.firstSubscriber = Subscriber.Subscriber(self.SubscriberHostIPV4, self.SubscriberHostPort)
        self.mTopic = None
    def subscribeTo(self, aTopic):
        self.mTopic = aTopic
        self.firstSubscriber.subscribeTo(aTopic, self.onDataAvailableTopicOne)
    def onDataAvailableTopicOne(self, aData):
        self.emit(QtCore.SIGNAL("printToText(QString)"), aData)
    def run(self):
        while 1:
            time.sleep(2)
    def clearUp(self):
        if (not (self.mTopic == None)):
            self.mTopic = None
            self.firstSubscriber.unSubscribe()
            return
#===================================UI Thread for Subscriber=================================#
def startUI():
    applicationBase = QtGui.QApplication(sys.argv)
    ASimpleSubscriberApp = StartQt4()
    ASimpleSubscriberApp.move(300, 300)
    ASimpleSubscriberApp.setWindowTitle('ASimpleSubscriber') 
    
    ASimpleSubscriberApp.show()
    sys.exit(applicationBase.exec_())

#Begin Main Code here
if __name__ == "__main__":
    t = threading.Thread(target = startUI)
    t.start()

    while 1:
        time.sleep(1)
        pass

    print("End of program")

