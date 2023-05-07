from utils.app import *

from collections import deque

def reverse_string(x: str):
    """Fungsi untuk reverse string"""
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

    option_str = "\n[text_default]"
    for k, v in option.items():
        option_str += f"{k}. {v}\n"

    menu_str = "\n[text_default]"
    for k, v in menu.items():
        menu_str += f"{k}. {v}\n"

    panel_description = Panel(program4.description, title="[text_title]Deskripsi Program", title_align="left", style="default")
    panel_option = Panel(option_str, title="[text_title]Opsi Reverse String", title_align="left", style="default")
    panel_menu = Panel(menu_str, title="[text_title]Menu", title_align="left", style="default")

    while True:
        console.clear()
        console.rule(program4.title, style="default")
        console.print(Padding(panel_description, pad=(1, 0, 0, 0)))

        while True:
            input_string = Prompt.ask("[bold]\nHai👋! Masukkan string yang ingin di dibalik, lalu klik 'enter'\n")
            if input_string == "":
                console.print("[prompt.invalid]String tidak boleh kosong!")
            else:
                break

        count = 0
        while True:
            console.clear()
            console.rule(program4.title, style="default")

            if count == 0:
                console.print(Padding(panel_option, pad=(1, 0, 0, 0)))
                opt = IntPrompt.ask("\n[bold]Pilih Opsi", choices=[str(i) for i in option.keys()])
                
                import getpass
                match opt:
                    case 1:
                        console.clear()
                        console.rule(program4.title, style="default")

                        original_string = Panel(f"\n[text_default]{input_string}\n", title="[text_title]Original String", style="default")
                        reversed_string = Panel(f"\n[text_default]{reverse_string(input_string)}\n", title="[text_title]Reversed String", style="default")

                        console.print(Padding(original_string, pad=(1, 0, 0, 0)))
                        console.print(Padding(reversed_string, pad=(1, 0, 0, 0)))

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

                        console.clear()
                        console.rule(program4.title)

                        original_string = Panel(f"\n[text_default]{input_string}\n", title="[text_title]Original String", style="default")
                        reversed_string = Panel(f"\n[text_default]{result}\n", title="[text_title]Reversed String", style="default")

                        console.print(Padding(original_string, pad=(1, 0, 0, 0)))
                        console.print(Padding(reversed_string, pad=(1, 0, 0, 0)))

                        getpass.getpass("\nKlik 'enter' untuk melanjutkan")
                        count += 1
                        continue

            console.print(Padding(panel_menu, pad=(1, 0, 0, 0)))
            opt = IntPrompt.ask("\n[bold]Pilih Menu", choices=[str(i) for i in menu.keys()])

            match opt:
                case 1:
                    count += 1
                    break
                case 2:
                    count = 0
                    continue
                case 3:
                    return program4.stop()

title = "[text_title]Program 4: Reverse String" # untuk di tampilkan sebagai judul
name = "Reverse String" # untuk di tampilkan di list menu
description = """[text_default]
🔷 Ini merupakan program untuk membalikkan string.
🔷 Program ini mengimplementasikan struktur data tumpukan (stack) untuk membalikkan string.
🔷 Pada program ini terdapat fitur untuk membalikkan string keseluruhan dan membalikkan string perkata.\n""" # deskripsi program
program4 = App(name=name, title=title, description=description, program=main)

if __name__ == "__main__":
    program4.start()
