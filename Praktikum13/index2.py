class Animal:
    def __init__(self, name, makanan, hidup, berkembang_biak):
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

    def _info(self):
        print("Nama:", self.name)
        print("Makanan:", self.makanan)
        print("Hidup di:", self.hidup)
        print("Berkembang biak:", self.berkembang_biak)
        print()


class Badak(Animal):
    def __init__(self, name, makanan, berat, taring):
        super().__init__(name, makanan, "Daratan", "Vivipar")
        self.berat = berat
        self.taring = taring

    def _info(self):
        print("Nama:", self.name)
        print("Makanan:", self.makanan)
        print("Hidup di:", self.hidup)
        print("Berkembang biak:", self.berkembang_biak)
        print("Berat:", self.berat, "kg")
        print("Jumlah taring:", self.taring)
        print()


class Ikan(Animal):
    def __init__(self, name, makanan, jenis, warna):
        super().__init__(name, makanan, "Air", "Ovipar")
        self.jenis = jenis
        self.warna = warna

    def _info(self):
        print("Nama:", self.name)
        print("Makanan:", self.makanan)
        print("Hidup di:", self.hidup)
        print("Berkembang biak:", self.berkembang_biak)
        print("Jenis:", self.jenis)
        print("Warna:", self.warna)
        print()


class Ular(Animal):
    def __init__(self, name, makanan, panjang, bisa_menyuntik):
        super().__init__(name, makanan, "Daratan", "Ovipar")
        self.panjang = panjang
        self.bisa_menyuntik = bisa_menyuntik

    def _info(self):
        print("Nama:", self.name)
        print("Makanan :", self.makanan)
        print("Hidup di:", self.hidup)
        print("Berkembang biak:", self.berkembang_biak)
        print("Panjang:", self.panjang, "meter")
        print("Bisa menyuntik:", self.bisa_menyuntik)
        print()


# Contoh penggunaan class Badak
badak = Badak("Badak Sumatra", "Tumbuhan", 950, 2)
badak._info()

# Contoh penggunaan class Ikan
ikan = Ikan("Ikan Arwana", "Pelet", "Arwana", "Merah gold")
ikan._info()

# Contoh penggunaan class Ular
ular = Ular("Ular Piton", "Daging", 7, False)
ular._info()
