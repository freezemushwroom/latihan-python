# tes membuat file dan menulis file
"""
buka_File = open("file_Baru.txt", "w")

buka_File.write("Hello World")

buka_File.close()

# ini tes membuat file, lalu menuliskan isinya. Atau menulis ulang isinya bila sudah ada filenya
"""
"""
baca_File = open("file_Baru.txt", "r")

print(baca_File.read())

baca_File.close()

# berikut adalah tes membuka file lalu membaca isinya

"""
"""
with open("file_Baru.txt", "w") as f:
    f.write("Hello\n")
    for o in range(10):
        f.write("Awkwkkwkwkw\n")

"""
"""""
with open("file_Baru.txt", "r") as b:
    baca = b.readline()  # ini untuk membaca per linenya
    # baca = b.readlines()untuk ini bakal membaca semua line di dalam file, 
    # setelah ini bila memanggil print lagi akan mengembalikan line kosong
    print(baca)
    for o in b:
        print(b.read(), end='')
        
# ini adalah bentuk lain untuk membaca file

"""
"""""
# berikut adalah cara untuk mengkopi isi dari satu file ke file lainnya

with open("file_Baru.txt", "r") as b:
    with open("file_Lain.txt", "w") as f:
        for o in b:
            f.write(o)
"""
# sekian adalah catatan singkat untuk membuat file di python


# batas
