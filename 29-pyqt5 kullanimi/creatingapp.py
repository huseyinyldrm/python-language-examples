import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        # Pencere başlığını ayarla
        self.setWindowTitle("First Application")

        # Pencerenin boyut ve konumunu ayarla
        self.setGeometry(500, 200, 700, 700)

        # Pencereye araç ipucu ekle
        self.setToolTip("my tooltip")

        # Kullanıcı arayüzünü başlat
        self.initUI()

    def clicked(self):
        # Butona tıklanıldığında sonuç etiketini güncelle
        self.lbl_result.setText("Ad: " + self.txt_name.text() + " Soyad: " + self.txt_surname.text())

    def initUI(self):
        # İsim etiketi oluştur ve konumunu ayarla
        self.lbl_name = QLabel(self)
        self.lbl_name.setText("Adiniz:")
        self.lbl_name.move(50, 30)

        # Soyisim etiketi oluştur ve konumunu ayarla
        self.lbl_surname = QLabel(self)
        self.lbl_surname.setText("Soyadiniz:")
        self.lbl_surname.move(50, 70)

        # Sonuç etiketini oluştur, boyutunu ve konumunu ayarla
        self.lbl_result = QLabel(self)
        self.lbl_result.resize(300, 50)
        self.lbl_result.move(150, 130)

        # İsim için metin kutusu oluştur ve konumunu ayarla
        self.txt_name = QLineEdit(self)
        self.txt_name.move(150, 30)
        self.txt_name.resize(200, 32)

        # Soyisim için metin kutusu oluştur ve konumunu ayarla
        self.txt_surname = QLineEdit(self)
        self.txt_surname.move(150, 70)
        self.txt_surname.resize(200, 32)

        # Kaydet butonu oluştur, konumunu ayarla ve tıklanma olayını bağla
        self.btn_save = QPushButton(self)
        self.btn_save.setText("Kaydet")
        self.btn_save.move(150, 110)
        self.btn_save.clicked.connect(self.clicked)

def window():
    # Uygulama nesnesi oluştur
    app = QApplication(sys.argv)

    # Pencere nesnesi oluştur ve göster
    win = MyWindow()
    win.show()

    # Uygulamayı çalıştır ve pencere kapatılana kadar bekle
    sys.exit(app.exec_())

# Pencereyi başlat
window()


"""
1-QApplication:
Aciklama: PyQt5 uygulamasini baslatmak icin gereken ana sinif.
Ornek: app = QApplication(sys.argv)

2-QWidget:
Aciklama: Tum PyQt5 arayuz bilesenlerinin temel sinifi.
Ornek: widget = QWidget()

3-QMainWindow:
Aciklama: Ana pencere sinifi, menu cubuklari, arac cubuklari ve durum cubuklari gibi bilesenleri icerir.
Ornek: main_window = QMainWindow()

4-QLabel:
Aciklama: Metin veya resim gostermek icin kullanilan etiket widget'i.
Ornek: label = QLabel("Hello, World!")

5-QPushButton:
Aciklama: Tiklanabilir dugme widget'i.
Ornek: button = QPushButton("Click Me")

6-QLineEdit:
Aciklama: Tek satirlik metin girisi widget'i.
Ornek: line_edit = QLineEdit()

7-QTextEdit:
Aciklama: Cok satirli metin girisi ve duzenleme widget'i.
Ornek: text_edit = QTextEdit()

8-QComboBox:
Aciklama: Acilir menu widget'i, kullaniciya secim yapma olanagi saglar.
Ornek: combo_box = QComboBox()

9-QCheckBox:
Aciklama: Isaretlenebilir kutucuk widget'i.
Ornek: check_box = QCheckBox("Check Me")

10-QRadioButton:
Aciklama: Radyo dugmesi widget'i, genellikle gruplar halinde kullanilir.
Ornek: radio_button = QRadioButton("Option 1")

11-QVBoxLayout:
Aciklama: Widget'lari dikey olarak yerlestirmek icin kullanilan duzenleme sinifi.
Ornek: vbox = QVBoxLayout()

12-QHBoxLayout:
Aciklama: Widget'lari yatay olarak yerlestirmek icin kullanilan duzenleme sinifi.
Ornek: hbox = QHBoxLayout()

13-QGridLayout:
Aciklama: Widget'lari izgara duzeninde yerlestirmek icin kullanilan duzenleme sinifi.
Ornek: grid = QGridLayout()

14-QFormLayout:
Aciklama: Form duzeni, etiket ve alan ciftlerini duzenlemek icin kullanilir.
Ornek: form = QFormLayout()

15-QDialog:
Aciklama: Modal diyalog penceresi olusturmak icin kullanilan sinif.
Ornek: dialog = QDialog()

16-QFileDialog:
Aciklama: Dosya secme diyalog penceresi olusturmak icin kullanilan sinif.
Ornek: file_dialog = QFileDialog()

17-QColorDialog:
Aciklama: Renk secme diyalog penceresi olusturmak icin kullanilan sinif.
Ornek: color_dialog = QColorDialog()

18-QFontDialog:
Aciklama: Yazi tipi secme diyalog penceresi olusturmak icin kullanilan sinif.
Ornek: font_dialog = QFontDialog()

19-QMessageBox:
Aciklama: Bilgi, uyari veya hata mesaji gostermek icin kullanilan diyalog penceresi.
Ornek: message_box = QMessageBox()

20-QTimer:
Aciklama: Zamanlayici, belirli araliklarla sinyal gondermek icin kullanilir.
Ornek: timer = QTimer()

21-QSlider:
Aciklama: Kaydirma cubugu, kullaniciya bir deger secme olanagi saglar.
Ornek: slider = QSlider(Qt.Horizontal)

22-QProgressBar:
Aciklama: Ilerleme cubugu, uzun suren islemlerin ilerlemesini gostermek icin kullanilir.
Ornek: progress_bar = QProgressBar()

23-QTableWidget:
Aciklama: Tablo widget'i, hucrelerde veri gostermek icin kullanilir.
Ornek: table_widget = QTableWidget()

24-QListWidget:
Aciklama: Liste widget'i, ogelerin listesini gostermek icin kullanilir.
Ornek: list_widget = QListWidget()

25-QTreeWidget:
Aciklama: Agac yapisi icinde ogeleri gostermek icin kullanilir.
Ornek: tree_widget = QTreeWidget()

"""
