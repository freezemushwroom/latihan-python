# program untuk mengecek rosario

"""
urutan kerja (urutan kerjanya sedikit karena menggunakan module dari program lain
1. gunakan tuple nama hari untuk mengembalikan nilai dari dictionary urutan_Peristiwa
2. catat waktu mengakses program dalam file txt
"""

import pengukur_Waktu as pW

urutan_Peristiwa = {"Senin": 'Gembira',
                    "Selasa": 'Sedih',
                    "Rabu": 'Mulia',
                    "Kamis": 'Terang',
                    "Jumat": 'Sedih',
                    "Sabtu": 'Gembira',
                    "Minggu": 'Mulia'}


def cek_akses():
    memo = open("Akses pengingat Rosario.txt", "r")
    hitung = 0
    isi = memo.read()
    urut = isi.split("\n")
    for i in urut:
        if i:
            hitung += 1
    if hitung == 0:  # apabila filenya kosong, membuat header sendiri
        with open("Akses pengingat Rosario.txt", "w") as tL:
            tL.write("Awal dari pembuatan file ini, JANGAN UBAH ISI FILE INI bila ingin bekerja dengan teratur!!!\n")
        hitung += 1
    else:
        pass
    return hitung


def catat_doa():
    with open("Akses pengingat Rosario.txt", "a+") as cD:
        o = cek_akses()  # untuk menghitung akses ke berapa
        waktu_tanggal = "\nDiakses pada, " + pW.waktu_() + " dan " + pW.tanggal_() + " , akses ke: " + str(o) + "\n"
        cD.write(waktu_tanggal)

    return "~Program Selesai"


hari = pW.hari_dindo()
print("Selamat malam Kak Rama\n")
pW.tidur(1.5)
print("Hari ini hari", hari, "\n")
pW.tidur(0.8)
print("Maka peristiwa rosarionya: ", urutan_Peristiwa[hari], "\n\n")
pW.tidur(1.2)
print("Selamat Berdoa")

print(catat_doa())

# Batas
