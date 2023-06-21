from utils.app import *

from collections import deque


def decimal_conversion(dec: int, toBase: int):
    """Fungsi untuk konversi dari sistem bilangan desimal ke sistem bilangan lain."""

    table_process = Table(title="Process Konversi", style="default")
    table_process.add_column(
        "[text_title]Desimal saat ini", style="text_default", justify="center")
    table_process.add_column("[text_title]Operasi",
                             style="text_default", justify="center")
    table_process.add_column("[text_title]Sisa bagi",
                             style="text_default", justify="center")

    if toBase == 10:
        table_process = None
        return (str(dec), table_process)

    current_dec = abs(dec)
    conversion_stack = deque()

    result = "-" if dec < 0 else ""

    while current_dec > 0:
        if toBase == 16:
            remainder = chr((current_dec % toBase) +
                            55) if current_dec % toBase >= 10 else current_dec % toBase
            conversion_stack.append(remainder)

            table_process.add_row(
                f"{-current_dec if dec < 0 else current_dec}", f"{-current_dec if dec < 0 else current_dec} / {toBase}", f"{remainder}")
            current_dec //= toBase
        else:
            remainder = current_dec % toBase
            conversion_stack.append(remainder)

            table_process.add_row(
                f"{-current_dec if dec < 0 else current_dec}", f"{-current_dec if dec < 0 else current_dec} / {toBase}", f"{remainder}")
            current_dec //= toBase

    while len(conversion_stack) > 0:
        result += str(conversion_stack.pop())

    return (result, table_process)


def biner_conversion(bin: str, toBase: int):
    """Fungsi untuk konversi dari sistem bilangan biner ke sistem bilangan lain."""
    negative = False
    if bin[0] == "-":
        bin = bin[1:].lstrip('0')
        negative = True
    else:
        bin = bin.lstrip('0')

    if toBase == 2:
        return ("-" + bin, None) if negative else (bin, None)

    biner = deque([int(i) for i in bin])
    dec = 0
    conversion_stack = deque()

    result = "-" if negative else ""

    index = 0
    while len(biner) > 0:
        dec += biner.pop() * 2**index
        if toBase == 8 and (index == 2 or len(biner) == 0):
            conversion_stack.append(dec)
            index = 0
            dec = 0
        elif toBase == 16 and (index == 3 or len(biner) == 0):
            conversion_stack.append(chr(dec + 55) if dec >= 10 else dec)
            index = 0
            dec = 0
        else:
            index += 1

    if toBase == 10:
        result += str(dec)
    else:
        while len(conversion_stack) > 0:
            result += str(conversion_stack.pop())

    return (result, None)


def octal_conversion(oct: str, toBase: int):
    """Fungsi untuk konversi dari sistem bilangan oktal ke sistem bilangan lain."""
    negative = False
    if oct[0] == "-":
        oct = oct[1:].lstrip('0')
        negative = True
    else:
        oct = oct.lstrip('0')

    if toBase == 8:
        return ("-" + oct, None) if negative else (oct, None)

    conversion_stack = deque()
    octal = deque([int(i) for i in oct])
    dec = 0
    biner = ""

    result = "-" if negative else ""

    for i in range(len(octal)):
        if toBase == 10:
            dec += octal.pop() * 8**i
        else:
            bin = decimal_conversion(octal.pop(), 2)[0]
            if len(octal) > 0:
                conversion_stack.append("0"*(3 - len(bin)) + bin)
            else:
                conversion_stack.append(bin)

    while len(conversion_stack) > 0:
        biner += conversion_stack.pop()

    match toBase:
        case 2:
            result += biner
        case 10:
            result += str(dec)
        case 16:
            result += biner_conversion(biner, 16)[0]

    return (result, None)


