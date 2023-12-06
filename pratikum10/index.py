hasil_akhir = [
    {'nama': 'Reza', 'nilai': 70},
    {'nama': 'Ciut', 'nilai': 63},
    {'nama': 'Dian', 'nilai': 80},
    {'nama': 'Badu', 'nilai': 40}
]

siswa_lulus = [siswa['nama'] for siswa in hasil_akhir if siswa['nilai'] > 65]

buah_buahan = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']


balikan_list = []
for i in range(len(buah_buahan) - 1, -1, -1):
    balikan_list.append(buah_buahan[i])
buah_buahan = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

duplikasi_list = []
for buah in buah_buahan:
    duplikasi_list.append(buah)
    duplikasi_list.append(buah)

s = 'NurulFikri'

print(siswa_lulus)
print(balikan_list)
print(duplikasi_list)
print(s.replace('i', '').replace('u',''))


