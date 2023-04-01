import sys
sys.path.append("apps")

from apps.utils.load import Load
from apps import program1, program2, program3, program4

title = "========== Project 1 SDA ==========\n"
description = """Deskripsi Project:
Project SDA 1, merupakan project mata kuliah Struktur Data dan Algoritma yang berisi program-program implementasi struktur data 
Tumpukan (Stack).
"""

programs = Load(title=title, description=(description, False))
programs.add([program1, program2, program3, program4])

if __name__ == "__main__":
    programs.run()
