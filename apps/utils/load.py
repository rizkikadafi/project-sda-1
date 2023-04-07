from .app import App, Panel, Padding, IntPrompt, Confirm, Text, console

class Load(App):
    def add(self, programs):
        self.programs = programs

    def run(self):
        menus = "\n[bold]"
        for i in range(len(self.programs)):
            menus += f"{i+1}. {self.programs[i].name}\n"

        panel_menu = Panel(menus, title="[bold #9ee5ff]Menu Program", title_align="left")
        panel_description = Panel(self.description, title="[bold #9ee5ff]Deskripsi", title_align="left")
        panel_closing = Panel(Text("\n🙏Terima kasih telah menggunakan aplikasi ini🙏\n", justify="center", style="bold white"), title="[bold #9ee5ff]Program Selesai", style="bold #9ee5ff")

        count = 0
        while True:
            console.clear()
            console.rule(self.title)
            console.print(Padding(panel_description, pad=(1, 0, 0, 0)))
            console.print(Padding(panel_menu, pad=(1, 0, 0, 0)))

            if count % 2 == 0:
                opt = IntPrompt.ask("[bold]\nPilih Program", choices=[str(i+1) for i in range(len(self.programs))])
                self.programs[opt-1].start()
                count += 1
            else:
                if Confirm.ask("[bold]\nKeluar Program?"):
                    console.clear()
                    console.print(panel_closing)
                    break
                else:
                    count += 1
