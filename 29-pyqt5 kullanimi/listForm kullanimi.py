from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from listForm import Ui_MainWindow
from PyQt5.QtWidgets import QInputDialog , QLineEdit , QMessageBox # QInputDialog içe aktarıldı
import sys

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        #load Students
        self.loadStudents()

        #add new student
        self.ui.btnAdd.clicked.connect(self.addStudent)

        #edit student
        self.ui.btnEdit.clicked.connect(self.editStudent)

        #delete student
        self.ui.btnRemove.clicked.connect(self.removeStudent)

        #up student
        self.ui.btnUp.clicked.connect(self.upStudent)

        #down student
        self.ui.btnDown.clicked.connect(self.downStudent)

        #sort student
        self.ui.btnSort.clicked.connect(self.sortStudent)

        #exit
        self.ui.btnExit.clicked.connect(self.close)

    def loadStudents(self):
        self.ui.listItems.addItems(["Ahmet","Ali","Murat","Can","Canan","Betul","Sevda"])
        self.ui.listItems.setCurrentRow(0) # ilk index secili durumda olur.

    def addStudent(self):
        currentIndex=self.ui.listItems.currentRow()
        text,ok=QInputDialog.getText(self,"New Student","Student Name")
        if ok and text is not None:
            self.ui.listItems.insertItem(currentIndex,text) # 0. indexten sonra ekle.
    
    def editStudent(self):
        index=self.ui.listItems.currentRow()
        item=self.ui.listItems.item(index)

        if item is not None:
            text,ok=QInputDialog.getText(self,"Edit Student","Student Name",QLineEdit.Normal,item.text())

            if text and ok is not None:
                item.setText(text)
    
    def removeStudent(self):
        index=self.ui.listItems.currentRow()
        item=self.ui.listItems.item(index)
        
        if item is None:
            return
        
        q=QMessageBox.question(self,"Remove Student","Do you want to remove student "+item.text(),QMessageBox.Yes | QMessageBox.No)

        if q==QMessageBox.Yes:
            item=self.ui.listItems.takeItem(index)
            del item
    
    def upStudent(self):
        index=self.ui.listItems.currentRow()
        if index >=1:
            item=self.ui.listItems.takeItem(index)
            self.ui.listItems.insertItem(index-1,item)
            self.ui.listItems.setCurrentItem(item)

        
    def downStudent(self):
        index=self.ui.listItems.currentRow()

        if index <self.ui.listItems.count()-1:
            item=self.ui.listItems.takeItem(index)
            self.ui.listItems.insertItem(index+1,item)
            self.ui.listItems.setCurrentItem(item)
        

    def sortStudent(self):
        self.ui.listItems.sortItems()
    
    def close(self):
        quit()


def app():
    app=QtWidgets.QApplication(sys.argv)
    win=Window()
    win.show()
    sys.exit(app.exec_())


app()
