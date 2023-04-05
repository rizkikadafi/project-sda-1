import sys
sys.path.append("apps")

from apps.utils.load import Load
from apps import program1, program2, program3, program4

title = "[bold #9ee5ff]Project SDA 1[/]"
description = """[bold]
[italic]Project SDA 1[/], merupakan project mata kuliah [italic]Struktur Data dan Algoritma[/] yang berisi program-program implementasi struktur data [italic]Tumpukan (Stack)[/].
"""

programs = Load(title=title, description=description)
programs.add([program1, program2, program3, program4])

if __name__ == "__main__":
    programs.run()
