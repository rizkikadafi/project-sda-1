from utils.app import *

from data_structure.stack import Stack

def full_data_panel(value) -> Panel:
    """Panel untuk menampilkan info ketika data penuh."""

    panel = Panel(Text(f"\nTumpukan telah penuh! [{value}] tidak dimasukkan!\n", justify="center", style="text_warning"), title="[title_warning]INFO", style="warning")
    return panel

def success_panel(value, operation: str) -> Panel:
    """Panel untuk menampilkan info ketika operasi tertentu berhasil dilakukan."""

    panel = Panel("None")
    match operation:
        case "addition":
            panel = Panel(Text(f"\n[{value}] berhasil dimasukkan.\n", justify="center", style="text_success"), title="[title_success]INFO", style="success")
        case "deletion":
            panel = Panel(Text(f"\n[{value}] berhasil dihapus!\n", justify="center", style="text_success"), title="[text_success]INFO", style="success")
        case "emptying":
            panel = Panel(Text(f"\nTumpukan telah dikosongkan!\n", justify="center", style="text_success"), title="[text_success]INFO", style="success")

    return panel

def empty_data_panel(operation: str) -> Panel:
    """Panel untuk menampilkan info ketika data kosong."""

    panel = Panel("None")
    match operation:
        case "deletion":
            panel = Panel(Text("\nTumpukan Kosong! Tidak ada data yang bisa dihapus!\n", justify="center", style="text_warning"), title="[title_warning]INFO", style="warning")
        case "display_data":
            panel = Panel(Text("\nTumpukan Kosong! Tidak ada data yang bisa ditampilkan!\n", justify="center", style="text_warning"), title="[title_warning]INFO", style="warning")

    return panel

def table_data(data: Stack, opt: str) -> Table | Panel:
    """Tabel untuk menampilkan data."""

    list_data = [i for i in data._stack] 

    table = Table(style="default")
    table.add_column("[text_title]No.", style="text_default", justify="center")
    table.add_column("[text_title]Data", style="text_default", min_width=20)

    match opt:
        case "top_data":
            table.title = "[text_title]Data Teratas"

            table.add_row("1", data.peek())
        case "all_data":
            table.title = "[text_title]Data Pada Tumpukan"

            for i in range(len(list_data)):
                table.add_row(f"{i+1}", list_data.pop())
        case "all_data_deletion":
            table.title = "[text_title]Data Pada Tumpukan"

            for i in range(len(list_data)):
                table.add_row(f"{i+1}", data.pop())

    return table

def main():
    while True:
        MAX = IntPrompt.ask("\n" + r"[bold]Masukkan maksimum daya tampung data \[bilangan bulat (positif)]")
        if MAX > 0:
            break

        console.print("[prompt.invalid]Harap masukkan bilangan bulat positif (lebih besar dari 0)!")

    stack = Stack(MAX)

    console.clear()
    console.rule(program2.title)

    menu = {
        1: "Tambahkan data",
        2: "Tampilkan data",
        3: "Hapus data teratas",
        4: "Keluar program"
    }

    menu_str = "\n[text_default]"
    for i, k in menu.items():
        menu_str += f"{i}. {k}\n"

    display_data_opt = {
        1: "Tampilkan data teratas",
        2: "Tampilkan seluruh data (Tanpa penghapusan)",
        3: "Tampilkan seluruh data (Dengan penghapusan!)",
    }

    display_data_opt_str = "\n[text_default]"
    for k, v in display_data_opt.items():
        display_data_opt_str += f"{k}. {v}\n"

    panel_menu = Panel(menu_str, title="[text_title]Menu Program", title_align="left", style="default")
    panel_display_data_opt = Panel(display_data_opt_str, title="[text_title]Opsi Tampilan Data", title_align="left", style="default")

    while True:
        console.clear()
        console.rule(program2.title, style="default")

        console.print(Padding(panel_menu, pad=(1, 0, 0, 0)))

        opt = IntPrompt.ask("[bold]\nPilih menu", choices=[str(i) for i in menu.keys()])

        import getpass
        match opt:
            case 1:
                while True:
                    data = Prompt.ask("[bold]\nMasukkan data")
                    if data == "":
                        console.print("[prompt.invalid]Data tidak boleh kosong!")
                    else:
                        break
                if stack.full():
                    console.print(full_data_panel(data))
                else:
                    stack.push(data)
                    console.print(success_panel(data, operation="addition"))

                getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 2:
                if stack.empty():
                    console.print(empty_data_panel(operation="display_data"))
                    getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
                    continue

                console.clear()
                console.rule(program2.title, style="default")

                console.print(Padding(panel_display_data_opt, pad=(1, 0, 0, 0)))
                opt = IntPrompt.ask("\n[bold]Pilih Opsi Tampilan Data", choices=[str(i) for i in display_data_opt.keys()])

                match opt:
                    case 1:
                        console.print(table_data(stack, opt="top_data"), justify="center")
                    case 2:
                        console.print(table_data(stack, opt="all_data"), justify="center")
                    case 3:
                        console.print(table_data(stack, opt="all_data_deletion"), justify="center")
                        console.print(Padding(success_panel(None, operation="emptying"), pad=(1, 0, 0, 0)))

                getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 3:
                if stack.empty():
                    console.print(empty_data_panel(operation="deletion"))
                else:
                    console.print(table_data(stack, opt="top_data"), justify="center")
                    if Confirm.ask("\n[bold]Apakah anda yakin ingin menghapus data tersebut!"):
                        data = stack.pop()
                        console.print(success_panel(data, operation="deletion"))

                getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 4:
                return program2.stop()

title = "[text_title]Program 2: Implementasi Tumpukan dengan Array" # untuk di tampilkan sebagai judul
name = "Tumpukan dengan Array" # untuk di tampilkan di list menu
description = """[text_default]
🔷 Program 2 merupakan program implementasi struktur data tumpukan (stack) dengan menggunakan array. 
🔷 Program ini memiliki fitur untuk menambahkan, menampilkan dan menghapus data.
🔷 Pada program ini, maksimal data yang dapat dimasukkan dibatasi dan dapat ditentukan oleh user.\n""" # deskripsi program
program2 = App(name=name, title=title, description=description, program=main)

if __name__ == "__main__":
    program2.start()
