from Print import Print
from Fasada import Fasada
from Debug import Debug
from File_ha import File_ha

class Controler(Fasada):
    """
    Class to handle user request and extends class Fasada
    Class is set to user = 1 (No authentication)
    """
    id_user = 1

    def Nakup(self,bota):
        """
        Function to buy product
        :param bota: str (name of bota)
        :return:
        """
        pp = Print("Vybrali jste si botu {}".format(bota))
        pp.deli()
        data = self._bota_from_name(bota)

        velikosti = []

        for x in data:
            velikosti.append(x[3])
            cena = x[5]

        pp.print("Cena /ks je {}".format(cena))
        pp.print("Velikosti máme: {}".format(pp.array_to_str(velikosti)))
        kontrola1 = True
        while(1):
            try:

                pp.print("Jakou velikost chcete nakoupit?")
                velikost = int(input())
                if not str(velikost) in velikosti:
                    raise Exception("Musíte zadat validní, které máme na skladě velikosti {}".format(pp.array_to_str(velikosti)))

                pp.print("Zadejte počet kusů")
                pocet_kusu = int(input())

                if pocet_kusu <= 0:
                    raise Exception("Zadali jste více kusů, než je momentálně na skladě.. (max {})".format(x[4]))

                for x in data:
                    if x[2] == bota and x[2] == velikost:
                        if x[4] < pocet_kusu:
                            raise Exception("Zadali jste více kusů, než je momentálně na skladě.. (max {})".format(x[4]))

                break;

            except ValueError:
                pp.print("Zadejte číslo...")
            except Exception as e:
                pp.print(e)

        ids = self.vyber_platby()

        pp.deli()
        pp.print("Provádím objednávku...")
        pp.deli()

        try:
            self._kupovat_botu(bota, pocet_kusu, self.id_user, ids,velikost)
            return True
        except Exception as e:
            pp.print("Něco se pokazilo...")
            Debug(e)
            return False


    def objednavka(self,metoda_platebni, pocet_kusu,nazev_boty):

        if(self._kupovat_botu(nazev_boty,pocet_kusu,self.id_user,metoda_platebni)):
            return True
        return False


    def vyber_platby(self):
        pp = Print("Vyberte si platební metodu")

        while(1):
            try:
                platby = self._get_Platby()

                list_id = []
                string = ""
                for x in platby:
                    list_id.append(x[0])
                    string = string + str(x[0])+". "+str(x[1])+ " cena +"+str(x[2])+ "\n"

                string[:-1]
                pp.print(string)

                vyber = int(input())

                nasel = False

                for x in platby:
                    if x[0] == vyber:
                        nasel = True
                        break

                if not nasel:
                    raise Exception("Zadejte validní číslo")

                return platby[vyber -1][0]

            except ValueError:
                pp.print("Zadejte číslo")
            except Exception as e:
                pp.print(e)

    def is_bota_on_stack(self,where):
        """
        :param where: str (name of bota)
        :return: bool
        """

        data = self._bota_from_name(where)

        if len(data) > 0:
            return True
        return False

    def get_nabidka(self):
        data_from_DB = self._get_nabidka_DB()
        count = 1;
        if len(data_from_DB) == 0:
            Print("Bohužel nabídka je zatím prázdná...")
        for x in data_from_DB:
            Print("{}. Značka: {} Název: \"{}\" Velikost: {} {}Kusů na skladě, Cena: {}Kč".format(count,x[1],x[2],x[3],x[4],x[5]))
            count = count + 1;

    def get_user_obj(self):
        """
        Get user orders and print them in readable form
        :return:
        """
        data = self._get_user_data(self.id_user)
        Debug(data)
        if len(data) == 0:
            return "Nemáte ještě žádné objednávky..."

        string = ""

        for x in data:
            string = string + "Název boty: " + str(x[0])
            string = string + " - Velikost: " + str(x[1])
            string = string + " - Datum nákupu: " + str(x[2])
            if x[3]:
                zaplaceno = "Zaplaceno"
            else:
                zaplaceno = "Nezaplaceno"
            string = string + " - Datum nákupu: " + zaplaceno
            if x[4] == None or x[4] == "":
                dodano = "Zatím ne"
            else:
                dodano = "Dodáno {}".format(x[4])
            string = string + " - Značka: " + x[5]+ "\n\r"

        return  string;

    def delete_history(self):
        """
        Function to delete history
        """
        pp = Print()
        try:
            self._delete_history_from_user(self.id_user)
            pp.print("Historie objednávek se smazala.")
        except:
            pp.print("Něco se nepovedlo při mazání vaší historie")

    def update(self):
        """
        Function to handle update DB
        """
        pp = Print("Zadejte absolutní cestu k souboru")
        user_path = input()
        file_ha = File_ha(user_path)
        data = file_ha.load_file()
        try:
            self._insert_znacky(data[0])
            pp.deli()
            pp.print("Povedlo se přidat značky ... {}".format(pp.array_to_str(data[0])))
        except:
            pp.print("Nepovedlo se akualizovat značky... {}".format(pp.array_to_str(data[0])))
        pp.deli()
        try:
            self._insert_bota(data[1])
            pp.print("Povedlo se nahrát nové zboží")
        except Exception as e:
            pp.print("Nepovedlo se aktualizovat značky ... {} e: {}".format(pp.array_to_str(data[1]),e))

