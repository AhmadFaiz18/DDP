class Animal:
    def __init__(self, name, makanan, hidup, berkembang_biak):
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

# Contoh penggunaan:
kucing = Animal("Harimau", "Daging", "Darat", "Vivipar")
gajah = Animal("Kambing", "Tumbuhan", "Darat", "Vivipar")

# Mengakses properti
print("Harimau makan", kucing.makanan)
print("Kambing hidup di", gajah.hidup)