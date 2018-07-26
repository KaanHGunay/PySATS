import sqlite3


# Genel Veri Tabanı İşlemleri
class VeriTabani():
    # Veri Tabanı Bağlantısı Oluşturup Bağlantı Nesnesini Geri Döner
    @staticmethod
    def Baglanti(VeriTabaniAdi = "SATS"):
        try:
            con = sqlite3.connect(VeriTabaniAdi + ".db")
            return con
        except ConnectionError as e:
            print(e)

    # Veri Tabanı Bağlantısı Oluşturup Cursor Nesnesi Geri Döner
    @staticmethod
    def Baglan(VeriTabaniAdi = "SATS"):
        try:
            con = sqlite3.connect(VeriTabaniAdi + ".db")
            return con.cursor()
        except ConnectionError as e:
            print(e)

    # Veri Tabanından Parametre Olarak Verilen Tablodan Tüm Kayıtları Döner
    @staticmethod
    def TumKayitlariGetir(ClsName: str):
        con = VeriTabani.Baglanti()
        cursor = con.cursor()
        cursor.execute("Select * From ?", (ClsName, ))
        kayitlar = cursor.fetchall()
        con.close()
        return kayitlar

    # Veri Tabanından Parametre Olarak Verilen Tablodan Parametre Olarak Verilen ID Numaralı Kaydı Döner
    @staticmethod
    def IDIleKaydiGetir(ClsName: str, ID: int):
        con = VeriTabani.Baglanti()
        cursor = con.cursor()
        cursor.execute("Select * From ? Where ID = ?", (ClsName, ID))
        kayit = cursor.fetchone()
        con.close()
        return kayit


# Veri Tabanında Bulunan 'Iller' Tablosu Varlığı
class Iller():
    # Tablonun Kolonları İle Varlığın Oluşturulması
    def __init__(self, ID = 0, isim = ""):
        self.ID = ID
        self.isim = isim

    # Varlığın Stringe Dönüştürülmesi
    def __str__(self):
        return self.isim

    # Tabloda Bulunan Tüm Verilerin Çekilmesi
    @staticmethod
    def TumVerileriGetir():
        iller = VeriTabani.TumKayitlariGetir(Iller.__name__)
        liste = []
        
        for ID, isim in iller:
            il = Iller()
            il.ID = ID
            il.isim = isim
            liste.append(il)
        
        return liste

    # Talodan ID İle Veri Çekilmesi
    @staticmethod
    def IDIleVeriGetir(ID: int):
        kayit = VeriTabani.IDIleKaydiGetir(Iller.__name__, ID)
        il = Iller()
        il.ID = kayit[0]
        il.isim = kayit[1]
        return il

    # Tabloya Yeni Veri Eklenmesi
    @staticmethod
    def VeriEkle(il):
        con = VeriTabani.Baglanti()
        cursor = con.cursor()
        cursor.execute("Insert Into Iller(isim) Values(?)", (il.isim, ))
        con.commit()
        con.close()

    # Tablodan Veri Silinmesi
    @staticmethod
    def VeriSil(il):
        con = VeriTabani.Baglanti()
        cursor = con.cursor()
        cursor.execute("Delete From Iller Where ID = ?", (il.ID, ))
        con.commit()
        con.close()

    # Tablodan Veri Güncellenmesi
    @staticmethod
    def VeriGuncelle(eskiVeriID: int, yeniVeri):
        con = VeriTabani.Baglanti()
        cursor = con.cursor()
        cursor.execute("Update Iller Set isim = ? Where ID = ?", (yeniVeri.isim, eskiVeriID))
        con.commit()
        con.close()


# Veri Tabanında Bulunan 'Ilceler' Tablosu Varlığı
class Ilceler():
    def __init__(self, ID = 0, isim = ""):
        self.ID = ID
        self.isim = isim
        self.il = Iller()

    def __str__(self):
        return self.isim

    # Tabloda Bulunan Tüm Verilerin Çekilmesi
    @staticmethod
    def TumVerileriGetir():
        ilceler = VeriTabani.TumKayitlariGetir(Ilceler.__name__)
        liste = []

        for ID, isim, il_ID in ilceler:
            ilce = Ilceler()
            ilce.ID = ID
            ilce.isim = isim
            ilce.il = Iller.IDIleVeriGetir(il_ID)
            liste.append(ilce)

        return liste

    # Talodan ID İle Veri Çekilmesi
    @staticmethod
    def IDIleVeriGetir(ID: int):
        kayit = VeriTabani.IDIleKaydiGetir(Ilceler.__name__, ID)
        ilce = Ilceler()
        ilce.ID = kayit[0]
        ilce.isim = kayit[1]
        ilce.il = VeriTabani.IDIleKaydiGetir(Iller.__name__, kayit[2])
        return ilce
