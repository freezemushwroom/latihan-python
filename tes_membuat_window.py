# tes membuat window baru GUI

# sebelum melanjutkan lagi, kuputuskan untuk mempelajari tentang class dahulu

import tkinter as tk
# import pengukur_Waktu as pW

"""""
def create_window():
    window = tk.Tk()
    label = tk.Label(window, text="Hello, Tkinter!")
    label.pack()
    window.mainloop()
"""

def biarin():
    isi_text.set("Namaku Bopel")


# create_window()
muncul = tk.Tk()
isi_text = tk.StringVar()


tampil = tk.Label(muncul, textvariable = isi_text )
tampil.pack()
isi_text.set("Halo, salam kenal!")
tampil.after(2000, biarin)  # akhirnya berhasil mengubah teks dengan menggunakna after()


muncul.mainloop()


"""""
# bingung mau gimana lagi nanti dilanjtuin logikanya

root = tk.Tk()
frame = tk.Frame(root)


def dosomething():
    mylabel.config(text="Namaku Bopel")


mylabel = tk.Label(frame, text="Halo salam kenal", bg="red")
mylabel.pack(padx=5, pady=10)

mybutton = tk.Button(frame, text="Lanjut", command=dosomething)
mybutton.pack(padx=5, pady=10)

frame.pack(padx=5, pady=5)
root.mainloop()
"""
"""""
ide program buangan:

ide 1: mencoba membuat kode lebih efisien, tapi malah ancurin alur
@staticmethod
    def tampilkan_atau_sembunyikan_widget(buka_atau_tutup, ts_1, ts_2, ts_3, ts_4, ts_5, ts_6):
        jumlah_sementara = ts_1 + ts_2 + ts_3 + ts_4 + ts_5 + ts_6
        if buka_atau_tutup == 1:  # ini untuk menutup (1), dan semua ts_ = 1 akan ditutup. ts_ = 0 akan diabaikan
            while jumlah_sementara != 0:
                if ts_1 == 1:
                    ts_1 = 0
                    plb.nama_lantai_baru.grid_remove()
                if ts_2 == 1:
                    ts_2 = 0
                    plb.tombol_konfirmasi_1.grid_remove()
                if ts_3 == 1:
                    ts_3 = 0
                    plb.tombol_konfirmasi_2.grid_remove()
                if ts_4 == 1:
                    ts_4 = 0
                    plb.tombol_konfirmasi_3.grid_remove()
                if ts_5 == 1:
                    ts_5 = 0
                    plb.tulisan_konfirmasi.grid_remove()
                if ts_6 == 1:
                    ts_6 = 0
                    fu.tampilan_lantai_lantai.grid_remove()
        elif buka_atau_tutup == 0:  # ini untuk membuka(0), dan semua ts_ = 1 akan dibuka. ts_ = 0 akan diabaikan
            while jumlah_sementara != 0:
                if ts_1 == 1:
                    ts_1 = 0
                    plb.nama_lantai_baru.grid(row=1, column=0, columnspan=3)
                if ts_2 == 1:
                    ts_2 = 0
                    plb.tombol_konfirmasi_1.grid(row=1, column=1)
                if ts_3 == 1:
                    ts_3 = 0
                    plb.tombol_konfirmasi_2.grid(row=1, column=3)
                if ts_4 == 1:
                    ts_4 = 0
                    plb.tombol_konfirmasi_3.grid(row=1, column=3)
                if ts_5 == 1:
                    ts_5 = 0
                    plb.tulisan_konfirmasi.grid(row=0, column=1, columnspan=3)
                if ts_6 == 1:
                    ts_6 = 0
                    fu.tampilan_lantai_lantai.grid(row=4, column=3, padx=1, pady=1)
        
    nama_lantai_baru : ts_1
    tombol_konfirmasi_1 : ts_2
    tombol_konfirmasi_2 : ts_3
    tombol_konfirmasi_3 : ts_4
    tulisan_konfirmasi : ts_5
    tampilan_lantai_lantai : ts_6
        
        pass

# batas


"""


# batas
