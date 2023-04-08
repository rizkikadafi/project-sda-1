from .app import App, Panel, Padding, IntPrompt, Confirm, Text, console

class Load(App):
    def add(self, programs):
        self.programs = programs

    def run(self):
        menus = "\n[text_default]"
        for i in range(len(self.programs)):
            menus += f"{i+1}. {self.programs[i].name}\n"

        panel_menu = Panel(menus, title="[text_title]Menu Program", title_align="left")
        panel_description = Panel(self.description, title="[text_title]Deskripsi", title_align="left")
        panel_closing = Panel(Text("\n🙏Terima kasih telah menggunakan aplikasi ini🙏\n", justify="center", style="text_default"), title="[text_title]Program Selesai", style="default")

        count = 0
        while True:
            console.clear()
            console.rule(self.title, style="default")
            console.print(Padding(panel_description, pad=(1, 0, 0, 0)), style="default")
            console.print(Padding(panel_menu, pad=(1, 0, 0, 0)), style="default")

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