def hexadecimal_conversion(hex: str, toBase: int):
    """Fungis untuk konversi dari sistem bilangan hexadesimal ke sistem bilangan lain."""
    negative = False
    if hex[0] == "-":
        hex = hex[1:].lstrip('0')
        negative = True
    else:
        hex = hex.lstrip('0')

    if toBase == 16:
        return ("-" + hex.upper(), None) if negative else (hex.upper(), None)

    result = "-" if negative else ""

    conversion_stack = deque()
    hexa = deque(hex.upper())
    dec = 0
    biner = ""

    for i in range(len(hexa)):
        hex_digit = hexa.pop()
        if toBase == 10:
            dec += int(ord(hex_digit) - 55 if hex_digit.isalpha()
                       else hex_digit) * 16**i
        else:
            bin = decimal_conversion(
                int(ord(hex_digit) - 55 if hex_digit.isalpha() else hex_digit), 2)[0]
            if len(hexa) > 0:
                conversion_stack.append("0"*(4 - len(bin)) + bin)
            else:
                conversion_stack.append(bin)

    while len(conversion_stack) > 0:
        biner += conversion_stack.pop()

    match toBase:
        case 2:
            result += biner
        case 8:
            result += biner_conversion(biner, 8)[0]
        case 10:
            result += str(dec)

    return (result, None)


class BinPrompt(PromptBase):
    response_type = int
    validate_error_massage = "[prompt.invalid]Harap masukkan angka yang valid pada Sistem Bilangan Biner!"

    def process_response(self, value: str):
        value = value.strip()

        if not value:
            raise InvalidResponse(self.validate_error_massage)

        negative_value = False
        if value[0] == "-":
            value = value[1:]
            negative_value = True

        value = value.lstrip("0")

        if (not value.isdecimal() or not all([int(i) < 2 for i in value])):
            raise InvalidResponse(self.validate_error_massage)
        return "-" + value if negative_value else value


class OctPrompt(PromptBase):
    response_type = int
    validate_error_massage = "[prompt.invalid]Harap masukkan angka yang valid pada Sistem Bilangan Oktal!"

    def process_response(self, value: str):
        value = value.strip()

        if not value:
            raise InvalidResponse(self.validate_error_massage)

        negative_value = False
        if value[0] == "-":
            value = value[1:]
            negative_value = True

        value = value.lstrip("0")

        if (not value.isdecimal() or not all([int(i) < 8 for i in value])):
            raise InvalidResponse(self.validate_error_massage)
        return "-" + value if negative_value else value


class DecPrompt(PromptBase):
    response_type = int
    validate_error_massage = "[prompt.invalid]Harap masukkan angka yang valid pada Sistem Bilangan Desimal!"

    def process_response(self, value: str):
        value = value.strip()

        if not value:
            raise InvalidResponse(self.validate_error_massage)

        negative_value = False
        if value[0] == "-":
            value = value[1:]
            negative_value = True

        value = value.lstrip("0")

        if not value.isdecimal():
            raise InvalidResponse(self.validate_error_massage)
        return "-" + value if negative_value else value


class HexPrompt(PromptBase):
    response_type = int
    validate_error_massage = "[prompt.invalid]Harap masukkan angka yang valid pada Sistem Bilangan Heksadesimal!"

    def process_response(self, value: str):
        value = value.strip()

        if not value:
            raise InvalidResponse(self.validate_error_massage)

        negative_value = False
        if value[0] == "-":
            value = value[1:]
            negative_value = True

        value = value.lstrip("0").upper()

        if not (all([ord(i) >= 65 and ord(i) <= 70 for i in value if i.isalpha()]) and value.isalnum()):
            raise InvalidResponse(self.validate_error_massage)
        return "-" + value if negative_value else value

def result_conversion_layout(base: tuple, to_base: tuple):
    layout_conversion = Layout(name="conversion", size=3)
    layout_conversion.split_column(
        Layout(name="conversion_child", size=5, ratio=1, minimum_size=3),
    )

    layout_conversion["conversion_child"].split_row(
            Layout(name="base", ratio=3),
            Align.center(Text("➔", justify="center"), vertical="middle"),
            Layout(name="to_base", ratio=3)
    )

    layout_conversion["base"].update(Panel(Text(f"\n{base[1]}\n", justify="center", style="text_default"), title=f"[text_title]{base[0]}", style="default"))
    layout_conversion["to_base"].update(Panel(Text(f"\n{to_base[1]}\n", justify="center", style="text_default"), title=f"[text_title]{to_base[0]}", style="default"))

    return layout_conversion


