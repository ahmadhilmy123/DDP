# no 1
def hello():
    print("hallo nama saya adalah Ahmad Hilmy")
    print("saya tinggal di Depok")
    print("saya adalah Seorang Laki-Laki")
    print("umur saya 18 tahun")
    print("hobis saya yaitu Berenang")

hello()

# no 2
def mencari_nilai(nilai):
    if nilai < 60:
        print("Nilai Anda Adalah:", int(nilai), "|| Nilai Anda Gagal")
    elif 61 <= nilai <= 70:
        print("Nilai Anda Adalah:", int(nilai), "|| Nilai Anda Baik")
    elif 71 <= nilai <= 80:
        print("Nilai Anda Adalah:", int(nilai), "|| Nilai Anda Sangat Baik")
    elif 81 <= nilai <= 100:
        print("Nilai Anda Adalah:", int(nilai), "|| Nilai Anda Istimewa")
    else:
        print("Input tidak valid. Masukkan nilai antara 0 dan 100.")


nilaisiswa = float(input("Masukkan Nilai Anda: "))
mencari_nilai(nilaisiswa)

# no 3
def mencari_ganjil(angka):
    number = 1
    while number <= angka:
        print(number, end=', ')
        number += 2

nilaiganjil = float(input("Masukkan Angka: "))
mencari_ganjil(nilaiganjil)