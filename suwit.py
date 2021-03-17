import time
import random

print("=" * 32)
print("""
    Selamat Datang di Game
     Batu Gunting Kertas
""")
print("=" * 32)
print("""
Silahkan Pilih : 
1. Batu
2. Gunting
3. Kertas
""")

player = int(input("Masukkan Angka : "))
com = random.randint(1, 3)

if player == 1:
    print("Kamu memilih Batu")
    if com == 1:
        time.sleep(0.5)
        print("")
        print("Lawan Memilih Batu")
        time.sleep(0.5)
        print("")
        print("Seri")
    elif com == 2:
        time.sleep(0.5)
        print("")
        print("Lawan Memilih Gunting")
        time.sleep(0.5)
        print("")
        print("Kamu Menang")
    elif com == 3:
        time.sleep(0.5)
        print("")
        print("Lawan Memilih Kertas")
        time.sleep(0.5)
        print("")
        print("Kamu Kalah")

elif player == 2:
    print("Kamu memilih Gunting")
    if com == 1:
        time.sleep(0.5)
        print("")
        print("Lawan Memilih Batu")
        time.sleep(0.5)
        print("")
        print("Kamu Kalah")
    elif com == 2:
        time.sleep(0.5)
        print("")
        print("Lawan Memilih Gunting")
        time.sleep(0.5)
        print("")
        print("Seri")
    elif com == 3:
        time.sleep(0.5)
        print("")
        print("Lawan Memilih Kertas")
        time.sleep(0.5)
        print("")
        print("Kamu Menang")

elif player == 3:
    print("Kamu memilih Kertas")
    if com == 1:
        time.sleep(0.5)
        print("")
        print("Lawan Memilih Batu")
        time.sleep(0.5)
        print("")
        print("Kamu Menang")
    elif com == 2:
        time.sleep(0.5)
        print("")
        print("Lawan Memilih Gunting")
        time.sleep(0.5)
        print("")
        print("Kamu Kalah")
    elif com == 3:
        time.sleep(0.5)
        print("")
        print("Lawan Memilih Kertas")
        time.sleep(0.5)
        print("")
        print("Seri")