def main():
    # Menu sistem bilangan
    number_system = {
        1: ("Biner", 2),
        2: ("Oktal", 8),
        3: ("Desimal", 10),
        4: ("Heksadesimal", 16)
    }

    menu = "\n[text_default]"
    for k, v in number_system.items():
        menu += f"{k}. {v[0]}\n"

    panel_menu = Panel(
        menu, title="[text_title]Sistem Bilangan", title_align="left", style="default")
    panel_description = Panel(
        program1.description, title="[text_title]Deskripsi Program", title_align="left", style="default")

    while True:
        console.clear()
        console.rule(program1.title, style="default")
        console.print(Padding(panel_description,
                      pad=(1, 0, 0, 0)), style="default")
        
        console.print(Padding(panel_menu, pad=(1, 0, 0, 0)))

        # pilih sistem bilangan yang ingin di konversi
        base = IntPrompt.ask("\n[bold]Pilih sistem bilangan yang ingin dikonversi", choices=[
                             str(i) for i in number_system.keys()])

        # pilih tujuan konversi
        to_base = IntPrompt.ask("\n[bold]Pilih tujuan konversi", choices=[
                                str(i) for i in number_system.keys()])

        # konfirmasi
        console.print(Text("\nBerikut adalah konversi yang ingin dilakukan",
                      style="underline bold"), justify="center")
        console.print(
            f"[text_default]{number_system[base][0]}[/] ➔ [text_default]{number_system[to_base][0]}\n[/]", justify="center")

        if Confirm.ask("\n[bold]Apakah anda yakin ingin melakukan konversi tersebut?"):
            break

        input_value = None
        output_value = None

    match number_system[base][0]:
        case "Biner":
            input_value = BinPrompt.ask(
                "[bold]Masukkan angka dalam Sistem Bilangan Biner")
            output_value = biner_conversion(
                input_value, number_system[to_base][1])
        case "Oktal":
            input_value = OctPrompt.ask(
                "[bold]Masukkan angka dalam Sistem Bilangan Oktal")
            output_value = octal_conversion(
                input_value, number_system[to_base][1])
        case "Desimal":
            input_value = DecPrompt.ask(
                "[bold]Masukkan angka dalam Sistem Bilangan Desimal")
            output_value = decimal_conversion(
                int(input_value), number_system[to_base][1])
        case "Heksadesimal":
            input_value = HexPrompt.ask(
                "[bold]Masukkan angka dalam Sistem Bilangan Heksadesimal")
            output_value = hexadecimal_conversion(
                input_value, number_system[to_base][1])

    # output layout
    if number_system[base][0] == "Desimal" and Confirm.ask("Apakah anda ingin menampilkan proses konversi?"):
        console.clear()
        console.rule(program1.title, style="default")
        console.print(result_conversion_layout(base=(number_system[base][0], input_value), to_base=(number_system[to_base][0], output_value[0])), height=5)
        console.print(output_value[1], justify="center")
    else:
        console.print(result_conversion_layout(base=(number_system[base][0], input_value), to_base=(number_system[to_base][0], output_value[0])), height=5)

    if Confirm.ask("[bold]Keluar Program?"):
        return program1.stop()


# untuk di tampilkan sebagai judul
title = "[text_title]Program 1: Konversi Sistem Bilangan\n"
name = "Konversi Sistem Bilangan"  # untuk di tampilkan di list menu
description = """[text_default]
🔷 Program 1 merupakan program untuk mengonversi bilangan dari satu sistem bilangan ke sistem bilangan lain. 
🔷 Program ini menggunakan implementasi struktur data tumpukan (stack) dalam melakukan konversi sistem bilangan. 
🔷 Program ini hanya menangani bilangan bulat saja (positif dan negatif), dimana pada bilangan negatif diawali dengan tanda '-'.\n"""  # deskripsi program

program1 = App(name=name, title=title, description=description, program=main)

if __name__ == "__main__":
    program1.start()
