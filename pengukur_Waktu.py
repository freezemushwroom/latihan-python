# program untuk mengambil waktu dan mengembalikkannya dalam bentuk yang diinginkan, tinggal import aja
# kalau di laptop mungkin setting tanggal bukan dalam indonesia, masih pakai bahasa inggris

"""""
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



import time


def tanggal_():
    waktu_ini = time.strftime("Tanggal: %d:%m:%Y")
    return waktu_ini


def tanggal_digit():
    waktu_ini = time.strftime("%d:%m:%Y")
    return waktu_ini


def waktu_():
    waktu_ini = time.strftime("Waktu: %H:%M:%S")
    return waktu_ini


def waktu_digit():
    waktu_ini = time.strftime("%H:%M:%S")
    return waktu_ini


def tanggal_nama():
    waktu_ini = time.strftime("Hari: %A, Bulan: %B")
    return waktu_ini


def jam():
    waktu = time.strftime("%H")
    return waktu


def menit():
    waktu = time.strftime("%M")
    return waktu


def detik():
    waktu = time.strftime("%S")
    return waktu


def hari_digit():
    waktu = time.strftime("%d")
    return waktu


def hari():
    waktu = time.strftime("%A")
    return waktu


def bulan_digit():
    waktu = time.strftime("%m")
    return waktu


def bulan():
    waktu = time.strftime("%B")
    return waktu


def tahun():
    waktu = time.strftime("%Y")
    return waktu


def zona_waktu():
    waktu = time.strftime("%Z")
    return waktu


def hari_dminggu():
    waktu = time.strftime("%w")
    return waktu


def hari_dindo():
    urutan_hari = {"0": 'Minggu', "1": 'Senin', "2": 'Selasa', "3": 'Rabu', "4": 'Kamis', "5": 'Jumat', "6": 'Sabtu'}
    waktu = time.strftime("%w")
    hari_ini = urutan_hari[waktu]  # mengembalikan nama hari dalam indonesia
    return hari_ini


def tidur(x):
    time.sleep(x)
    return 0

# batas
