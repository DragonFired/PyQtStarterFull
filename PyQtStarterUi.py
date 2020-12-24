# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/arana/Documents/PycharmProjects/SNHU/Classes/CrapsStarter/Craps.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(692, 453)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.rollButton = QtWidgets.QPushButton(self.centralwidget)
        self.rollButton.setGeometry(QtCore.QRect(270, 320, 115, 32))
        self.rollButton.setObjectName("rollButton")
        self.die1View = QtWidgets.QLabel(self.centralwidget)
        self.die1View.setGeometry(QtCore.QRect(110, 40, 181, 171))
        self.die1View.setText("")
        self.die1View.setPixmap(QtGui.QPixmap(":/images/6Face.png"))
        self.die1View.setObjectName("die1View")
        self.die2View = QtWidgets.QLabel(self.centralwidget)
        self.die2View.setGeometry(QtCore.QRect(380, 40, 181, 181))
        self.die2View.setText("")
        self.die2View.setPixmap(QtGui.QPixmap(":/images/6Face.png"))
        self.die2View.setObjectName("die2View")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 692, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.rollButton.setText(_translate("MainWindow", "PushButton"))

import diceResources_rc
