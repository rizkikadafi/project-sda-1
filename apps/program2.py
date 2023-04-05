from utils.app import *

from data_structure.stack import Stack

def full_data_panel(value) -> Panel:
    """Panel untuk menampilkan info ketika data penuh."""

    panel = Panel(Text(f"\nTumpukan telah penuh! [{value}] tidak dimasukkan!\n", justify="center", style="bold"), title="[bold]INFO")
    return panel

def success_panel(value, operation: str) -> Panel:
    """Panel untuk menampilkan info ketika operasi tertentu berhasil dilakukan."""

    panel = Panel("None")
    match operation:
        case "addition":
            panel = Panel(Text(f"\n[{value}] berhasil dimasukkan.\n", justify="center", style="bold"), title="[bold]INFO")
        case "deletion":
            panel = Panel(Text(f"\n[{value}] berhasil dihapus!\n", justify="center", style="bold"), title="[bold]INFO")
        case "emptying":
            panel = Panel(Text(f"\nTumpukan telah dikosongkan!\n", justify="center", style="bold"), title="[bold]INFO")

    return panel

def empty_data_panel(operation: str) -> Panel:
    """Panel untuk menampilkan info ketika data kosong."""

    panel = Panel("None")
    match operation:
        case "deletion":
            panel = Panel(Text("\nTumpukan Kosong! Tidak ada data yang bisa dihapus!\n", justify="center", style="bold"), title="[bold]INFO")
        case "display_top_data":
            panel = Panel(Text("\nTumpukan Kosong! Tidak ada data teratas yang bisa ditampilkan!\n", justify="center", style="bold"), title="[bold]INFO")
        case "display_all_data":
            panel = Panel(Text("\nTumpukan Kosong! Tidak ada data yang bisa ditampilkan!\n", justify="center", style="bold"), title="[bold]INFO")

    return panel

def table_data(data: Stack, opt: str) -> Table | Panel:
    """Tabel untuk menampilkan data."""

    list_data = [i for i in data._stack] 

    table = Table()
    table.add_column("No.", style="bold", justify="center")
    table.add_column("Data", style="bold", min_width=20)

    match opt:
        case "top_data":
            table.title = "[bold]Data Teratas"

            table.add_row("1", data.peek())
        case "all_data":
            table.title = "[bold]Data Pada Tumpukan"

            for i in range(len(list_data)):
                table.add_row(f"{i+1}", list_data.pop())
        case "all_data_deletion":
            table.title = "[bold]Data Pada Tumpukan"

            for i in range(len(list_data)):
                table.add_row(f"{i+1}", data.pop())

    return table

def main():
    maks = IntPrompt.ask("\n" + r"[bold]Masukkan maksimal daya tampung data \[bilangan bulat]")

    stack = Stack(maks)

    console.clear()
    console.rule(program2.title)

    menu = {
        1: "Tambahkan data",
        2: "Hapus data teratas",
        3: "Tampilkan data teratas",
        4: "Tampilkan seluruh data (Tanpa penghapusan)",
        5: "Tampilkan seluruh data (Dengan penghapusan!)",
        6: "Keluar program"
    }

    menu_str = "\n[bold]"
    for i, k in menu.items():
        menu_str += f"{i}. {k}\n"

    panel_menu = Panel(menu_str, title="[bold #9ee5ff]Menu Program", title_align="left")

    while True:
        console.clear()
        console.rule(program2.title)

        console.print(Padding(panel_menu, pad=(1, 0, 0, 0)))

        opt = IntPrompt.ask("[bold]\nPilih menu", choices=["1", "2", "3", "4", "5", "6"])

        import getpass
        match opt:
            case 1:
                data = Prompt.ask("[bold]\nMasukkan data")
                if stack.full():
                    console.print(full_data_panel(data))
                else:
                    stack.push(data)
                    console.print(success_panel(data, operation="addition"))

                getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 2:
                if stack.empty():
                    console.print(empty_data_panel(operation="deletion"))
                else:
                    data = stack.pop()
                    console.print(success_panel(data, operation="deletion"))

                getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 3:
                if stack.empty():
                    console.print(empty_data_panel(operation="display_top_data"))
                else:
                    console.print(table_data(stack, opt="top_data"), justify="center")

                getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 4:
                if stack.empty():
                    console.print(empty_data_panel(operation="display_all_data"))
                else:
                    console.print(table_data(stack, opt="all_data"), justify="center")

                getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 5:
                if stack.empty():
                    console.print(empty_data_panel(operation="display_all_data"))
                else:
                    console.print(table_data(stack, opt="all_data_deletion"), justify="center")
                    console.print(Padding(success_panel(None, operation="emptying"), pad=(1, 0, 0, 0)))

                getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 6:
                return program2.stop()

title = "[bold #9ee5ff]Program 2: Implementasi Tumpukan dengan Array" # untuk di tampilkan sebagai judul
name = "Tumpukan dengan Array" # untuk di tampilkan di list menu
description = """[bold]
🔷 Program 2 merupakan program implementasi struktur data tumpukan (stack) dengan menggunakan array. 
🔷 Program ini memiliki fitur untuk menambahkan, menampilkan dan menghapus data.
🔷 Pada program ini, maksimal data yang dapat dimasukkan dibatasi dan dapat ditentukan oleh user.\n""" # deskripsi program
program2 = App(name=name, title=title, description=description, program=main)

if __name__ == "__main__":
    program2.start()
