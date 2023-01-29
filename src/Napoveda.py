class Napoveda:

    def get_deli(self):
        return "\n\r##############\n\r"

    def get_napoveda(self):
        string = self.get_deli()+\
                 "Vítejte v nápovědě" \
                  +self.get_deli()+\
                 "1. Program se ovládá pomocí klávesnice\n" \
                 "2. Před 1. spuštěním se ujistěte že pužíváte MySQL v 10.4.22 +, Python 3.9 + a máte nainstalovaný MySQL driver pro python\n" \
                 "3. Do databáze (nejléme MySQL WORKBENCH) založte databázi 'python_projects' a naimportujte sql/sql.sql soubor\n" \
                 "4. Nastavte uživatelská práva a vyplňte je do config/config.csv\n  -->  1. řádek PORT, 2. řádek host, 3. řádek přihlašovací jméno, 4. řádek heslo, 5. jméno databáze" \
                 +self.get_deli()+\
                 "Při importování ze souboru (v menu možnost 5) se musí zadat celá adresa k souboru (absolutní a program musí mít k ní přistup) Př: C:/Users/vasek\PycharmProjects/db_driver/alfa3/testovaci_data/UPDATE.csv" \
                 +self.get_deli()+\
                 "Pokud by jste měli jakýkoliv dotaz, obraťe se na mě vasek.taitl@gmail.com" \
                 +self.get_deli()+\
                 "Program je volně k použití ZDARMA, je pod licencí Creative Commons - BY" \
                 + self.get_deli()
        return  string