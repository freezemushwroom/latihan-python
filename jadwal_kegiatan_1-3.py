# status: selesai testing, berhasil
# versi: 1.1

# !!!Pelajaran penting: Kalau mau buat decision making yang menggunakan if - elif - else
# sebaiknya setelah statement if pertama dilanjutkan dengan elif dan bukan if lagi
# karna, mungkin sistem akan mengganggap if berikutnya adalah rentetan statement yang berbeda
# hingga menyebabkan sistem untuk melakukan pengecekkan ulang lagi ke awal program
# atau ke statement if/elif/else lainnya yang ada di tingkat atasnya
# ( tingkat diatasnya = yang tidak dalam indent yang sama)
# intisari: kalau mau pakai if, statement selanjutnya pakai elif atau else, jangan if lagi apabila bandingin yang sama

import pengukur_Waktu as pW
import modul_Border as mB
import manipulator_File as mF

tidur_Siang = 0
sibuk_tanda = 0
status_Iya = ["Iya", "Ya", "Benar", "Betul", "Yes", "Yoi", "Sangat", "Ja"]
status_Tidak = ["No", "Tidak", "Nggak", "Ngak", "Ngggak", "Mungkin", "Nah", "Nahh", "Nahhh", "Maybe"]
Input_berhasil = 1
pembanding = "nothing"
juml = 0
list_Kegiatan = []


def prioritas_kegiatan(arg):  # 'arg' sebelumnya adalah 'sibuk_tanda' tapi diganti supaya mengshadow variabelnya
    global Input_berhasil, pembanding, sibuk_tanda
    o = 0
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
                o = 3
                sibuk_tanda = 0
            elif pembanding in status_Iya[:]:
                for a in range(2):
                    a = a + 1
                    print("Tambahan ke", a)
                    kegiatan = input(" :")
                    list_Kegiatan.append(kegiatan)
                Input_berhasil = 0
                o = 3
                sibuk_tanda = 1

    elif arg != 1:
        for o in range(5):
            o = o + 1
            print("Kegiatan ke", o)
            kegiatan = input(" :") 
            list_Kegiatan.append(kegiatan)
        o = 5
        sibuk_tanda = 2
    return o


def kesibukan(jam_t, arg):
    global tidur_Siang, juml
    print("\n\n\n")
    if jam_t < 6:
        tidur_Siang = 1
        juml = prioritas_kegiatan(arg)  # 3 atau 5
        list_Kegiatan.append("Tidur")  # 4 atau 6
    else:
        tidur_Siang = 0
        juml = prioritas_kegiatan(arg)
    return juml


def memprint(nf):
    mF.tambah_file(nf, "\n==============================\n")  # sebagai pembatas antar bagian
    mF.tambah_file(nf, "Berikut adalah hal yang perlu dilakukan: ")
    for i in range(len(list_Kegiatan[:])):  # dengan begini i adalah angka dan bukan isi dati listnya
        mF.tambah_file(nf, list_Kegiatan[i])  # disini mengisi list kegiatan
    mF.tambah_file(nf, pW.waktu_digit())  # disini menaruh file waktu
    mF.tambah_file(nf, pW.tanggal_digit())  # disini menaruh file tanggal
    pW.tidur(0.4)
    return "\nProses selesai"


# main program  ↓
mB.batasan()  # ini berhasil
pW.tidur(0.2)
watang = pW.tanggal_() + " " + pW.waktu_()
print(watang)
print("Halo Selamat pagi!\n\n")
aktif = 1
simpen_ga = 1
pasti = 1

while aktif:
    Jam_tidur = int(input("\nBerapa jam tidur anda?: "))
    jumlah = 0

    while Input_berhasil:
        Status_sibuk = input("\nApakah anda sibuk hari ini?: ")
        pembanding = Status_sibuk.capitalize()  # harus begini karna tidak meghubah value awalnya
        if pembanding in status_Iya[:]:
            sibuk_tanda = 1
            jumlah = kesibukan(Jam_tidur, sibuk_tanda)
            Input_berhasil = 0
        elif pembanding in status_Tidak[:]:
            sibuk_tanda = 0
            jumlah = kesibukan(Jam_tidur, sibuk_tanda)
            Input_berhasil = 0
    pW.tidur(0.8)
    print("\n\n\nSemangat Kak, hari ini kamu ada ", jumlah, " kegiatan: \n")
    pW.tidur(1.2)
    print("Yaitu: \n")
    pW.tidur(0.4)
    for oh in range(3):  # kalau sudah memakai 'variable' in range(), maka tidak perlu lagi variable = variable + 1
        print(list_Kegiatan[oh], "\n")
        pW.tidur(0.6)

    if jumlah == 0:
        print("ERROR")
        exit()

    if sibuk_tanda == 0:
        print("")

    elif sibuk_tanda == 1:
        print("Dan juga tambahan 2 kegiatan, yaitu: \n")
        for oh in range(3, 5):
            print(list_Kegiatan[oh], "\n")
            pW.tidur(0.6)

    elif sibuk_tanda == 2:
        for oh in range(3, 5):
            print(list_Kegiatan[oh], "\n")
            pW.tidur(0.6)

    if tidur_Siang == 1:
        print("\nSerta Prioritasmu adalah Tidur siang!!!")
    else:
        print("\nTidur bukanlah prioritas")

    mB.garis_baru(1)
    pW.tidur(0.4)
    while simpen_ga:
        opsi_save = input("Apakah anda ingin menyimpan data ini?: ")
        pembanding = opsi_save.capitalize()
        pW.tidur(0.2)
        if pembanding in status_Iya[:]:  # jangna lupa setelah input di kapitalisasi
            simpen_ga = 0
            while pasti:
                nama_file = input("\nMasukkan nama file yang ingin anda simpan: ")
                pW.tidur(0.2)
                cek_ = mF.cek_file(nama_file)
                if cek_ is False:
                    pW.tidur(0.2)
                    print("File tersebut belum ada, saya akan buatkan file itu")
                    pW.tidur(0.6)
                    print(memprint(nama_file))
                    aktif = 0
                    pasti = 0

                elif cek_ is True:
                    pW.tidur(0.2)
                    print("File tersebut sudah ada, data akan segera sata tambahkan")
                    Input_berhasil = 1
                    while Input_berhasil:
                        tulis_ulang = input("Apakah kakak ingin menggunakan file ini? ")
                        pembanding = tulis_ulang.capitalize()
                        if pembanding in status_Iya[:]:
                            Input_berhasil = 0
                            pW.tidur(0.2)
                            print(memprint(nama_file))
                            pasti = 0
                        elif pembanding in status_Tidak[:]:
                            Input_berhasil = 0
                            pW.tidur(0.2)
                            pass

        elif pembanding in status_Tidak[:]:
            mB.garis_baru(2)
            simpen_ga = 0
            # break

    print("\n\nSemangat melakukan kegiatanmu!")  # program selesai
    pW.tidur(2)
    aktif = 0
# belum implemetn fitur taroh di txt.file


# batas
