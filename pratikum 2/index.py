soal1="/---------Biodata diri-------------/"
nama="Ahmad Hilmy"
nim="0110223148"
No_telepon="088214612609"
alamat="Kp.sugutamu"
pembatas="/----------------------------------------------------------------/"

print(soal1)
print("Nama :",nama)
print("Nim :",nim)
print("No telepon :",No_telepon)
print("Alamat :",alamat)
print("")
print(pembatas)
print("")
print("")

soal2="/---------Biodata diri-------------/"
nama="Agas Triawan"
nim="0110223161"
alamat="Tapos Depok"
No_telepon="088295747113"
pembatas="/----------------------------------------------------------------/"

print(soal2)
print("Nama :",nama)
print("Nim :",nim)
print("Alamat :",alamat)
print("No telepon :",No_telepon)
print("")
print(pembatas)
print("")
print("")

soal3="/--------------/berat badan ideal--------"
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

soal4="/-----------------nilai konversi dari celcius ke fahreinheit -------------------"
print('##  Program Python Konversi Suhu  ##')
print('====================================')
print()
 
celc = float(input('Input suhu celsius: '))
 
agas = (9/5 * celc) + 32
faiz = celc + 273.15
akbar = celc * (4/5)
 
print(celc,'derajat Celsius =',agas,'derajat Agas')
print(celc,'derajat Celsius =',faiz,'derajat Faiz')
print(celc,'derajat Celsius =',akbar,'derajat Akbar')

print ("--- Program Menghitung Volume dan Luas tabung motubablog ---\n")

tinggi=int(input("Masukan Tinggi : "))
jari=int(input("Masukan Jari-jari Lingkaran : "))

phi=22/7

luas=int(2*phi*jari*(tinggi+jari))
volume=int((phi*(jari*jari))*tinggi)

print ("Luas tabung = ", luas)
print ("Volume tabung = ", volume)