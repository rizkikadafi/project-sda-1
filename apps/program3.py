from utils.app import App
from collections import deque

def main():
    stack = deque()

    menu = {
        1: "Tambahkan data",
        2: "Hapus data teratas",
        3: "Tampilkan data teratas",
        4: "Tampilkan seluruh data (Dengan penghapusan!)",
        5: "Tampilkan seluruh data (Tanpa penghapusan)",
        6: "Keluar program"
    }   

    count = 0
    while True:
        if count > 0:
            program3.clear()
            print(program3.title)

        print("Menu Program:")
        for i, k in menu.items():
            print(f"{i}. {k}")

        opt = program3.prompt_options("\nPilih menu", [i for i in menu.keys()])

        import getpass
        match opt:
            case 1:
                data = input("Masukkan data: ")
                stack.append(data)
                print(f"\n[{data}] telah dimasukkan.")
                getpass.getpass("\nKlik 'enter' untuk melanjutkan")
            case 2:
                if len(stack) == 0:
                    print("\nData Kosong! Tidak ada data yang bisa dihapus!")
                    getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
                else:
                    data = stack.pop()
                    print(f"\n[{data}] telah dihapus!")
                    getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 3:
                if len(stack) == 0:
                    print("\nData Kosong! Tidak ada data teratas yang bisa ditampilkan!")
                    getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
                else:
                    print(f"\nData teratas adalah [{stack[-1]}]")
                    getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 4:
                if len(stack) == 0:
                    print("\nData Kosong! Tidak ada data yang bisa ditampilkan!")
                    getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
                else:
                    print()
                    while len(stack) > 0:
                        print(stack.pop())
                    print("\nData telah dikosongkan!")
                    getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 5:
                data = [i for i in stack] 
                if len(data) == 0:
                    print("\nData Kosong! Tidak ada data yang bisa ditampilkan!")
                else:
                    print()
                    while len(data) > 0:
                        print(data.pop())
                getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 6:
                return program3.stop()

        count += 1

title = "========== Program 3: Implementasi Tumpukan Tanpa Batasan Data ==========\n" # untuk di tampilkan sebagai judul
name = "Tumpukan Tanpa Batasan Data" # untuk di tampilkan di list menu
description = ("""Deskripsi Program:
Ini merupakan program implementasi struktur data tumpukan (stack) dengan menggunakan class deque pada python. 
Pada program ini, maksimal data yang dapat dimasukkan tidak dibatasi.\n""", False) # deskripsi program
program3 = App(name=name, title=title, description=description, program=main)

if __name__ == "__main__":
    program3.start()
