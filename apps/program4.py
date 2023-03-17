from utils.app import App
from collections import deque

def reverse_string(x: str):
    stack = deque(x)

    hasil_akhir = ""

    while len(stack) != 0:
        hasil_akhir += stack.pop()

    return hasil_akhir

def main():
    option = {
        1: "Membalikkan keseluruhan string",
        2: "Membalikkan string per kata",
    }

    menu = {
        1: "Masukkan string baru",
        2: "Kembali",
        3: "Keluar program"
    }

    count = 0
    while True:
        if count > 0:
            program4.clear()
            print(program4.title)

        input_string = input("Hai! Masukkan string yang ingin di dibalik, lalu klik enter:\n")

        count = 0
        while True:
            program4.clear()
            print(program4.title)
            print(f"Original String:\n{input_string}\n")

            if count == 0:
                print("Opsi Reverse String:")
                for k, v in option.items():
                    print(f"{k}. {v}")
                    
                opt = int(program4.prompt_options(word="\nPilih Opsi:", opts=[i for i in option.keys()]))
                
                import getpass
                match opt:
                    case 1:
                        program4.clear()
                        print(program4.title)
                        print(f"Original String:\n{input_string}\n")

                        print(f"Berikut ini adalah string yang sudah dibalik:\n{reverse_string(input_string)}")

                        getpass.getpass("\nKlik 'enter' untuk melanjutkan")
                        count += 1
                        continue
                    case 2:
                        words = [word for word in input_string.split()]
                        reverse_stack_words = deque()

                        while len(words) > 0:
                            reverse_stack_words.append(reverse_string(words.pop()))

                        result = ""
                        while len(reverse_stack_words) > 0:
                            result += reverse_stack_words.pop() + " "

                        program4.clear()
                        print(program4.title)
                        print(f"Original String:\n{input_string}\n")

                        print(f"Berikut ini adalah string yang sudah dibalik:\n{result}")

                        getpass.getpass("\nKlik 'enter' untuk melanjutkan")
                        count += 1
                        continue

            print("Pilih Menu:")
            for k, v in menu.items():
                print(f"{k}. {v}")

            opt = int(program4.prompt_options(word="\nPilih Opsi:", opts=[i for i in menu.keys()]))

            match opt:
                case 1:
                    count += 1
                    break
                case 2:
                    count = 0
                    continue
                case 3:
                    return program4.stop()

title = "========== Program 4: Reverse String ==========\n" # untuk di tampilkan sebagai judul
name = "Reverse String" # untuk di tampilkan di list menu
description = ("""Deskripsi Program:
* Ini merupakan program untuk membalikkan string.
* Program ini mengimplementasikan struktur data tumpukan (stack) untuk membalikkan string.
* Pada program ini terdapat fitur untuk membalikkan string keseluruhan dan membalikkan string perkata.\n""", False) # deskripsi program
program4 = App(name=name, title=title, description=description, program=main)

if __name__ == "__main__":
    program4.start()
