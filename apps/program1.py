from utils.app import App
from collections import deque

def decimal_conversion(dec: int, toBase: int):
    if toBase == 10 or dec == 0 or dec == 1:
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
    negative = False
    if bin[0] == "-":
        bin = bin[1:].lstrip('0')
        negative = True

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
    negative = False
    if oct[0] == "-":
        oct = oct[1:].lstrip('0')
        negative = True

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
    negative = False
    if hex[0] == "-":
        hex = hex[1:].lstrip('0')
        negative = True

    if toBase == 16 or hex == "0" or hex == "1":
        return "-" + hex if negative else hex

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

def main():
    # Menu sistem bilangan
    number_system = {
        1: ("Biner", 2),
        2: ("Oktal", 8),
        3: ("Desimal", 10),
        4: ("Heksadesimal", 16)
    }

    count = 0
    while True:
        if count > 0:
            program1.clear()
            print(program1.title)
        print("Sistem Bilangan:")
        for k, v in number_system.items():
            print(f"{k}. {v[0]}")

        # pilih sistem bilangan yang ingin di konversi
        base = int(program1.prompt_options(word="\nPilih sistem bilangan yang ingin dikonversi", opts=[1,2,3,4]))

        # pilih tujuan konversi
        to_base = int(program1.prompt_options(word="Pilih tujuan konversi", opts=[1,2,3,4]))

        # konfirmasi
        print("\nBerikut adalah konversi yang ingin dilakukan: ")
        print(f"{number_system[base][0]} -----> {number_system[to_base][0]}\n")

        count += 1
        confirm = program1.prompt_options(word="Apakah anda yakin ingin melakukan konversi tersebut?", opts=["y","n"])
        if confirm == "y":
            break

    while True:
        input_value = input(f"\nMasukkan angka dalam Sistem Bilangan {number_system[base][0]}: ") 

        negative_value = False
        if input_value[0] == "-":
            input_value = input_value[1:]
            negative_value = True

        if number_system[base][0] == "Heksadesimal" and not (all([ord(i.upper()) >= 65 and ord(i.upper()) <= 70 for i in input_value if i.isalpha()]) and input_value.isalnum()):
            print(f"Sistem Bilangan {number_system[base][0]} yang dimasukkan tidak valid!")
        elif number_system[base][0] == "Desimal" and not input_value.isdecimal():
            print(f"Sistem Bilangan {number_system[base][0]} yang dimasukkan tidak valid!")
        elif number_system[base][0] == "Oktal" and (not input_value.isdecimal() or not all([int(i) < 8 for i in input_value])):
            print(f"Sistem Bilangan {number_system[base][0]} yang dimasukkan tidak valid!")
        elif number_system[base][0] == "Biner" and (not input_value.isdecimal() or not all([int(i) < 2 for i in input_value])):
            print(f"Sistem Bilangan {number_system[base][0]} yang dimasukkan tidak valid!")
        else:
            input_value = "-" + input_value if negative_value else input_value
            break

    output_value = None

    match number_system[base][0]:
        case "Biner":
            output_value = biner_conversion(input_value, number_system[to_base][1])
        case "Oktal":
            output_value = octal_conversion(input_value, number_system[to_base][1])
        case "Desimal":
            output_value = decimal_conversion(int(input_value), number_system[to_base][1])
        case "Heksadesimal":
            output_value = hexadecimal_conversion(input_value, number_system[to_base][1])

    print(f"Berikut adalah hasil konversinya: {output_value}")

    confirm = program1.prompt_options(word="\nQuit Program?", opts=["y","n"])
    if confirm == "y":
        return program1.stop()

title = "========== Program 1: Konversi Sistem Bilangan ==========\n" # untuk di tampilkan sebagai judul
name = "Konversi Sistem Bilangan" # untuk di tampilkan di list menu
description = ("""Deskripsi Program:
Ini merupakan program untuk mengonversi bilangan dari satu sistem bilangan ke sistem bilangan lain. 
Program ini menggunakan implementasi struktur data tumpukan (stack) dalam melakuan konversi sistem bilangan. 
Program ini hanya menangani bilangan bulat saja (positif dan negatif), dimana pada bilangan negatif diawali dengan tanda '-'.\n""", False) # deskripsi program

program1 = App(name=name, title=title, description=description, program=main)

if __name__ == "__main__":
    program1.start()
