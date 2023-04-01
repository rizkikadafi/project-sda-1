from .app import App

class Load(App):
    def add(self, programs):
        self.programs = programs

    def run(self):
        count = 0
        while True:
            self.clear()
            print(self.title)

            if count == 0 and not self.description[1]:
                print(self.description[0])
            else:
                print(self.description[0])

            print("Menu Program:")
            for i in range(len(self.programs)):
                print(f"{i+1}. {self.programs[i].name}")
            if count % 2 == 0:
                opt = int(self.prompt_options(word="\nPilih Program", opts=[1,2,3,4]))
                self.programs[opt-1].start()
                count += 1
            else:
                confirm = self.prompt_options(word="\nQuit Program?", opts=["y", "n"])
                if confirm == "y":
                    break
                else:
                    count += 1
