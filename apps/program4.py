from utils.app import App

def main():
    print("doing some task")

title = "========== Program 4: Title Program 4 ==========\n" # untuk di tampilkan sebagai judul
name = "Nama program 4" # untuk di tampilkan di list menu
description = ("Deskripsi untuk aplikasi\n", False) # deskripsi program
program4 = App(name=name, title=title, description=description, program=main)

if __name__ == "__main__":
    program4.start()
