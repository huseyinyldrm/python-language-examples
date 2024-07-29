import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
from PyQt5.QtGui import QPalette,QColor

class Color(QWidget):
    def __init__(self,color) :
        super(Color,self).__init__()
        self.setAutoFillBackground(True)

        palette=self.palette()
        palette.setColor(QPalette.Window,QColor(color)) #buraya dikkat!!!
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setGeometry(100,100,500,500)
        
        vlayout=QtWidgets.QVBoxLayout() # Vertical yani alt alta
        vlayout.addWidget(Color('red'))
        vlayout.addWidget(Color('blue'))
        vlayout.addWidget(Color('green'))
        vlayout.addWidget(Color('yellow'))
        vlayout.setContentsMargins(50,50,50,50)

        hlayout=QtWidgets.QHBoxLayout() # Horizontal yani yan yana
        hlayout.addWidget(Color('purple'))
        hlayout.addWidget(Color('red'))
        hlayout.setSpacing(40)

        vlayout.addLayout(hlayout)

        # layout=QtWidgets.QGridLayout()
        # layout.addWidget(Color('red'),0,0)
        # layout.addWidget(Color('green'),1,0)
        # layout.addWidget(Color('blue'),1,1)
        # layout.addWidget(Color('pink'),3,3)


        widget=QWidget()
        widget.setLayout(vlayout)

        self.setCentralWidget(widget)

def app():
    app=QApplication(sys.argv)
    win=MainWindow()
    win.show()
    sys.exit(app.exec_())

app()