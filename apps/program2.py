from utils.app import App
from data_structure.stack import Stack

def main():
    while True:
        maks = input("Masukkan maksimal daya tampung data [bilangan bulat] (1): ")
        if not maks.isdecimal():
            print("Input yang anda masukkan tidak valid!\n")
        else:
            maks = int(maks)
            break

    stack = Stack(maks)
    program2.clear()
    print(program2.title)

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
            program2.clear()
            print(program2.title)

        print("Menu Program:")
        for i, k in menu.items():
            print(f"{i}. {k}")

        opt = program2.prompt_options("\nPilih menu", [i for i in menu.keys()])

        import getpass
        match opt:
            case 1:
                data = input("Masukkan data: ")
                if stack.full():
                    print(f"\nData telah penuh! [{data}] tidak dimasukkan!")
                    getpass.getpass("\nKlik 'enter' untuk melanjutkan")
                else:
                    stack.push(data)
                    print(f"\n[{data}] telah dimasukkan.")
                    getpass.getpass("\nKlik 'enter' untuk melanjutkan")
            case 2:
                if stack.empty():
                    print("\nData Kosong! Tidak ada data yang bisa dihapus!")
                    getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
                else:
                    data = stack.pop()
                    print(f"\n[{data}] telah dihapus!")
                    getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 3:
                if stack.empty():
                    print("\nData Kosong! Tidak ada data teratas yang bisa ditampilkan!")
                    getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
                else:
                    print(f"\nData teratas adalah [{stack.peek()}]")
                    getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 4:
                if stack.empty():
                    print("\nData Kosong! Tidak ada data yang bisa ditampilkan!")
                    getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
                else:
                    print("Berikut adalah data dalam tumpukan:")
                    while not stack.empty():
                        print(stack.pop())
                    print("\nData telah dikosongkan!")
                    getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 5:
                data = [i for i in stack._stack] 
                if len(data) == 0:
                    print("\nData Kosong! Tidak ada data yang bisa ditampilkan!")
                else:
                    print("Berikut adalah data dalam tumpukan:")
                    while len(data) > 0:
                        print(data.pop())
                getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 6:
                return program2.stop()

        count += 1

title = "========== Program 2: Implementasi Tumpukan dengan Array ==========\n" # untuk di tampilkan sebagai judul
name = "Tumpukan dengan Array" # untuk di tampilkan di list menu
description = ("""Deskripsi Program:
* Ini merupakan program implementasi struktur data tumpukan (stack) dengan menggunakan array. 
* Program ini memiliki fitur untuk menambahkan, menampilkan dan menghapus data.
* Pada program ini, maksimal data yang dapat dimasukkan dibatasi.\n""", False) # deskripsi program
program2 = App(name=name, title=title, description=description, program=main)

if __name__ == "__main__":
    program2.start()
