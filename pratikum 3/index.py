soal1="/--------------/berat badan ideal--------"
def calc_BMI(berat, tinggi):

    # rumus BMI
    BMI = berat / (tinggi * tinggi)

    # bisa juga menggunakan rumus BMI dibawah ini 
    # silahkan uncomment kode dibawah dan
    # comment kode rumus BMI diatas untuk mencobanya
    # BMI = berat / tinggi**2

    # cek nilai BMI
    print("Nilai BMI anda:",BMI)

    if BMI > 22.9:
        return "Overweight"
    elif BMI < 18.5:
        return "Underweight"
    else:
        return "Normal"

berat = float(input("Berat badan (kg):"))
tinggi = float(input("Tinggi badan (m):"))

result = calc_BMI(berat, tinggi)
print("Status BMI anda saat ini:", result)

print("")
print("")

soal2 = "/---------------- Soal 2 || Bilangan Positif & Negatif ----------------/"

print(soal2)
bilangan = float(input("Masukan Bilangan: "))

if bilangan != int(bilangan):
    print("Bilangan anda bukan bilangan bulat, masukan kembali bilangan anda")
    bilangan = float(input("Masukan Bilangan: "))

if bilangan < 0:
    print(soal2)
    print("Bilangan Anda Adalah:", int(bilangan), "|| Bilangan Anda adalah Negatif")
elif bilangan > 0:
    print(soal2)
    print("Bilangan Anda Adalah:", int(bilangan), "|| Bilangan Anda adalah Positif")
else:
    print(soal2)
    print("Bilangan Anda Adalah:", int(bilangan), "|| Bilangan Anda adalah Nol")


soal3 = "/---------------- Soal 3 || Batu Gunting Kertas ----------------/"

print(soal3)
jenis_suit_1 = input("Jenis Suit Orang Pertama (Batu, Gunting, atau Kertas): ")
jenis_suit_2 = input("Jenis Suit Orang Kedua (Batu, Gunting, atau Kertas): ")

if jenis_suit_1 == jenis_suit_2:
    print(soal3)
    print("Hasilnya adalah Seri. Kedua pemain memilih", jenis_suit_1)
elif jenis_suit_1 == "Batu" and jenis_suit_2 == "Gunting" or jenis_suit_1 == "Gunting" and jenis_suit_2 == "Kertas" or jenis_suit_1 == "Kertas" and jenis_suit_2 == "Batu":
    print(soal3)
    print("Pemenangnya adalah Orang Pertama dengan pilihan", jenis_suit_1)
else:
    print(soal3)
    print("Pemenangnya adalah Orang Kedua dengan pilihan", jenis_suit_2)