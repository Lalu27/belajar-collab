def tambah(a,b):
  return a+b
def pengurangan(a,b):
  return a-b
  
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

  elif pilihan == 2 :
    print(angka1,"-",angka2,"=", pengurangan(angka1, angka2))
  
  else:
    print(pilihan)
 
