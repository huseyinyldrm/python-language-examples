import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from checkboxForm import Ui_MainWindow # ayni klasorde olmalıdır.

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.cbSinema.stateChanged.connect(self.showState)
        self.ui.cbKitapOkumak.stateChanged.connect(self.showState)
        self.ui.cbSpor.stateChanged.connect(self.showState)

        self.ui.cbBoksYapma.stateChanged.connect(self.showState2)
        self.ui.cbFutbol.stateChanged.connect(self.showState2)
        self.ui.cbYuzmek.stateChanged.connect(self.showState2)


        self.ui.btnSecimlerAl.clicked.connect(self.getAllChecked)
        self.ui.btnSecimlerAl_2.clicked.connect(self.getAllChecked2)

    def getAllChecked(self):
        result=''
        items=self.ui.groupHobiler.findChildren(QtWidgets.QCheckBox)
        for cb in items:
            if cb.isChecked(): 
                result+=cb.text() + '\n'   
        
        self.ui.lblResult_2.setText(result)
    
    def getAllChecked2(self):
        result=''
        items=self.ui.groupHobiler_2.findChildren(QtWidgets.QCheckBox)
        for cb in items:
            if cb.isChecked(): 
                result+=cb.text() + '\n'   
        
        self.ui.lblResult.setText(result)



    def showState(self,value):
            cb=self.sender()

            print(value)
            print(cb.text())
            print(cb.isChecked())

    def showState2(self,value):
            cb=self.sender()

            print(value)
            print(cb.text())
            print(cb.isChecked())


def app():
    app=QtWidgets.QApplication(sys.argv)
    win=myApp()
    win.show()
    sys.exit(app.exec_())


app()