#module
import os

os.system('clear')

print '=========================='
print '[1] Perjumlahan'
print '[2] Perkalian'
print '[3] Pengurangan'
print '[4] Pembagian'
pilih = input('Masukan Pilihan Anda : ')
if pilih == 1:
  print
  angka_1 = input('Angka Ke1 : ')
  angka_2 = input('Angka Ke2 : ')
  total = angka_1 + angka_2
  print'Hasil: ',total


elif pilih == 2:
  print
  angka_1 = input('Angka Ke1 : ')
  angka_2 = input('Angka Ke2 : ')
  total = angka_1 * angka_2
  print'Hasil: ',total
  
