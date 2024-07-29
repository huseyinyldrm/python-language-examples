import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from tableForm import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.loadProducts()
        self.ui.pushButton.clicked.connect(self.saveProduct) # kaydetme butonunu aktif eder.
        self.ui.tableProducts.doubleClicked.connect(self.doubleClick) # degistirmek istenilen urune cift  tikladiginda etkin olur.

    def saveProduct(self):
        name = self.ui.txtName.text()
        price = self.ui.txtPrice.text()

        if name and price:  # Boş kontrolü
            model = self.ui.tableProducts.model()
            rowCount = model.rowCount()
            model.insertRow(rowCount)
            model.setItem(rowCount, 0, QStandardItem(name))
            model.setItem(rowCount, 1, QStandardItem(price))
            print(f"Added: {name} - {price}")

    def doubleClick(self):
        for item in self.ui.tableProducts.selectedIndexes():
            print(item.row(), item.column(), item.data())

    def loadProducts(self):
        # Ürün listesi
        products = [
            {"name": "samsung s6", "price": 2000},
            {"name": "samsung s7", "price": 4000},
            {"name": "samsung s8", "price": 5000},
            {"name": "samsung s9", "price": 7000},
            {"name": "samsung s3", "price": 1000}
        ]

        # QStandardItemModel ile tablo modeli oluşturuluyor
        model = QStandardItemModel(len(products), 2)  # Satır ve sütun sayısı belirleniyor
        model.setHorizontalHeaderLabels(["Name", "Price"])  # Sütun başlıkları ayarlanıyor

        # Ürün bilgileri modele ekleniyor
        for rowIndex, product in enumerate(products):
            model.setItem(rowIndex, 0, QStandardItem(product["name"]))  # Ürün ismi ekleniyor
            model.setItem(rowIndex, 1, QStandardItem(str(product["price"])))  # Ürün fiyatı ekleniyor

        # Model tabloya ayarlanıyor
        self.ui.tableProducts.setModel(model)

        # Sütun genişlikleri ayarlanıyor
        self.ui.tableProducts.setColumnWidth(0, 200)
        self.ui.tableProducts.setColumnWidth(1, 100)

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()
