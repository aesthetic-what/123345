# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '\\edu.local\public\studenthomes\22200322\Desktop\manage_shop(Гапчук)\src\design\edit_data_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(857, 444)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.name_input = QtWidgets.QLineEdit(self.centralwidget)
        self.name_input.setGeometry(QtCore.QRect(50, 20, 301, 51))
        self.name_input.setObjectName("name_input")
        self.price_input = QtWidgets.QLineEdit(self.centralwidget)
        self.price_input.setGeometry(QtCore.QRect(50, 80, 301, 51))
        self.price_input.setObjectName("price_input")
        self.count_input = QtWidgets.QLineEdit(self.centralwidget)
        self.count_input.setGeometry(QtCore.QRect(50, 140, 301, 51))
        self.count_input.setObjectName("count_input")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 260, 281, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.take_photo = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.take_photo.sizePolicy().hasHeightForWidth())
        self.take_photo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.take_photo.setFont(font)
        self.take_photo.setStyleSheet("QPushButton:hover {\n"
"    background-color: #ffdbcc;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #fcb9aa;\n"
"}\n"
"QPushButton {\n"
"    background-color: rgb(57, 208, 208);\n"
"    border-radius: 31px;\n"
"}")
        self.take_photo.setObjectName("take_photo")
        self.verticalLayout.addWidget(self.take_photo)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton:hover {\n"
"    background-color: #ffdbcc;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #fcb9aa;\n"
"}\n"
"QPushButton {\n"
"    background-color: rgb(57, 208, 208);\n"
"    border-radius: 31px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(390, 30, 431, 351))
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.name_input.setPlaceholderText(_translate("MainWindow", "Введите новое имя товара"))
        self.price_input.setPlaceholderText(_translate("MainWindow", "Введите цену товара"))
        self.count_input.setPlaceholderText(_translate("MainWindow", "Введите количество товара"))
        self.take_photo.setText(_translate("MainWindow", "Выбрать картинку"))
        self.pushButton.setText(_translate("MainWindow", "Изменить"))
