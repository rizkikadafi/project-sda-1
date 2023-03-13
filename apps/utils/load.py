from .app import App

class Load(App):
    def add(self, programs):
        self.programs = programs

    def run(self):
        count = 0
        while True:
            self.clear()
            print(self.title)
            for i in range(len(self.programs)):
                print(f"{i+1}. {self.programs[i].name}")
            if count == 0:
                opt = int(input("\nPilih Program: "))
                self.programs[opt-1].start()
                count += 1
            elif count > 0:
                confirm = self.prompt_options(word="\nQuit Program?", opts=["y", "n"])
                if confirm == "y":
                    break
                else:
                    count = 0

