# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'radiobuttonForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
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
        self.lblulke = QtWidgets.QLabel(self.centralwidget)
        self.lblulke.setGeometry(QtCore.QRect(30, 430, 191, 81))
        self.lblulke.setText("")
        self.lblulke.setObjectName("lblulke")
        self.lblEgitim = QtWidgets.QLabel(self.centralwidget)
        self.lblEgitim.setGeometry(QtCore.QRect(400, 430, 191, 81))
        self.lblEgitim.setText("")
        self.lblEgitim.setObjectName("lblEgitim")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 290, 131, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 290, 131, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBoxUlke = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxUlke.setGeometry(QtCore.QRect(20, 10, 331, 271))
        self.groupBoxUlke.setObjectName("groupBoxUlke")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBoxUlke)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 301, 231))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 0, 0, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout.addWidget(self.radioButton_4, 2, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 1, 0, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout.addWidget(self.radioButton_3, 3, 0, 1, 1)
        self.groupBoxEgitim = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxEgitim.setGeometry(QtCore.QRect(380, 10, 331, 281))
        self.groupBoxEgitim.setObjectName("groupBoxEgitim")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBoxEgitim)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 20, 301, 231))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.radioButton_6 = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_6.setObjectName("radioButton_6")
        self.gridLayout_3.addWidget(self.radioButton_6, 1, 0, 1, 1)
        self.radioButton_7 = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_7.setObjectName("radioButton_7")
        self.gridLayout_3.addWidget(self.radioButton_7, 2, 0, 1, 1)
        self.radioButton_5 = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_5.setObjectName("radioButton_5")
        self.gridLayout_3.addWidget(self.radioButton_5, 0, 0, 1, 1)
        self.radioButton_8 = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_8.setObjectName("radioButton_8")
        self.gridLayout_3.addWidget(self.radioButton_8, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.pushButton.setText(_translate("MainWindow", "Ülke Seçimi"))
        self.pushButton_2.setText(_translate("MainWindow", "Eğitim Durumu"))
        self.groupBoxUlke.setTitle(_translate("MainWindow", "Ülkeler"))
        self.radioButton.setText(_translate("MainWindow", "Türkiye"))
        self.radioButton_4.setText(_translate("MainWindow", "Danimarka"))
        self.radioButton_2.setText(_translate("MainWindow", "İsviçre"))
        self.radioButton_3.setText(_translate("MainWindow", "Norveç"))
        self.groupBoxEgitim.setTitle(_translate("MainWindow", "Eğitim"))
        self.radioButton_6.setText(_translate("MainWindow", "Üniversite"))
        self.radioButton_7.setText(_translate("MainWindow", "Yüksek Lisans"))
        self.radioButton_5.setText(_translate("MainWindow", "Lise"))
        self.radioButton_8.setText(_translate("MainWindow", "Doktora"))
