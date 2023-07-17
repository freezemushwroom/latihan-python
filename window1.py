import tkinter as wn

print("Disini 0")  # urutan ke - 0

layar = wn.Tk()
layar.title("Lift Digital")
layar.geometry("400x400")


def lantai_atas():
    letak_anda.set("Lantai 2")
    print("Disini 8")  # urutan ke - 8 dan seterusnya
    return 0


def lantai_bawah():
    letak_anda.set("Lantai Dasar")
    print("Disini 7")  # urutan ke - dan seterusnya
    return 0


def lantai_tengah():
    letak_anda.set("Lantai 1")
    print("Disini 6")  # urutan ke - 5
    return 0


def jeda_sebentar():
    letak_anda.set("Sekarang kita ada di ...")
    print("Disini 5")  # urutan ke - 4
    return 0


print("Disini 1")  # urutan ke - 1
letak_anda = wn.StringVar()
letak_anda.set("Anda mau ke lantai apa?")

label_1 = wn.Label(layar, textvariable=letak_anda)

tombol_atas = wn.Button(layar, text="Lantai atas", command=lantai_atas)
tombol_bawah = wn.Button(layar, text="Lantai bawah", command=lantai_bawah)
label_1.after(3000, jeda_sebentar)
label_1.after(5000, lantai_tengah)  # after() sebagai fungsi delay untuk program GUI ini

print("Disini 2")  # urutan ke - 2

tombol_atas.pack()
label_1.pack()
tombol_bawah.pack()

print("Disini 3")  # urutan ke - 3

layar.mainloop()
print("Disini 4")  # kesini hanya saat window ditutup

layar.title("Lift Digital kedua 2")
layar.geometry("400x300")

tombol_atas.pack()
tombol_bawah.pack()
label_1.pack()

layar.mainloop()

