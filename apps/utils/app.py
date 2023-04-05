from typing import Callable, List
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.layout import Layout
from rich.text import Text
from rich.padding import Padding
from rich.prompt import Prompt, IntPrompt, Confirm, PromptBase, InvalidResponse
from rich.align import Align

console = Console()

IntPrompt.validate_error_message = "[prompt.invalid]Harap masukkan bilangan bulat yang valid!"
IntPrompt.illegal_choice_message = (
    "[prompt.invalid.choice]Harap masukkan pilihan dari salah satu opsi yang tersedia!"
)
Confirm.validate_error_message = "[prompt.invalid]Harap masukkan Y atau N"

class App():
    def __init__(self, name: str="My Program", title: str="[bold #9ee5ff]My Program\n", description: str="", program: Callable=lambda: None):
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
        panel_description = Panel(self.description, title="[bold #9ee5ff]Deskripsi Program", title_align="left")
        while self.running:
            console.clear()
            console.rule(self.title)
            print()

            console.print(panel_description)
                    
            self.program()
