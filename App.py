import sys
from PyQt5 import QtWidgets, QtGui, Qt
from Database import Iller
from Ortak import OrtakIslemler, SATSLabel, SATSComboBox, SATSDatePicker, SATSListView, SATSButton, SATSTextBox, SATSPasswordBox


# Ana Ekranın ve Özelliklerinin Tanımlanması
class AnaEkran(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.MainWindowDuzenle()

    def MainWindowDuzenle(self):
        # MainWindowda görünecek isim
        self.setWindowTitle("SATS")

        # MainWindow Arka Plan Rengi
        self.setAutoFillBackground(True)
        palet = self.palette()
        palet.setColor(self.backgroundRole(), QtGui.QColor(230, 230, 230))
        self.setPalette(palet)

        # MainWindow Gösterimi
        self.showMaximized()


# Açılış Karşılama Ekranı
class Hosgeldiniz(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Temel Görünümün Tanımlanıp İçeriğinin Dodurulması
        grid = Ortak.TemelGorunum()
        lblHosgeldiniz = SATSLabel("Hoşgeldiniz")

        # Hoşgeldiniz Labelının İşlem Alanını Ortalaması Amacıyla Tanımalanan Layoutlar
        h_box_lblHosgeldiniz = QtWidgets.QHBoxLayout()
        h_box_lblHosgeldiniz.addStretch()
        h_box_lblHosgeldiniz.addWidget(lblHosgeldiniz)
        h_box_lblHosgeldiniz.addStretch()
        v_box_lblHosgeldiniz = QtWidgets.QVBoxLayout()
        v_box_lblHosgeldiniz.addLayout(h_box_lblHosgeldiniz)

        grid.addLayout(v_box_lblHosgeldiniz, 2, 0)
        self.setLayout(grid)


# Olay Ekleme Ekranı
class OlayKayit(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    # Olay Kayıt Formunun Tasarımı
    def init_ui(self):
        # Temel Görünümün Tanımlanması
        self.anagrid = Ortak.TemelGorunum()
        self.grid = QtWidgets.QGridLayout()

        # İşlem Alanının Satır ve Süturlara Bölünmesi
        OrtakIslemler.RowOlustur(self.grid, 1, 3, 3, 3, 1, 3, 3, 3, 3, 1)
        OrtakIslemler.ColumnOlustur(self.grid, 1, 8, 8, 8, 8, 8, 8, 1)

        # İşlem Alanına Eklenecek Bileşenlerin Tanımlanıp İşlem Alanına Eklenmesi
        lbl_il = SATSLabel("İl:")
        self.grid.addWidget(lbl_il, 1, 1)
        
        cb_il = SATSComboBox()
        self.grid.addWidget(cb_il, 1, 2)
        iller = Iller.TumVerileriGetir()
        for il in iller:
            cb_il.addItem(str(il))

        lbl_ilce = SATSLabel("İlçe:")
        self.grid.addWidget(lbl_ilce, 1, 3)

        cb_ilce = SATSComboBox()
        self.grid.addWidget(cb_ilce, 1, 4)

        lbl_pm = SATSLabel("Polis Merkezi:")
        self.grid.addWidget(lbl_pm, 1, 5)

        cb_pm = SATSComboBox()
        self.grid.addWidget(cb_pm, 1, 6)

        lbl_mh = SATSLabel("Mahalle:")
        self.grid.addWidget(lbl_mh, 2, 1)

        cb_mh = SATSComboBox()
        self.grid.addWidget(cb_mh, 2, 2)

        lbl_sn = SATSLabel("Suç Nevi:")
        self.grid.addWidget(lbl_sn, 2, 3)

        cb_sn = SATSComboBox()
        self.grid.addWidget(cb_sn, 2, 4)

        lbl_fd = SATSLabel("Fail Durumu:")
        self.grid.addWidget(lbl_fd, 2, 5)

        cb_fd = SATSComboBox()
        self.grid.addWidget(cb_fd, 2, 6)

        lbl_tarih = SATSLabel("Tarih:")
        self.grid.addWidget(lbl_tarih, 3, 1)

        de_tarih = SATSDatePicker()
        self.grid.addWidget(de_tarih, 3, 2)

        lbl_magdur = SATSLabel("Mağrur(lar):")
        self.grid.addWidget(lbl_magdur, 4, 1)

        lw_magdur = SATSListView()
        self.grid.addWidget(lw_magdur, 5, 1, 2, 2)

        btn_magdur_ekle = SATSButton("Ekle")
        btn_magdur_ekle.clicked.connect(lambda: OlayKayit.btn_magdur_ekle_click(btn_magdur_ekle.parent().parent()))
        self.grid.addWidget(btn_magdur_ekle, 7, 1)

        btn_magdur_cikar = SATSButton("Çıkar")
        self.grid.addWidget(btn_magdur_cikar, 7, 2)

        lbl_supheli = SATSLabel("Şüpheli(ler):")
        self.grid.addWidget(lbl_supheli, 4, 5)

        lw_supheli = SATSListView()
        self.grid.addWidget(lw_supheli, 5, 5, 2, 2)

        btn_supheli_ekle = SATSButton("Ekle")
        btn_supheli_ekle.clicked.connect(lambda: OlayKayit.btn_supheli_ekle_click(btn_supheli_ekle.parent().parent()))
        self.grid.addWidget(btn_supheli_ekle, 7, 5)

        btn_supheli_cikar = SATSButton("Çıkar")
        self.grid.addWidget(btn_supheli_cikar, 7, 6)

        lbl_tanik = SATSLabel("Tanık(lar):")
        self.grid.addWidget(lbl_tanik, 4, 3)

        lw_tanik = SATSListView()
        self.grid.addWidget(lw_tanik, 5, 3, 2, 2)

        btn_tanik_ekle = SATSButton("Ekle")
        btn_tanik_ekle.clicked.connect(lambda: OlayKayit.btn_tanik_ekle_click(btn_tanik_ekle.parent().parent()))
        self.grid.addWidget(btn_tanik_ekle, 7, 3)

        btn_tanik_cikar = SATSButton("Çıkar")
        self.grid.addWidget(btn_tanik_cikar, 7, 4)

        btn_ekle = SATSButton("Ekle")
        self.grid.addWidget(btn_ekle, 8, 5, 1, 2)
        
        # Tanımlanan Tasarımın Widgeta Eklenmesi
        self.anagrid.addLayout(self.grid, 2, 0)
        self.setLayout(self.anagrid)

    # Mağdur Ekleme Formunun Tasarımı
    @staticmethod
    def MagdurEkle():
        # Temel Görünümün Tanımlanması
        widget = QtWidgets.QWidget()
        anagrid = Ortak.TemelGorunum()
        grid = QtWidgets.QGridLayout()

        # İşlem Alanının Satır ve Süturlara Bölünmesi
        OrtakIslemler.RowOlustur(grid, 1, 1, 1, 1, 1, 1)
        OrtakIslemler.ColumnOlustur(grid, 3, 3, 3, 3, 1)

        # İşlem Alanına Eklenecek Bileşenlerin Tanımlanıp İşlem Alanına Eklenmesi
        lbl_TC = SATSLabel("TC Kimlik No:")
        grid.addWidget(lbl_TC, 1, 0)

        lbl_isim = SATSLabel("İsim:")
        grid.addWidget(lbl_isim, 2, 0)

        lbl_soyisim = SATSLabel("Soyisim:")
        grid.addWidget(lbl_soyisim, 3, 0)

        txt_TC = SATSTextBox()
        grid.addWidget(txt_TC, 1, 1)

        txt_isim = SATSTextBox()
        grid.addWidget(txt_isim, 2, 1)

        txt_soyisim = SATSTextBox()
        grid.addWidget(txt_soyisim, 3, 1)

        lw_liste = SATSListView()
        grid.addWidget(lw_liste, 1, 2, 3, 2)

        btn_ekle = SATSButton("Ekle")
        grid.addWidget(btn_ekle, 4, 2)

        btn_cikar = SATSButton("-")
        grid.addWidget(btn_cikar, 1, 4)

        btn_tamam = SATSButton("Tamam")
        grid.addWidget(btn_tamam, 4, 3)

        # Oluşturulan Tasarımın Widget Olarak Geri Döndürülmesi
        anagrid.addLayout(grid, 2, 0)
        widget.setLayout(anagrid)
        return widget

    # Tanık Ekleme Formunun Tasarımı
    @staticmethod
    def TanikEkle():
        # Temel Görünümün Tanımlanması
        widget = QtWidgets.QWidget()
        anagrid = Ortak.TemelGorunum()
        grid = QtWidgets.QGridLayout()

        # İşlem Alanının Satır ve Süturlara Bölünmesi
        OrtakIslemler.RowOlustur(grid, 1, 1, 1, 1, 1, 1)
        OrtakIslemler.ColumnOlustur(grid, 3, 3, 3, 3, 1)

        # İşlem Alanına Eklenecek Bileşenlerin Tanımlanıp İşlem Alanına Eklenmesi
        lbl_TC = SATSLabel("TC Kimlik No:")
        grid.addWidget(lbl_TC, 1, 0)

        lbl_isim = SATSLabel("İsim:")
        grid.addWidget(lbl_isim, 2, 0)

        lbl_soyisim = SATSLabel("Soyisim:")
        grid.addWidget(lbl_soyisim, 3, 0)

        txt_TC = SATSTextBox()
        grid.addWidget(txt_TC, 1, 1)

        txt_isim = SATSTextBox()
        grid.addWidget(txt_isim, 2, 1)

        txt_soyisim = SATSTextBox()
        grid.addWidget(txt_soyisim, 3, 1)

        lw_liste = SATSListView()
        grid.addWidget(lw_liste, 1, 2, 3, 2)

        btn_ekle = SATSButton("Ekle")
        grid.addWidget(btn_ekle, 4, 2)

        btn_cikar = SATSButton("-")
        grid.addWidget(btn_cikar, 1, 4)

        btn_tamam = SATSButton("Tamam")
        grid.addWidget(btn_tamam, 4, 3)

        # Oluşturulan Tasarımın Widget Olarak Geri Döndürülmesi
        anagrid.addLayout(grid, 2, 0)
        widget.setLayout(anagrid)
        return widget

    # Şüpheli Ekleme Formunun Tasarımı
    @staticmethod
    def SupheliEkle():
        # Temel Görünümün Tanımlanması
        widget = QtWidgets.QWidget()
        anagrid = Ortak.TemelGorunum()
        grid = QtWidgets.QGridLayout()

        # İşlem Alanının Satır ve Süturlara Bölünmesi
        OrtakIslemler.RowOlustur(grid, 1, 1, 1, 1, 1, 1)
        OrtakIslemler.ColumnOlustur(grid, 3, 3, 3, 3, 1)

        # İşlem Alanına Eklenecek Bileşenlerin Tanımlanıp İşlem Alanına Eklenmesi
        lbl_TC = SATSLabel("TC Kimlik No:")
        grid.addWidget(lbl_TC, 1, 0)

        lbl_isim = SATSLabel("İsim:")
        grid.addWidget(lbl_isim, 2, 0)

        lbl_soyisim = SATSLabel("Soyisim:")
        grid.addWidget(lbl_soyisim, 3, 0)

        txt_TC = SATSTextBox()
        grid.addWidget(txt_TC, 1, 1)

        txt_isim = SATSTextBox()
        grid.addWidget(txt_isim, 2, 1)

        txt_soyisim = SATSTextBox()
        grid.addWidget(txt_soyisim, 3, 1)

        lw_liste = SATSListView()
        grid.addWidget(lw_liste, 1, 2, 3, 2)

        btn_ekle = SATSButton("Ekle")
        grid.addWidget(btn_ekle, 4, 2)

        btn_cikar = SATSButton("-")
        grid.addWidget(btn_cikar, 1, 4)

        btn_tamam = SATSButton("Tamam")
        grid.addWidget(btn_tamam, 4, 3)

        # Oluşturulan Tasarımın Widget Olarak Geri Döndürülmesi
        anagrid.addLayout(grid, 2, 0)
        widget.setLayout(anagrid)
        return widget

    # Olay Ekleme Butonuna Tıklandığında Tasarımın MainWindowa Eklenmesi
    @staticmethod
    def Olustur(MainWindow: QtWidgets.QMainWindow):
        olay_kayit = OlayKayit()
        MainWindow.setCentralWidget(olay_kayit)

    # Mağdur Ekle Butonunun Tıklanma Olayı
    @staticmethod
    def btn_magdur_ekle_click(MainWindow: QtWidgets.QMainWindow):
        widget = OlayKayit.MagdurEkle()
        MainWindow.setCentralWidget(widget)

    # Tanık Ekle Butonunun Tıklanma Olayı
    @staticmethod
    def btn_tanik_ekle_click(MainWindow: QtWidgets.QMainWindow):
        widget = OlayKayit.TanikEkle()
        MainWindow.setCentralWidget(widget)

    # Şüpheli Ekle Butonunun Tıklanma Olayı
    @staticmethod
    def btn_supheli_ekle_click(MainWindow: QtWidgets.QMainWindow):
        widget = OlayKayit.SupheliEkle()
        MainWindow.setCentralWidget(widget)


# Veri Tabanıda Bulunan Olay Kayıtlarını Düzenlenmesi/Silinmesi Ekranı
class Duzenle_Sil(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Temel Görünümün Tanımlanması
        anagrid = Ortak.TemelGorunum()
        grid = QtWidgets.QGridLayout()

        # İşlem Alanının Satır ve Süturlara Bölünmesi
        OrtakIslemler.RowOlustur(grid, 1, 2, 2, 2, 2, 2, 1)
        OrtakIslemler.ColumnOlustur(grid, 1, 4, 4, 4, 4, 1)

        # İşlem Alanına Eklenecek Bileşenlerin Tanımlanıp İşlem Alanına Eklenmesi
        lbl_il = SATSLabel("İl:")
        grid.addWidget(lbl_il, 1, 1)

        cb_il = SATSComboBox()
        grid.addWidget(cb_il, 1, 2)

        lbl_ilce = SATSLabel("İlçe:")
        grid.addWidget(lbl_ilce, 1, 3)

        cb_ilce = SATSComboBox()
        grid.addWidget(cb_ilce, 1, 4)

        lbl_pm = SATSLabel("Polis Merkezi")
        grid.addWidget(lbl_pm, 2, 1)

        cb_pm = SATSComboBox()
        grid.addWidget(cb_pm, 2, 2)

        lbl_mh = SATSLabel("Mahalle:")
        grid.addWidget(lbl_mh, 2, 3)

        cb_mh = SATSComboBox()
        grid.addWidget(cb_mh, 2, 4)

        lbl_sn = SATSLabel("Suç Nevi:")
        grid.addWidget(lbl_sn, 3, 1)

        cb_sn = SATSComboBox()
        grid.addWidget(cb_sn, 3, 2)

        lbl_fd = SATSLabel("Fail Durumu:")
        grid.addWidget(lbl_fd, 3, 3)

        cb_fd = SATSComboBox()
        grid.addWidget(cb_fd, 3, 4)

        lbl_tarih_bas = SATSLabel("Başlangıç Tarihi:")
        grid.addWidget(lbl_tarih_bas, 4, 1)

        de_bas = SATSDatePicker()
        grid.addWidget(de_bas, 4, 2)

        lbl_tarih_bit = SATSLabel("Bitiş Tarihi:")
        grid.addWidget(lbl_tarih_bit, 4, 3)

        de_bit = SATSDatePicker()
        grid.addWidget(de_bit, 4, 4)

        btn_ara = SATSButton("Ara")
        grid.addWidget(btn_ara, 5, 3, 1, 2)

        # Tanımlanan Tasarımın Widgeta Eklenmesi
        anagrid.addLayout(grid, 2, 0)
        self.setLayout(anagrid)

    # Düzenle/Sil Butonuna Tıklandığında Tasarımın MainWindowa Eklenmesi
    @staticmethod
    def Olustur(MainWindow):
        duzenle_sil = Duzenle_Sil()
        MainWindow.setCentralWidget(duzenle_sil)


# İstatistiki Verierin Görüntülenme Ekranı
class Istatikler(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Temel Görünümün Tanımlanması
        anagrid = Ortak.TemelGorunum()
        grid = QtWidgets.QGridLayout()

        # İşlem Alanının Satır ve Süturlara Bölünmesi
        OrtakIslemler.RowOlustur(grid, 1, 5, 1)
        OrtakIslemler.ColumnOlustur(grid, 1, 8, 8, 1)

        # İşlem Alanına Eklenecek Bileşenlerin Tanımlanıp İşlem Alanına Eklenmesi
        btn_bolge = SATSButton("Bölgeye Göre İstatistikler", True)
        grid.addWidget(btn_bolge, 1, 1)

        btn_suc = SATSButton("Suça Göre İstatistikler", True)
        grid.addWidget(btn_suc, 1, 2)

        # Tanımlanan Tasarımın Widgeta Eklenmesi
        anagrid.addLayout(grid, 2, 0)
        self.setLayout(anagrid)

    # İstatistik Butonuna Tıklandığında Tasarımın MainWindowa Eklenmesi
    @staticmethod
    def Olustur(MainWindow):
        istatistikler = Istatikler()
        MainWindow.setCentralWidget(istatistikler)


# Şifre Değiştirme Ekranı
class Profilim(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Temel Görünümün Tanımlanması
        anagrid = Ortak.TemelGorunum()
        grid = QtWidgets.QGridLayout()

        # İşlem Alanının Satır ve Süturlara Bölünmesi
        OrtakIslemler.RowOlustur(grid, 5, 2, 2, 2, 2, 5)
        OrtakIslemler.ColumnOlustur(grid, 5, 4, 4, 5)

        # İşlem Alanına Eklenecek Bileşenlerin Tanımlanıp İşlem Alanına Eklenmesi
        lbl_mev_sifre = SATSLabel("Mevcut Şifre:")
        grid.addWidget(lbl_mev_sifre, 1, 1)

        pss_mev_sif = SATSPasswordBox()
        grid.addWidget(pss_mev_sif, 1, 2)

        lbl_yeni_sifre = SATSLabel("Yeni Şifre:")
        grid.addWidget(lbl_yeni_sifre, 2, 1)

        pss_yeni_sifre = SATSPasswordBox()
        grid.addWidget(pss_yeni_sifre)

        lbl_yeni_sifre_tk = SATSLabel("Yeni Şifre Tekrar:")
        grid.addWidget(lbl_yeni_sifre_tk, 3, 1)

        pss_yeni_sifre_tk = SATSPasswordBox()
        grid.addWidget(pss_yeni_sifre_tk, 3, 2)

        btn_kaydet = SATSButton("Kaydet")
        grid.addWidget(btn_kaydet, 4, 2)

        # Tanımlanan Tasarımın Widgeta Eklenmesi
        anagrid.addLayout(grid, 2, 0)
        self.setLayout(anagrid)

    # İstatistik Butonuna Tıklandığında Tasarımın MainWindowa Eklenmesi
    @staticmethod
    def Olustur(MainWindow):
        profiim = Profilim()
        MainWindow.setCentralWidget(profiim)


# Sistem Adminlerine Mesaj Gönderilme Ekranı
class Iletisim(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Temel Görünümün Tanımlanması
        anagrid = Ortak.TemelGorunum()
        grid = QtWidgets.QGridLayout()

        # İşlem Alanının Satır ve Süturlara Bölünmesi
        OrtakIslemler.RowOlustur(grid, 1, 2, 2, 2, 12, 2, 2)
        OrtakIslemler.ColumnOlustur(grid, 1, 8, 1)

        # İşlem Alanına Eklenecek Bileşenlerin Tanımlanıp İşlem Alanına Eklenmesi
        lbl_konu = SATSLabel("Konu:")
        grid.addWidget(lbl_konu, 1, 1)

        txt_konu = SATSTextBox()
        grid.addWidget(txt_konu, 2, 1)

        lbl_mesaj = SATSLabel("Mesaj:")
        grid.addWidget(lbl_mesaj, 3, 1)

        txt_mesaj = SATSTextBox()
        grid.addWidget(txt_mesaj, 4, 1)

        btn_gonder = SATSButton("Gönder")
        grid.addWidget(btn_gonder, 5, 1)

        # Tanımlanan Tasarımın Widgeta Eklenmesi
        anagrid.addLayout(grid, 2, 0)
        self.setLayout(anagrid)

    # İstatistik Butonuna Tıklandığında Tasarımın MainWindowa Eklenmesi
    @staticmethod
    def Olustur(MainWindow):
        iletisim = Iletisim()
        MainWindow.setCentralWidget(iletisim)


# Admin İşlemleri Ekranı
class Admin_Paneli(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    # Temel Görünümün Tanımlanması
    def init_ui(self):
        anagrid = Ortak.TemelGorunum()
        grid = QtWidgets.QGridLayout()

        # İşlem Alanının Satır ve Süturlara Bölünmesi
        OrtakIslemler.RowOlustur(grid, 1, 1, 1, 1, 1, 1)
        OrtakIslemler.ColumnOlustur(grid, 1, 2, 1)

        # İşlem Alanına Eklenecek Bileşenlerin Tanımlanıp İşlem Alanına Eklenmesi
        btn_personel_ekle = SATSButton("Personel Ekle", True)
        grid.addWidget(btn_personel_ekle, 1, 1)

        btn_personel_duzenle = SATSButton("Personel Düzenle", True)
        grid.addWidget(btn_personel_duzenle, 2, 1)

        btn_mesajlar = SATSButton("Mesajlar", True)
        grid.addWidget(btn_mesajlar, 3, 1)

        btn_oturum_kayitlari = SATSButton("Oturum Kayıtları", True)
        grid.addWidget(btn_oturum_kayitlari, 4, 1)

        # Tanımlanan Tasarımın Widgeta Eklenmesi
        anagrid.addLayout(grid, 2, 0)
        self.setLayout(anagrid)

    # İstatistik Butonuna Tıklandığında Tasarımın MainWindowa Eklenmesi
    @staticmethod
    def Olustur(MainWindow):
        admin_paneli = Admin_Paneli()
        MainWindow.setCentralWidget(admin_paneli)


# Temel Görünüm Tasarımı
class Ortak(QtWidgets.QWidget):
    @staticmethod
    def TemelGorunum() -> QtWidgets.QGridLayout:
        grid = QtWidgets.QGridLayout()
        OrtakIslemler.RowOlustur(grid, 1, 1, 10)

        btn_olay_kayit = SATSButton("Olay Kayıt", True)
        btn_olay_kayit.clicked.connect(lambda: OlayKayit.Olustur(btn_olay_kayit.parent().parent()))
        btn_duzenle_sil = SATSButton("Düzenle/Sil", True)
        btn_duzenle_sil.clicked.connect(lambda: Duzenle_Sil.Olustur(btn_duzenle_sil.parent().parent()))
        btn_istatistikler = SATSButton("İstatistikler", True)
        btn_istatistikler.clicked.connect(lambda: Istatikler.Olustur(btn_istatistikler.parent().parent()))
        btn_profilim = SATSButton("Profilim", True)
        btn_profilim.clicked.connect(lambda: Profilim.Olustur(btn_profilim.parent().parent()))
        btn_iletisim = SATSButton("İletişim", True)
        btn_iletisim.clicked.connect(lambda: Iletisim.Olustur(btn_iletisim.parent().parent()))
        btn_admin_paneli = SATSButton("Admin Paneli", True)
        btn_admin_paneli.clicked.connect(lambda: Admin_Paneli.Olustur(btn_admin_paneli.parent().parent()))

        h_box = QtWidgets.QHBoxLayout()
        h_box.addWidget(btn_olay_kayit)
        h_box.addWidget(btn_duzenle_sil)
        h_box.addWidget(btn_istatistikler)
        h_box.addWidget(btn_profilim)
        h_box.addWidget(btn_iletisim)
        h_box.addWidget(btn_admin_paneli)
        h_box.addStretch()

        grid.addLayout(h_box, 0, 0)

        lblPersonel = SATSLabel("Polis Memuru Kaan Han GÜNAY / Çekirge Polis Merkezi Amirliği")

        h_box2 = QtWidgets.QHBoxLayout()
        h_box2.addStretch()
        h_box2.addWidget(lblPersonel)

        grid.addLayout(h_box2, 1, 0)

        return grid


app = QtWidgets.QApplication(sys.argv)
anaekran = AnaEkran()
hosgeldiniz = Hosgeldiniz()
anaekran.setCentralWidget(hosgeldiniz)
sys.exit(app.exec_())
