from typing import Callable, Tuple

class App():
    def __init__(self, name: str="My Program", title: str="========== My Program ==========\n", description: Tuple[str, bool]=("", True), program: Callable=lambda: None):
        self.name = name
        self.title = title
        self.description = description
        self.program = program

    def prompt(self, word="\nQuit Program?(y/n): ", options=("y", "n")):
        ans = input(word)
        return True if ans == options[0] else False
        
    def clear(self):
        import os
        operating_system = os.name
        match operating_system:
            case "posix": os.system("clear")
            case "nt": os.system("cls") 

    def start(self):
        run = True
        count = 0
        while run:
            self.clear()
            print(self.title)
            if not self.description[1]:
                if count == 0:
                    print(self.description[0])
                    count += 1
                    
            self.program()
            run = not self.prompt()




