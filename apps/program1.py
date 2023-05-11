from utils.app import *

from collections import deque

def decimal_conversion(dec: int, toBase: int):
    """Fungsi untuk konversi dari sistem bilangan desimal ke sistem bilangan lain."""
    if toBase == 10:
        return str(dec)

    current_dec = abs(dec)
    conversion_stack = deque()

    result = "-" if dec < 0 else ""

    while current_dec > 0:
        if toBase == 16:
            conversion_stack.append(chr((current_dec % toBase) + 55) if current_dec % toBase >= 10 else current_dec % toBase)
            current_dec //= toBase
        else:
            conversion_stack.append(current_dec % toBase)
            current_dec //= toBase

    while len(conversion_stack) > 0:
        result += str(conversion_stack.pop())

    return result

def biner_conversion(bin: str, toBase: int):
    """Fungsi untuk konversi dari sistem bilangan biner ke sistem bilangan lain."""
    negative = False
    if bin[0] == "-":
        bin = bin[1:].lstrip('0')
        negative = True
    else:
        bin = bin.lstrip('0')

    if toBase == 2:
        return "-" + bin if negative else bin

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

    return result

def octal_conversion(oct: str, toBase: int):
    """Fungsi untuk konversi dari sistem bilangan oktal ke sistem bilangan lain."""
    negative = False
    if oct[0] == "-":
        oct = oct[1:].lstrip('0')
        negative = True
    else:
        oct = oct.lstrip('0')

    if toBase == 8:
        return "-" + oct if negative else oct

    conversion_stack = deque()
    octal = deque([int(i) for i in oct])
    dec = 0
    biner = ""

    result = "-" if negative else ""

    for i in range(len(octal)):
        if toBase == 10:
            dec += octal.pop() * 8**i
        else:
            bin = decimal_conversion(octal.pop(), 2)
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
            result += biner_conversion(biner, 16)

    return result

