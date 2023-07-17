# status: selesai testing, berhasil
# versi: 1.1

import time


tidur_Siang = 0
sibuk_tanda = 0
status_Iya = ["Iya", "Ya", "Benar", "Betul", "Yes", "Yoi", "Sangat", "Ja"]
status_Tidak = ["No", "Tidak", "Nggak", "Ngak", "Ngggak", "Mungkin", "Nah", "Nahh", "Nahhh", "Maybe"]
Input_berhasil = 1
pembanding = "nothing"
i = 0
a = 0
juml = 0
list_Kegiatan = []


def prioritas_kegiatan(arg):  # 'arg' sebelumnya adalah 'sibuk_tanda' tapi diganti supaya mengshadow variabelnya
    global i, a, Input_berhasil, pembanding
    print("Silahkan tulis kegiatan anda untuk hari ini: \n")
    if arg == 1:
        for i in range(3):
            i = i + 1
            print("Kegiatan ke", i)
            kegiatan = input(" :")
            list_Kegiatan.append(kegiatan)
        while Input_berhasil:
            konfirmasi = input("Apakah ada kegiatan lain?: ")
            pembanding = konfirmasi.capitalize()
            # print(pembanding)
            if pembanding in status_Tidak[:]:
                Input_berhasil = 0
                i = 3
            if pembanding in status_Iya[:]:
                for a in range(2):
                    a = a + 1
                    print("Tambahan ke", a)
                    kegiatan = input(" :")
                    list_Kegiatan.append(kegiatan)
                Input_berhasil = 0
                i = 5

    else:
        for i in range(5):
            i = i + 1
            print("Kegiatan ke", i)
            kegiatan = input(" :") 
            list_Kegiatan.append(kegiatan)
        i = 5
    return i


def sibuk(jam_t):
    global tidur_Siang, sibuk_tanda, juml
    sibuk_tanda = 1
    print("\n\n\n")
    if jam_t < 6:
        tidur_Siang = 1
        juml = prioritas_kegiatan(sibuk_tanda)  # 3 atau 5
        list_Kegiatan.append("Tidur")  # 4 atau 6
    else:
        tidur_Siang = 0
        juml = prioritas_kegiatan(sibuk_tanda)
    return juml


def tidak_sibuk(jam_t):
    global tidur_Siang, sibuk_tanda, juml  # variable global harus di declare
    sibuk_tanda = 0
    print("\n\n\n")
    if jam_t < 6:
        tidur_Siang = 1
        juml = prioritas_kegiatan(sibuk_tanda)  # 5
        list_Kegiatan.append("Tidur")  # 6
    else:
        tidur_Siang = 0
        juml = prioritas_kegiatan(sibuk_tanda)
    return juml


# main program  ↓
print("Halo Selamat pagi!\n\n\n")

Jam_tidur = int(input("Berapa jam tidur anda?: "))
jumlah = 0

while Input_berhasil:
    Status_sibuk = input("\nApakah anda sibuk hari ini?: ")
    pembanding = Status_sibuk.capitalize()  # harus begini karna tidak meghubah value awalnya
    if pembanding in status_Iya[:]:
        jumlah = sibuk(Jam_tidur)
        Input_berhasil = 0
    if pembanding in status_Tidak[:]:
        jumlah = tidak_sibuk(Jam_tidur)
        Input_berhasil = 0
time.sleep(0.8)
print("\n\n\nSemangat Kak, hari ini kamu ada ", jumlah, " kegiatan: \n")
time.sleep(1.2)
print("Yaitu: \n")
time.sleep(0.4)
for oh in range(3):  # kalau sudah memakai 'variable' in range(), maka tidak perlu lagi variable = variable + 1
    print(list_Kegiatan[oh], "\n")
    time.sleep(0.6)

if sibuk_tanda == 1 and a > 0:
    print("Dan juga tambahan 2 kegiatan, yaitu: \n")
    for oh in range(3, 5):
        print(list_Kegiatan[oh], "\n")
        time.sleep(0.6)
elif sibuk == 1 and a == 0:
    print("")

else: 
    for oh in range(3, 5):
        print(list_Kegiatan[oh], "\n")
        time.sleep(0.6)


if tidur_Siang == 1:
    print("\nSerta Prioritasmu adalah Tidur siang!!!")    
else:
    print("\nTidur bukanlah prioritas")


print("\n\nSemangat melakukan kegiatanmu!")
# batas
