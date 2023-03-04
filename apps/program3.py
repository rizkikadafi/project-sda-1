from utils.app import App

def main():
    print("doing some task")

title = "========== Program 3: Title Program 3 ==========\n" # untuk di tampilkan sebagai judul
name = "Nama program 3" # untuk di tampilkan di list menu
description = ("Deskripsi untuk aplikasi\n", False) # deskripsi program
program3 = App(name=name, title=title, description=description, program=main)

if __name__ == "__main__":
    program3.start()