def hexadecimal_conversion(hex: str, toBase: int):
    """Fungis untuk konversi dari sistem bilangan hexadesimal ke sistem bilangan lain."""
    negative = False
    if hex[0] == "-":
        hex = hex[1:].lstrip('0')
        negative = True
    else:
        hex = hex.lstrip('0')

    if toBase == 16:
        return "-" + hex.upper() if negative else hex.upper()

    result = "-" if negative else ""

    conversion_stack = deque()
    hexa = deque(hex.upper())
    dec = 0
    biner = ""

    for i in range(len(hexa)):
        hex_digit = hexa.pop()
        if toBase == 10:
            dec += int(ord(hex_digit) - 55 if hex_digit.isalpha() else hex_digit) * 16**i
        else:
            bin = decimal_conversion(int(ord(hex_digit) - 55 if hex_digit.isalpha() else hex_digit), 2)
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
            result += biner_conversion(biner, 8)
        case 10:
            result += str(dec)

    return result

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

    mode_opt = {
        1: "one-to-one conversion",
        2: "one-to-all conversion"
    }

    mode_opt_str = "\n[text_default]"
    for k, v in mode_opt.items():
        mode_opt_str += f"{k}. {v}\n"

    panel_menu = Panel(menu, title="[text_title]Sistem Bilangan", title_align="left", style="default")
    panel_mode_opt = Panel(mode_opt_str, title="[text_title]Mode Konversi", title_align="left", style="default")
    panel_description = Panel(program1.description, title="[text_title]Deskripsi Program", title_align="left", style="default")

    while True:
        console.clear()
        console.rule(program1.title, style="default")
        console.print(Padding(panel_description, pad=(1, 0, 0, 0)), style="default")

        console.print(Padding(panel_mode_opt, pad=(1, 0, 0, 0)), style="default")

        mode = IntPrompt.ask("\n[bold]Pilih mode konversi", choices=[str(i) for i in mode_opt.keys()])
        match mode:
            case 1:
                while True:
                    console.clear()
                    console.rule(program1.title, style="default")

                    console.print(Padding(panel_menu, pad=(1, 0, 0, 0)), style="default")

                    base = IntPrompt.ask("\n[bold]Pilih sistem bilangan yang ingin dikonversi", choices=[str(i) for i in number_system.keys()])
                    to_base = IntPrompt.ask("\n[bold]Pilih tujuan konversi", choices=[str(i) for i in number_system.keys()])

                    console.print(Panel(f"\n[text_default]{number_system[base][0]}[/] ➔ [text_default]{number_system[to_base][0]}\n[/]", style="default", title="[text_title]Koversi Sistem Bilangan"), justify="center")

                    if Confirm.ask("\n[bold]Apakah anda yakin ingin melakukan konversi tersebut?"):
                        break

                input_value = None
                output_value = None

                match number_system[base][0]:
                    case "Biner":
                        input_value = BinPrompt.ask("[bold]Masukkan angka dalam Sistem Bilangan Biner")
                        output_value = biner_conversion(input_value, number_system[to_base][1])
                    case "Oktal":
                        input_value = OctPrompt.ask("[bold]Masukkan angka dalam Sistem Bilangan Oktal")
                        output_value = octal_conversion(input_value, number_system[to_base][1])
                    case "Desimal":
                        input_value = DecPrompt.ask("[bold]Masukkan angka dalam Sistem Bilangan Desimal")
                        output_value = decimal_conversion(int(input_value), number_system[to_base][1])
                    case "Heksadesimal":
                        input_value = HexPrompt.ask("[bold]Masukkan angka dalam Sistem Bilangan Heksadesimal")
                        output_value = hexadecimal_conversion(input_value, number_system[to_base][1])
                console.print(result_conversion_layout((number_system[base][0], input_value), (number_system[to_base][0], output_value)), height=5)
            case 2:
                pass

    #     console.print(Padding(panel_menu, pad=(1, 0, 0, 0)), style="default")

    #     # pilih sistem bilangan yang ingin di konversi
    #     base = IntPrompt.ask("\n[bold]Pilih sistem bilangan yang ingin dikonversi", choices=[str(i) for i in number_system.keys()])

    #     # pilih tujuan konversi
    #     to_base = IntPrompt.ask("\n[bold]Pilih tujuan konversi", choices=[str(i) for i in number_system.keys()])

    #     # konfirmasi
    #     console.print(Text("\nBerikut adalah konversi yang ingin dilakukan", style="underline bold"), justify="center")
    #     console.print(f"[text_default]{number_system[base][0]}[/] ➔ [text_default]{number_system[to_base][0]}\n[/]", justify="center")

    #     if Confirm.ask("[bold]Apakah anda yakin ingin melakukan konversi tersebut?"):
    #         break

    # input_value = None
    # output_value = None

    # match number_system[base][0]:
    #     case "Biner":
    #         input_value = BinPrompt.ask("[bold]Masukkan angka dalam Sistem Bilangan Biner")
    #         output_value = biner_conversion(input_value, number_system[to_base][1])
    #     case "Oktal":
    #         input_value = OctPrompt.ask("[bold]Masukkan angka dalam Sistem Bilangan Oktal")
    #         output_value = octal_conversion(input_value, number_system[to_base][1])
    #     case "Desimal":
    #         input_value = DecPrompt.ask("[bold]Masukkan angka dalam Sistem Bilangan Desimal")
    #         output_value = decimal_conversion(int(input_value), number_system[to_base][1])
    #     case "Heksadesimal":
    #         input_value = HexPrompt.ask("[bold]Masukkan angka dalam Sistem Bilangan Heksadesimal")
    #         output_value = hexadecimal_conversion(input_value, number_system[to_base][1])

    # layout_conversion = Layout(name="conversion", size=3)
    # layout_conversion.split_column(
    #     Layout(name="conversion_child", size=5, ratio=1, minimum_size=3),
    # )

    # layout_conversion["conversion_child"].split_row(
    #         Layout(name="base", ratio=3),
    #         Align.center(Text("➔", justify="center"), vertical="middle"),
    #         Layout(name="to_base", ratio=3)
    # )

    # layout_conversion["base"].update(Panel(Text(f"\n{input_value}\n", justify="center", style="text_default"), title=f"[text_title]{number_system[base][0]}", style="default"))
    # layout_conversion["to_base"].update(Panel(Text(f"\n{output_value}\n", justify="center", style="text_default"), title=f"[text_title]{number_system[to_base][0]}", style="default"))

    # console.print(layout_conversion, height=5)

        if Confirm.ask("[bold]Keluar Program?"):
            return program1.stop()

title = "[text_title]Program 1: Konversi Sistem Bilangan\n" # untuk di tampilkan sebagai judul
name = "Konversi Sistem Bilangan" # untuk di tampilkan di list menu
description = """[text_default]
🔷 Program 1 merupakan program untuk mengonversi bilangan dari satu sistem bilangan ke sistem bilangan lain. 
🔷 Program ini menggunakan implementasi struktur data tumpukan (stack) dalam melakukan konversi sistem bilangan. 
🔷 Program ini hanya menangani bilangan bulat saja (positif dan negatif), dimana pada bilangan negatif diawali dengan tanda '-'.\n""" # deskripsi program

program1 = App(name=name, title=title, description=description, program=main)

if __name__ == "__main__":
    program1.start()
