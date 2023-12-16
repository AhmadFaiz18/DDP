from Gempa import *

gempa_pertama = Gempa ("Banten",1.2)
gempa_kedua = Gempa ("Palu",6.1)
gempa_ketiga = Gempa ("Cianjur",5.1)
gempa_keempat = Gempa ("Jayapura",3.1)
gempa_kelima = Gempa ("Garut",4.1)

print('=== Gempa Bumi Info ===')
print()
gempa_pertama.dampak(1.2)
print('=== Gempa Bumi Info ===')
print()
gempa_kedua.dampak(6.1)
print('=== Gempa Bumi Info ===')
print()
gempa_ketiga.dampak(5.1)
print('=== Gempa Bumi Info ===')
print()
gempa_keempat.dampak(3.1)
print('=== Gempa Bumi Info ===')
print()
gempa_kelima.dampak(4.1)


