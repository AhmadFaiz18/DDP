#<-----Nomor1----->
#Deklarasi fungsi
def data_diri():
    print("Nama saya Faiz")
    print("alamat Depok")   
    print("Gender:Laki-laki")
    print("umur:18")
    print("Hoby:Olahraga")
#Memanggil Fungsi
data_diri()

# no 2
def kelulusan(nilai):
   if nilai < 60:
       return "Gagal"
   elif 61 <= nilai <= 70:
       return "Baik"
   elif 71 <= nilai <= 80:
       return "Sangat Baik"
   elif 81 <= nilai <= 100:
       return "Istimewa"
   else:
       return "Nilai tidak valid"

print(kelulusan(61))

# no 3
def cetak_bilangan_ganjil(f):
    for i in range(1, f+1, 2):
        print(i,end=" ")

cetak_bilangan_ganjil(100)



