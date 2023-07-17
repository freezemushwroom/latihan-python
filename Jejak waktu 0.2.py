#program nge track wakktu
#file: Jejak waktu 0.2

import time
# import os



#print(datetime.now())#metode 1
'''
ambil_Waktu = time.localtime()
waktu_Kini = time.strftime("Tanggal: %m/%d/%Y , Pukul: %H:%M:%S", ambil_Waktu)
print(waktu_Kini)
'''#metode 2
def jam_Lokal():
    Ambil_waktu = time.localtime()
    Waktu_kini = time.strftime("Tanggal: %d/%m/%Y , Pukul: %H:%M:%S")
    return Waktu_kini

print(jam_Lokal())
print("\n")
print(time.ctime())  # ini untuk menunjukkan tanggal dan waktu saat ini
#jujur aja lebih milih metode 2
#karna hanya ngambil data yang diperlukan dari tuple struct_time
"""
Urutan tuple struct_time:

year
month
day
hour
minute
second
weekday
day of the year
daylight saving

dan directivenya

%a = nama singkat weekday dalam bahasa lokal
%A = nama lengkap weekday dalam bahasa lokal
%b = nama singkat bulan dalam bahasa lokal
%B = nama lengkap bulan dalam bahasa lokal
%c = representasi dari tanggal dan waktu
%d = hari di bulan dalam decimal
%H = jam(24 jam) dalam decimal
%I = jam(12 jam) dalam decimal
%j = hari dalam tahun itu dalam decimal
%m = bulan dalam decimal
%M = menit dalam decimal
%p = bentuk lokal dari AM atau PM
%S = detik dalam bentuk decimal
%U = mingguan dalam satu tahun dalam bentuk decimal (Minggu adalah hari pertama dalam satu minggu)
%w = hari dalam minggu dalam bentuk decimal (minggu adalah hari pertama) dimana minggu = 0 dan sabtu = 6
%W = mingguan dalam satu tahun dalam bentuk decimal (Senin adalah hari pertama dalam satu minggu)
%x = representasi tanggal dalam bentuk lokal
%X = representasi waktu dalam bentuk lokal
%y = tahun tanpa abad dalam bentuk decimal
%Y = tahun dengan abad dalam bentuk decimal
%z = perbedaan jam dari UTC/GMT dalam bentuk hour/minutes dalam bentuk decimal
%Z = nama timezone
%% = sebuah karakter '%'

dan urutannya saat di print bisa diubah-ubah pula
"""

"""""
while 5>0:
    #print(datetime.now())#1
    print(jam_Lokal())#2
    time.sleep(0.01)
    os.system("cls")
"""



print(time.strftime("%Z"))


#batas