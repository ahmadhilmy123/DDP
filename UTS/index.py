nama_variabel ='argumen'
nama_variabel ='10'

# tinggi badan saya = 58
# luas tanah = 40
# 2panjang = 105


basis1 = float(input("Masukkan basis 1: "))
basis2 = float(input("Masukkan basis 2: "))  
tinggi = float(input("Masukkan tinggi: "))


sisiA = float(input("Masukkan sisi A: "))
sisiB = float(input("Masukkan sisi B: "))
keliling = basis1 + basis2 + sisiA + sisiB


luas = 0.5 * (basis1 + basis2) * tinggi

print("Keliling trapesium adalah:", keliling)
print("Luas trapesium adalah:", luas)

# Deklarasi variabel

angka_1 = float(input("Masukan angka 1: "))
angka_2 = float(input("Masukan angka 2: "))
operator = input("Pilih operator: ")

# Pemilihan operator

if operator == "+":
    hasil = angka_1 + angka_2
elif operator == "-":
    hasil = angka_1 - angka_2
elif operator == "/":
    hasil = angka_1 / angka_2
elif operator == "*":
    hasil = angka_1 * angka_2
elif operator == "**":
    hasil = angka_1 ** angka_2

# Output

print("Angka pertama:", angka_1)
print("Angka kedua:", angka_2)
print("Pilihan Operator:", operator)
print("Hasil operator:", hasil)