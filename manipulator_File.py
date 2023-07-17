# program manipulator data dalam file

import os


def format_f(file_txt):
    file_txt = file_txt + ".txt"
    return file_txt


def baca_file(file_txt):
    file_txt = format_f(file_txt)
    with open(file_txt, "r") as bf:
        print("blom ada apa apa")
        isi = bf.readlines()
        print(isi)


def cek_file(file):
    file = format_f(file)
    cek = os.path.exists(file)
    return cek  # mengembalikan True kalau ada file, False kalau tidak ada file


def tulis_file(file_txt):
    file_txt = format_f(file_txt)
    with open(file_txt, "w") as tf:
        tf.write("Blom ada apa apa")


def tambah_file(file_txt, isi):
    file_txt = format_f(file_txt)
    isi = isi + "\n"
    with open(file_txt, "a+") as tt:
        tt.write(isi)

# testing

# batas
