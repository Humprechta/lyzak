from Controler import Controler
from Print import Print
from Debug import Debug
from Napoveda import Napoveda
from Menu import Menu

if __name__ == "__main__":
    pp = Print("Dobrý den, vítejte v textovém obchodě s obuví")
    pp.deli()

    controler = Controler();
    menu = Menu()

    while(1):
        """
        Program loop
        """
        command_num = menu.menu()

        if command_num == 1:
            try:
                pp.print(controler.get_user_obj())
            except Exception as e:
                pp.print("CHYBA:\n\r{}".format(e))

        elif command_num == 2:

            pp.print(controler.get_nabidka())

            while(1):
                try:
                    """Nákup"""
                    pp.print("Chcete si něco z katalogu vybrat?\n\r1. Ano\n2. Ne")
                    inn = int(input())
                    if inn > 2 or inn < 1:
                        raise Exception("Zadejte číslo v rozmezí 1 - 2")
                    if inn == 2 or inn == 1:
                        break
                except ValueError:
                    pp.print("Zadejte číslo 1 - 2")
                except Exception as e:
                    pp.print(e)
            if inn == 1:
                pp.print("Zadejte název boty, která se vám líbí")
                try:
                    while(1):
                        bota = str(input())
                        if(controler.is_bota_on_stack(bota)):
                            if controler.Nakup(bota):
                                pp.print("Objednávka se úspěšně odeslala")
                                break;
                            else:
                                pp.print("Něco se npovedlo...")
                                break

                        else:
                            pp.print(
                                "Bota nebyla nalezena, pokud chcete opustit nákup napiště 'exit' a nebo tu zkuste znovu")
                        if bota == "exit":
                            break

                except ValueError:
                    print("Napiště název boty")
                except Exception as e :
                    Debug("Něco se nepovedlo: {}".format(e))

        elif command_num == 3:
            napoveda = Napoveda()
            pp.print(napoveda.get_napoveda())
        elif  command_num == 4:
            controler.delete_history()
        elif command_num == 5:
            controler.update()
        elif command_num == 6:
            pp.print("Program se ukončí...")
            pp.deli()
            exit(0)













