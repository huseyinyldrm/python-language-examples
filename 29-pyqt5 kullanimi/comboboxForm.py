# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'combobox.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(764, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cbSehirler = QtWidgets.QComboBox(self.centralwidget)
        self.cbSehirler.setGeometry(QtCore.QRect(10, 20, 251, 81))
        self.cbSehirler.setObjectName("cbSehirler")
        self.lblResult = QtWidgets.QLabel(self.centralwidget)
        self.lblResult.setGeometry(QtCore.QRect(290, 20, 281, 71))
        self.lblResult.setObjectName("lblResult")
        self.btnGetItem = QtWidgets.QPushButton(self.centralwidget)
        self.btnGetItem.setGeometry(QtCore.QRect(10, 150, 211, 71))
        self.btnGetItem.setObjectName("btnGetItem")
        self.btnLoadItems = QtWidgets.QPushButton(self.centralwidget)
        self.btnLoadItems.setGeometry(QtCore.QRect(10, 240, 211, 71))
        self.btnLoadItems.setObjectName("btnLoadItems")
        self.btnClear = QtWidgets.QPushButton(self.centralwidget)
        self.btnClear.setGeometry(QtCore.QRect(10, 330, 211, 71))
        self.btnClear.setObjectName("btnClear")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 764, 26))
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
        self.lblResult.setText(_translate("MainWindow", "TextLabel"))
        self.btnGetItem.setText(_translate("MainWindow", "Get Item"))
        self.btnLoadItems.setText(_translate("MainWindow", "Load Items"))
        self.btnClear.setText(_translate("MainWindow", "ClearItems"))
