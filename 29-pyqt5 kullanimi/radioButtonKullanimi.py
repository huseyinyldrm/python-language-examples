import sys
from PyQt5 import QtWidgets
from radiobuttonForm import Ui_MainWindow

# Main Window sınıfını tanımlıyoruz
class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()  # UI'ı başlatıyoruz
        self.ui.setupUi(self)  # UI öğelerini kuruyoruz

        # İlk radyo butonunu seçili hale getiriyoruz
        self.ui.radioButton.setChecked(True)

        # Radyo butonları için sinyal-slot bağlantılarını kuruyoruz
        self.ui.radioButton.toggled.connect(self.onClickedUlke)  # Türkiye
        self.ui.radioButton_2.toggled.connect(self.onClickedUlke)  # İsviçre
        self.ui.radioButton_3.toggled.connect(self.onClickedUlke)  # Danimarka
        self.ui.radioButton_4.toggled.connect(self.onClickedUlke)  # Norveç

        self.ui.radioButton_5.toggled.connect(self.onClickedEgitim)  # Lise
        self.ui.radioButton_6.toggled.connect(self.onClickedEgitim)  # Üniversite
        self.ui.radioButton_7.toggled.connect(self.onClickedEgitim)  # Yüksek Lisans
        self.ui.radioButton_8.toggled.connect(self.onClickedEgitim)  # Doktora

        # Butonlar için sinyal-slot bağlantılarını kuruyoruz
        self.ui.pushButton.clicked.connect(self.getSelectedUlke)
        self.ui.pushButton_2.clicked.connect(self.getSelectedEgitim)

    # Bir radyo butonuna tıklandığında seçilen ülkeyi yazdıran fonksiyon
    def onClickedUlke(self):
        rb = self.sender()  # Sinyali gönderen radyo butonunu alıyoruz

        if rb.isChecked():
            print("Seçilen Ülke:" + rb.text())

    # Bir radyo butonuna tıklandığında seçilen eğitimi yazdıran fonksiyon
    def onClickedEgitim(self):
        rb = self.sender()  # Sinyali gönderen radyo butonunu alıyoruz

        if rb.isChecked():
            print("Seçilen Eğitim:" + rb.text())

    # Seçili olan ülkeyi label'a yazdıran fonksiyon
    def getSelectedUlke(self):
        items = self.ui.groupBoxUlke.findChildren(QtWidgets.QRadioButton)  # Ülke radyo butonlarını alıyoruz
        for rb in items:
            if rb.isChecked():
                self.ui.lblulke.setText("Seçilen Ülke: " + rb.text())  # Seçili olanın text'ini label'a yazdırıyoruz
                break  # Seçili olanı bulduktan sonra döngüyü sonlandırıyoruz

    # Seçili olan eğitimi label'a yazdıran fonksiyon
    def getSelectedEgitim(self):
        items = self.ui.groupBoxEgitim.findChildren(QtWidgets.QRadioButton)  # Eğitim radyo butonlarını alıyoruz
        for rb in items:
            if rb.isChecked():
                self.ui.lblEgitim.setText("Seçilen Eğitim: " + rb.text())  # Seçili olanın text'ini label'a yazdırıyoruz
                break  # Seçili olanı bulduktan sonra döngüyü sonlandırıyoruz

# Uygulama başlatma fonksiyonu
def app():
    app = QtWidgets.QApplication(sys.argv)  # QApplication nesnesi oluşturuyoruz
    win = Window()  # Window nesnesi oluşturuyoruz
    win.show()  # Ana pencereyi gösteriyoruz
    sys.exit(app.exec_())  # Uygulama döngüsünü başlatıyoruz

# Uygulama fonksiyonunu çağırıyoruz
app()
