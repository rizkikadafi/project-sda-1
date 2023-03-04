from utils.app import App

def main():
    print("doing some task")

title = "========== Program 2: Title Program 2 ==========\n" # untuk di tampilkan sebagai judul
name = "Nama program 2" # untuk di tampilkan di list menu
description = ("Deskripsi untuk aplikasi\n", False) # deskripsi program
program2 = App(name=name, title=title, description=description, program=main)

if __name__ == "__main__":
    program2.start()
