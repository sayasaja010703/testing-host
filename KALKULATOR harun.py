print("=== KALKULATOR SEDERHANA ===")
print("pilih operasi yang ingin anda lakukan:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("Pembagian")

choice = int(input("Masukan pilihan (1/2/3/4): "))

if choice == 1: 
     num1 = float(input("Masukan angka pertama: "))
     num2 = float(input("Masukan anda kedua: "))
     result = num1 + num2
     print ("Hasil penjumlahanya:", result)

elif choice == 3:
    num1 = float (input("Masukan angka pertama: "))
    num2 = float (input ("Masukan angka kedua: "))
    result = num1 - num2 
    print("Hasil pengurangan:", result)

elif choice == 3:
    num1 = float(input("Masukan angka pertama: "))
    num2 = float(input("Masukan angka kedua: "))
    result = num1 * num2
    print ("Hasil perkalian:", result)

elif choice == 4:
    num1 = float(input("Masukan angka pertama: "))
    num2 = float(input("Masukan angka kedua: "))
    if num2 != 0:
        result = num1 / num2
        print("Hasil pembagian:", result)
    else:
        print("Pembagian dengan nol tidak dapat dilakukan.")

else:
    print("Pilihan tidak valid. silahkan pilih antara 1, 2, 3, atau 4.")