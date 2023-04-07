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

    option_str = "\n[bold]"
    for k, v in option.items():
        option_str += f"{k}. {v}\n"

    menu_str = "\n[bold]"
    for k, v in menu.items():
        menu_str += f"{k}. {v}\n"

    panel_description = Panel(program4.description, title="[bold #9ee5ff]Deskripsi Program", title_align="left")
    panel_option = Panel(option_str, title="[bold #9ee5ff]Opsi Reverse String", title_align="left")
    panel_menu = Panel(menu_str, title="[bold #9ee5ff]Menu", title_align="left")

    while True:
        console.clear()
        console.rule(program4.title)
        console.print(Padding(panel_description, pad=(1, 0, 0, 0)))

        input_string = Prompt.ask("[bold]\nHai👋! Masukkan string yang ingin di dibalik, lalu klik 'enter'\n")

        count = 0
        while True:
            console.clear()
            console.rule(program4.title)

            if count == 0:
                console.print(Padding(panel_option, pad=(1, 0, 0, 0)))
                opt = IntPrompt.ask("\n[bold]Pilih Opsi", choices=["1", "2"])
                
                import getpass
                match opt:
                    case 1:
                        console.clear()
                        console.rule(program4.title)

                        original_string = Panel(f"\n[bold]{input_string}\n", title="[bold #9ee5ff]Original String")
                        reversed_string = Panel(f"\n[bold]{reverse_string(input_string)}\n", title="[bold #9ee5ff]Reversed String")

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

                        original_string = Panel(f"\n[bold]{input_string}\n", title="[bold #9ee5ff]Original String")
                        reversed_string = Panel(f"\n[bold]{result}\n", title="[bold #9ee5ff]Reversed String")

                        console.print(Padding(original_string, pad=(1, 0, 0, 0)))
                        console.print(Padding(reversed_string, pad=(1, 0, 0, 0)))

                        getpass.getpass("\nKlik 'enter' untuk melanjutkan")
                        count += 1
                        continue

            console.print(Padding(panel_menu, pad=(1, 0, 0, 0)))
            opt = IntPrompt.ask("\n[bold]Pilih Menu", choices=["1", "2", "3"])

            match opt:
                case 1:
                    count += 1
                    break
                case 2:
                    count = 0
                    continue
                case 3:
                    return program4.stop()

title = "[bold #9ee5ff]Program 4: Reverse String" # untuk di tampilkan sebagai judul
name = "Reverse String" # untuk di tampilkan di list menu
description = """[bold]
🔷 Ini merupakan program untuk membalikkan string.
🔷 Program ini mengimplementasikan struktur data tumpukan (stack) untuk membalikkan string.
🔷 Pada program ini terdapat fitur untuk membalikkan string keseluruhan dan membalikkan string perkata.\n""" # deskripsi program
program4 = App(name=name, title=title, description=description, program=main)

if __name__ == "__main__":
    program4.start()
