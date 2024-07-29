import sys

from PyQt5.QtCore import Qt
from comboboxForm import Ui_MainWindow
from PyQt5 import QtWidgets


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        combo=self.ui.cbSehirler

        # combo.addItem("Ankara")
        # combo.addItem("Istanbul")
        # combo.addItem("Diyarbakir")
        # combo.addItem("Bingöl")
        # #combo.addItems(["Adana","Izmir","Muş","Malatya","Elaziğ"])

        self.ui.btnGetItem.clicked.connect(self.GetItem)
        self.ui.btnLoadItems.clicked.connect(self.LoadItems)
        self.ui.btnClear.clicked.connect(self.ClearItems)


        self.ui.cbSehirler.currentIndexChanged.connect(self.SelectedChangedIndex)
        self.ui.cbSehirler.currentIndexChanged[str].connect(self.SelectedChangedText)

    
    def LoadItems(self):
        sehirler=["Diyarbekir","Gaziantep","Mardin","Tunceli","Hakkari","Sivas","Bingöl","Şanliurfa","Elaziğ","Malatya","Erzincan"]

        self.ui.cbSehirler.addItems(sehirler)


    def GetItem(self):
        print(self.ui.cbSehirler.currentText())
        print(self.ui.cbSehirler.currentIndex())
        count=self.ui.cbSehirler.count()

        for index in range(count):
            print(self.ui.cbSehirler.itemText(index))

    def ClearItems(self):
        self.ui.cbSehirler.clear()

    def SelectedChangedIndex(self,index):
        print(index)

    def SelectedChangedText(self,text):
        print(text)

def app():
    app=QtWidgets.QApplication(sys.argv)
    win=Window()
    win.show()
    sys.exit(app.exec_())


app()
