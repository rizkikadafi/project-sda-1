from typing import Callable, Tuple, List

class App():
    def __init__(self, name: str="My Program", title: str="========== My Program ==========\n", description: Tuple[str, bool]=("", True), program: Callable=lambda: None):
        self.name = name
        self.title = title
        self.description = description
        self.program = program
        self.running = True

    def prompt_options(self, word: str, opts: List, invalid_massage: str= "Input yang anda masukkan tidak valid!"):
        while True:
            list_opts = [i for i in opts]
            str_opts = ""
            for opt in list_opts:
                if list_opts.index(opt) != len(list_opts) - 1:
                    str_opts += f"{str(opt)}/"
                else:
                    str_opts += f"{str(opt)}"

            ans = input(word + f" [{str_opts}] ({list_opts[0]}): ")

            if ans.isdecimal():
                ans = int(ans)

            if ans in opts:
                break

            print(invalid_massage)

        return ans       
        
    def clear(self):
        import os
        operating_system = os.name
        match operating_system:
            case "posix": os.system("clear")
            case "nt": os.system("cls") 

    def stop(self):
        self.running = False

    def start(self):
        self.running = True
        count = 0
        while self.running:
            self.clear()
            print(self.title)
            if not self.description[1]:
                if count == 0:
                    print(self.description[0])
                    count += 1
                    
            self.program()
