###############################
Vítáme vás v manuálu alfa3 1.0#
###############################

@Author: Václav Taitl C4b, jako školní projekt pro SPŠE Ječná (Praha 2, Ječná 30)
@Date: 2023-01-29

#########################################################################################################
Ke spuštění potřebujete operační systém win10+ čí unix s aplikací python (verze 3.9+) a MySQL v 10.4.22+#
#########################################################################################################

#######################################################################################################################################################
Před spuštěním nakonfigurujte soubor config.csv který je ve složce config a importujte sql script (sql/sql.sql) do MySQL, nejlépe přes MySQL workbench#
#######################################################################################################################################################

#testy jsou ve složce test_case

#Program je demostrace/ukázka spojení a základní práci programu v python s DB

#Vybral jsem si obchod s boty, který není ideálním příkladem, protože kdo by chtěl offline obchod... že?
#+ dodávat aplikaci, kde si klient musí naistalovat DBMS není ideální.
#Na to by byla potřeba webovka, takový projekt jsem již dělal můžete se mrknout https://mujtest1234.000webhostapp.com/mojeProjekty/obchudek/index.php
#Zdorjáky a export DB můžu případně dodat.

#Není zde autentifikace uživatele, program je natvrdo nastaven na uživatel_id = 1, u tohoto programu to dle mého ztrací smysl (u demonstrace)

#U alfy3 jsem udělal hodně kompormisů, jako 1 objednávka = 1 produkt, natvrdo uživatel_id = 1, není zde vyřešena ani na 100% sql injection protekce a import dat ze souboru není moc hlídaný (pouze zavedením transakcí, při selhání se commit neprovede).
#Ale myslím si že jsem splnil zadání, tak na 80%.

################################################################
Program spustíte po kliknutí na main.py, který je ve složce src#
################################################################

#Config.csv struktura
<PORT>;
<HOST>;
<USERNAME>;
<PASSWORD>;
<DB_NAME>

#########################################################################
Pokud máte nějaké dotazy, neváhejte mě kontaktovat vasek.taitl@gmail.com#
Program je volně k použití ZDARMA, je pod licencí Creative Commons - BY	#
#########################################################################