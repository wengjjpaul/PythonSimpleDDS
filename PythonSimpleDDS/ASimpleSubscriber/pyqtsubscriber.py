# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqtsubscriber.ui'
#
# Created: Sat May  4 12:18:33 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_PyQtSubscriber(object):
    def setupUi(self, PyQtSubscriber):
        PyQtSubscriber.setObjectName(_fromUtf8("PyQtSubscriber"))
        PyQtSubscriber.resize(400, 300)
        self.centralWidget = QtGui.QWidget(PyQtSubscriber)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.textBrowserForCurrentTopic = QtGui.QTextBrowser(self.centralWidget)
        self.textBrowserForCurrentTopic.setGeometry(QtCore.QRect(50, 130, 301, 71))
        self.textBrowserForCurrentTopic.setOverwriteMode(True)
        self.textBrowserForCurrentTopic.setObjectName(_fromUtf8("textBrowserForCurrentTopic"))
        self.listViewOfTopics = QtGui.QListWidget(self.centralWidget)
        self.listViewOfTopics.setGeometry(QtCore.QRect(50, 60, 301, 51))
        self.listViewOfTopics.setObjectName(_fromUtf8("listViewOfTopics"))
        self.textEdit = QtGui.QTextEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(160, 10, 191, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 10, 91, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        PyQtSubscriber.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(PyQtSubscriber)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        PyQtSubscriber.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(PyQtSubscriber)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        PyQtSubscriber.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(PyQtSubscriber)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        PyQtSubscriber.setStatusBar(self.statusBar)

        self.retranslateUi(PyQtSubscriber)
        QtCore.QMetaObject.connectSlotsByName(PyQtSubscriber)

    def retranslateUi(self, PyQtSubscriber):
        PyQtSubscriber.setWindowTitle(_translate("PyQtSubscriber", "PyQtSubscriber", None))
        self.pushButton.setText(_translate("PyQtSubscriber", "PushButton", None))

