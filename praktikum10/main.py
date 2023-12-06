
hasil_akhir = [
    {'nama': 'Reza', 'nilai': 70},
    {'nama': 'Ciut', 'nilai': 63},
    {'nama': 'Dian', 'nilai': 80},
    {'nama': 'Badu', 'nilai': 40}
]
siswa_lulus = [siswa['nama'] for siswa in hasil_akhir if siswa['nilai'] > 65]

print(siswa_lulus)

buah_buahan = ['pepaya','mangga','pisang','durian','jambu']
balikin_list = []
for i in range(len(buah_buahan)-1,-1,-1):
    balikin_list.append(buah_buahan[i])
buah_buahan = ['pepaya','mangga','pisang','durian','jambu']

print(balikin_list)

duplikasi_list = []
for buah in buah_buahan:
    duplikasi_list.append(buah)
    duplikasi_list.append(buah)

print(duplikasi_list)

kalimat = "NurulFikri"
konsonan_string=""
for karakter in kalimat:
    if karakter.isalpha() and karakter.lower() not in'aiueo':
        konsonan_string +=karakter

print(konsonan_string)