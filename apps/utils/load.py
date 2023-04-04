from .app import App, Panel, Padding, IntPrompt, Confirm, console

class Load(App):
    def add(self, programs):
        self.programs = programs

    def run(self):
        count = 0
        panel_description = Panel(self.description[0], title="[bold #9ee5ff]Deskripsi", title_align="left")

        while True:
            console.clear()
            console.rule(self.title)

            if (count == 0 and not self.description[1]) or self.description[1]:
                console.print(Padding(panel_description, pad=(1, 0, 0, 0)))

            menus = "[bold]"
            for i in range(len(self.programs)):
                menus += f"{i+1}. {self.programs[i].name}\n"
            console.print(Panel(menus, title="[bold #9ee5ff]Menu Program", title_align="left", padding=(1, 1, 0, 1)))

            if count % 2 == 0:
                opt = IntPrompt.ask("[bold]Pilih Program", choices=[str(i+1) for i in range(len(self.programs))])
                self.programs[opt-1].start()
                count += 1
            else:
                if Confirm.ask("[bold]Keluar Program?"):
                    break
                else:
                    count += 1
