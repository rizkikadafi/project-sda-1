import sys
sys.path.append("apps")

from apps.utils.load import Load
from apps import program1, program2, program3, program4

title = "========== Project 1 SDA ==========\n"
programs = Load(title=title)
programs.add([program1, program2, program3, program4])

if __name__ == "__main__":
    programs.run()
