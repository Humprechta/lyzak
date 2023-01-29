from Print import Print
class Menu():
    """
    Class for menu handling
    """

    pp = Print()
    def __init__(self):
        self.pp.print("Vyberte si z menu 1 - {}".format(len(self.get_commands())))

    def get_commands(self):
        return [
        ("Vypsat svoje objednávky", 1),
        ("Katalog", 2),
        ("Pomoc", 3),
        ("Smazat historii objednávek", 4),
        ("Aktualizovat nabídku", 5),
            ("Ukončit program", 6)
    ]

    def menu(self):
        self.pp.deli()
        for label, command_num in self.get_commands():
            self.pp.print("\t" + str(command_num) + ". " + label)
        command_num = None
        while (command_num == None):
            command_num = input("Zadejte číslo z menu (1-" + str(len(self.get_commands())) + "): ").strip()
            try:
                command_num = int(command_num)
                if (not 0 < command_num <= len(self.get_commands())):
                    raise Exception("Neplatné číslo")
            except:
                print("Neplatné zadání musíte zadat číslo mezi 1 až " + str(len(self.get_commands())))
                command_num = None

        self.pp.deli()
        return command_num