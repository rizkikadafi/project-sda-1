from utils.app import App

def main():
    print("doing some task")

title = "========== Program 1: Title Program 1 ==========\n" # untuk di tampilkan sebagai judul
name = "Nama program 1" # untuk di tampilkan di list menu
description = ("Deskripsi untuk aplikasi\n", False) # deskripsi program
program1 = App(name=name, title=title, description=description, program=main)

if __name__ == "__main__":
    program1.start()
