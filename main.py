import sys
sys.path.append("apps")

from apps.utils.load import Load
from apps import program1, program2, program3, program4

title = "[text_title]Project SDA 1[/]"
description = """[text_default]
[italic]Project SDA 1[/], merupakan project mata kuliah [italic]Struktur Data dan Algoritma[/] yang berisi program-program implementasi struktur data [italic]Tumpukan (Stack)[/].
"""

programs = Load(title=title, description=description)
programs.add([program1, program2, program3, program4])

if __name__ == "__main__":
    programs.run()
