from PyQt5 import QtWidgets, QtGui, Qt


# Tüm Tasarımda Kullanılacak Ortak Değişken ve İşlemler
class OrtakIslemler():
    # Yazı Tipi Ayarı
    @staticmethod
    def Font():
        font = QtGui.QFont()
        font.setPointSize(17)
        return font

    # Gridlerde Satır Oluşturma Fonksiyonu
    @staticmethod
    def RowOlustur(grid: QtWidgets.QGridLayout, *rows):
        row = 0
        for i in rows:
            grid.setRowStretch(row, i)
            row += 1

    # Gridlerde Sütun Oluşturma Fonksiyonu
    @staticmethod
    def ColumnOlustur(grid: QtWidgets.QGridLayout, *columns):
        column = 0
        for i in columns:
            grid.setColumnStretch(column, i)
            column += 1


# Tüm Tasarımda Kullanılacak Olan Label Tasarımı
class SATSLabel(QtWidgets.QLabel):
    def __init__(self, Metin: str):
        self.Metin = Metin
        super().__init__(Metin)
        super().setFont(OrtakIslemler.Font())


# Tüm Tasarımda Kullanılacak Olan ComboBox Tasarımı
class SATSComboBox(QtWidgets.QComboBox):
    def __init__(self):
        super().__init__()
        super().setFont(OrtakIslemler.Font())


# Tüm Tasarımda Kullanılacak Olan DatePicker Tasarımı
class SATSDatePicker(QtWidgets.QDateEdit):
    def __init__(self):
        super().__init__()
        super().setDate(Qt.QDate.currentDate())
        super().setFont(OrtakIslemler.Font())


# Tüm Tasarımda Kullanılacak Olan ListVew Tasarımı
class SATSListView(QtWidgets.QListView):
    def __init__(self):
        super().__init__()
        super().setFont(OrtakIslemler.Font())


# Tüm Tasarımda Kullanılacak Olan Button Tasarımı
class SATSButton(QtWidgets.QPushButton):
    def __init__(self, Metin: str, Flat = False):
        self.Metin = Metin
        super().__init__(Metin)
        super().setFont(OrtakIslemler.Font())
        super().setFlat(Flat)


# Tüm Tasarımda Kullanılacak Olan TextBox Tasarımı
class SATSTextBox(QtWidgets.QLineEdit):
    def __init__(self):
        super().__init__()
        super().setFont(OrtakIslemler.Font())


# Tüm Tasarımda Kullanılacak Olan PassWordBox Tasarımı
class SATSPasswordBox(QtWidgets.QLineEdit):
    def __init__(self):
        super().__init__()
        super().setEchoMode(QtWidgets.QLineEdit.Password)
        super().setFont(OrtakIslemler.Font())
