# tes border python

import time
import os
# import pyautogui
# import subprocess



"""
for i in range(9):
    print("=====", end="")#make end biar ga ngebuat newline
    # kalau dihitung ada 11×4 = 44 line
#print("=")

"""

# dengan ini total linenya ada 45


def batasan():
    print("\n\n\n")
    time.sleep(1.2)
    for i in range(9):
        print("=====", end="")
        time.sleep(0.2)
    print("\n")
    time.sleep(0.4)
    return True


def hapus():
    time.sleep(0.5)
    os.system('cls')
    return True


def garis_baru(jumlah):
    for i in range(jumlah):
        print("\n")
    return 1
"""
print("ohohohohohoohoho")
time.sleep(2)
"""
# os.system('clear')  # pakai cara ini tidak berhasil, 'clear' is not recognized as an internaal or external command
# os.system("cls")  # pakai cara ini tidak berhasil, tidak melakukan apa-apa
# print("\033[H\033[J")  # pakai cara ini tidak berhasil, tidak melakukan apa-apa
# pyautogui.clear()  # cara ini tidak bisa, karena modul pyautogui tidak bisa clear screen dengan sendirinya
"""
os.system('cls')
print("\033c", end="")
"""  # tidak berguna juga

# subprocess.call('cls', shell=True)  # ini juga tidak bisa, untuk clear screen di laptop memerlukan cara lain.
# saat ini belum ada caranya di laptop

# batas
