from PyQt5 import QtWidgets
import sys
from MainWindow import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.hesaplama)  #toplama
        self.ui.pushButton_2.clicked.connect(self.hesaplama)#cikarma
        self.ui.pushButton_3.clicked.connect(self.hesaplama)#carpma
        self.ui.pushButton_4.clicked.connect(self.hesaplama)#bolme

    
    def hesaplama(self):

        sender=self.sender().text()
        result=0

        if(sender=="Toplama"):
            result=int(self.ui.lineEdit.text()) + int(self.ui.lineEdit_2.text())
        elif(sender=="Cikarma"):
            result=int(self.ui.lineEdit.text()) - int(self.ui.lineEdit_2.text())
        elif(sender=="Carpma"):
            result=int(self.ui.lineEdit.text()) * int(self.ui.lineEdit_2.text())
        elif(sender=="Bolme"):
            result=int(self.ui.lineEdit.text()) / int(self.ui.lineEdit_2.text())

        self.ui.label_3.setText("Sonuc: "+str(result))



def app():
    app=QtWidgets.QApplication(sys.argv)
    win=myApp()
    win.show()
    sys.exit(app.exec_())


app()

# Qt Designer uzerinde olusturulan tasarim kaydedilir ve VSCode'de python diline cevirmek icin terminale gerekli olan su kod blogu yazilir:pyuic5 MainWindow.UI -o MainWindow.py  yazilir. ilk dosya adi mevcut kaydettigimiz dosya adi ikinci dosya adi ise kaydetmek istedigimiz dosya adi.
# Qt Designer uzerinde yaptigimiz degisiklikleri kaydedip tekrar bu islemleri yapmamiz yeterli olacaktir.

