# Soal No.1
# Input data
nama_kendaraan = input("Nama kendaraan: ")
jenis_bensin = input("Jenis bensin: ")
kota_tujuan = input("Kota tujuan: ")

# Data harga dan jarak tempuh
harga_per_liter = {
    "pertalite": 10000,
    "pertamax": 14000,
    "pertamax turbo": 17000
}

jarak_tempuh = {
    "pertalite": 12,
    "pertamax": 13,
    "pertamax turbo": 13.5
}

jarak_kota = {
    "jakarta": 20,
    "bekasi": 35.7,
    "depok": 5,
    "tangerang": 99,
    "bogor": 120.6
}

# Menghitung pemakaian bensin dan total biaya
pemakaian_bensin = jarak_kota[kota_tujuan] / jarak_tempuh[jenis_bensin]
total_biaya = pemakaian_bensin * harga_per_liter[jenis_bensin]

# Output data
print("Nama kendaraan:", nama_kendaraan)
print("Jenis bensin:", jenis_bensin)
print("Kota tujuan:", kota_tujuan)
print("Pemakaian bensin:", pemakaian_bensin, "liter")
print("Total biaya bensin:", total_biaya, "rupiah")

# Soal No.2
# Input data
nama_pembeli = input("Masukkan nama pembeli: ")
no_hp_pembeli = input("Masukkan nomor telepon pembeli: ")
jenis_pesanan = input("Pesan makanan atau minuman? ")
if jenis_pesanan == "makanan":
    print("Menu makanan:")
    print("1. nasi goreng (Rp. 15.000)")
    print("2. mie goreng (Rp. 12.000)")
    print("3. ayam geprek (Rp. 18.000)")
    menu = input("Masukkan pesanan: ")
    if menu == "1":
        harga = 15000
        nama_menu = "nasi goreng"
    elif menu == "2":
        harga = 12000
        nama_menu = "mie goreng"
    elif menu == "3":
        harga = 18000
        nama_menu = "ayam geprek"
    else:
        print("Menu tidak tersedia")
        exit()
elif jenis_pesanan == "minuman":
    print("Menu minuman:")
    print("1. aneka jus (Rp. 15.000)")
    print("2. soft drink (Rp. 10.000)")
    print("3. sweet ice Tea (Rp. 5.000)")
    menu = input("Masukkan pesanan: ")
    if menu == "1":
        harga = 15000
        nama_menu = "aneka Jus"
    elif menu == "2":
        harga = 10000
        nama_menu = "soft drink"
    elif menu == "3":
        harga = 5000
        nama_menu = "sweet ice tea"
    else:
        print("Menu tidak tersedia")
        exit()
else:
    print("Jenis pesanan tidak tersedia")
    exit()

jumlah_pesanan = int(input("Masukkan jumlah pesanan: "))

# Menghitung total harga
total_harga = harga * jumlah_pesanan

# Output data
print("Nama pembeli:", nama_pembeli)
print("Nomor telepon pembeli:", no_hp_pembeli)
print("Menu yang dipesan:", nama_menu)
print("Jumlah pesanan:", jumlah_pesanan)
print("Harga yang harus dibayarkan:", total_harga, "rupiah")

school_name = "STT Nurul Fikri"

student_range = 20

for i in range(1, student_range + 1):
    if i % 3 == 0:
        print(i, school_name)
    else:
        print(i)