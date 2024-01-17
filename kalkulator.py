def tambah(bil_a,bil_b):
  return bil_a+bil_b
def perkalian(bil_a,bil_b):
  return bil_a*bil_b

print("Pilih operasi :")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")

pilihan = input("Masukkan Pilihan (1/2/3) :")

if pilihan in ('1','2','3'):
  angka1 = int(input("Masukkan bilangan pertama :"))
  angka2 = int(input("Masukkan bilangan kedua :"))
  
  if pilihan == 1:
    print(angka1,"+",angka2,"=", tambah(angka1, angka2))
  elif pilihan == 3:
    print(angka1,"*",angka2,"=", tambah(angka1, angka2))
  else:
    print("Pilihan tidak valid")
