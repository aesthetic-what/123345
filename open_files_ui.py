# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '\\edu.local\public\studenthomes\22200322\Desktop\manage_shop(Гапчук)\src\open_files.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.open_explorer = QtWidgets.QPushButton(self.centralwidget)
        self.open_explorer.setGeometry(QtCore.QRect(10, 490, 131, 61))
        self.open_explorer.setObjectName("open_explorer")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 20, 691, 71))
        self.label.setText("")
        self.label.setObjectName("label")
        self.add_data = QtWidgets.QPushButton(self.centralwidget)
        self.add_data.setGeometry(QtCore.QRect(160, 490, 131, 61))
        self.add_data.setObjectName("add_data")
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(140, 100, 551, 361))
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.open_explorer.setText(_translate("MainWindow", "open"))
        self.add_data.setText(_translate("MainWindow", "add"))