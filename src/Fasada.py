from DB_controler import Conn
from Debug import Debug
import time

class Fasada:
    """
    Class for DB handling
    """
    def __init__(self):
        conn = Conn()
        self._connection = conn.getConn()
        self._mycursor = self._connection.cursor()

    def _get_Platby(self):
        """
        Get all data from table platba
        :return: list
        """
        sql = "SELECT id,nazev,cena from platba"
        self._mycursor.execute(sql)
        return self._mycursor.fetchall()

    def sql_protection(self,input):
        if "--" in input or ";" in input or "=" in input:
            raise Exception("Nepovolené znaky")

        return input

    def _get_all_my_orders(self,id_user = int):
        """
        Select all orders from DB where id_user = id_user
        :param id_user:
        :return: list
        """
        sql = "select produkt_bota.id as id,znacka.nazev as znacka,produkt_bota.nazev as nazev,velikost,kus,cena from produkt_bota inner join znacka on znacka.id = id_znacka where produkt_bota.nazev = (%s) and kus > 0"
        val = [id_user]
        self._mycursor.execute(sql, val)

    def _kupovat_botu(self,nazev,pocet_ks,id_user,platba,velikos):
        """
        Insert order into DB
        :param nazev: str
        :param pocet_ks: int
        :param id_user: int
        :param platba: int
        :param velikos: int
        :return: True (or raise Exeption)
        """
        sql = "insert into objednavka (id_user, id_bota, id_platba, vytvoreni, kusu, zaplaceno) values((%s),(select id from produkt_bota where nazev = (%s) and velikost = (%s)),(%s),(%s),(%s),(%s))"
        val = (id_user,nazev,str(velikos),int(platba),time.strftime('%Y-%m-%d'),pocet_ks,False)
        self._mycursor.execute(sql, val)
        #self._connection.commit()

        sql = "Update produkt_bota set kus = kus - (%s) where nazev = (%s) and velikost = (%s)"
        val = (pocet_ks,nazev,str(velikos))
        self._mycursor.execute(sql, val)
        self._connection.commit()

        return True

    def _bota_from_name(self,where):
        """
        Select data from produkt_bota where name = where
        :param where: str
        :return: list
        """
        where = self.sql_protection(where)
        sql = "select produkt_bota.id as id,znacka.nazev as znacka,produkt_bota.nazev as nazev,velikost,kus,cena from produkt_bota inner join znacka on znacka.id = id_znacka where produkt_bota.nazev = (%s) and kus > 0"
        val = [where]
        self._mycursor.execute(sql, val)

        return self._mycursor.fetchall()

    def _get_nabidka_DB(self,where = None):
        """
        Get all data from store, optional where znacka
        :return: list
        """
        if where == None:
            sql = "SELECT * from select_bota"
            self._mycursor.execute(sql)
            return self._mycursor.fetchall()

        where = self.sql_protection(where)

        sql = "select produkt_bota.id as id,znacka.nazev as znacka,produkt_bota.nazev as nazev,velikost,kus,cena from produkt_bota inner join znacka on znacka.id = id_znacka where znacka = (%s)"
        val = [where]
        self._mycursor.execute(sql, val)

        return self._mycursor.fetchall()


    def _get_user_data(self,id_user = int):
        """
        int jako protekce proti sql_injection stačí
        :param id_user: int
        :return: list[tuple]
        """
        sql = "select produkt_bota.nazev as nazev,produkt_bota.velikost as velikost, vytvoreni, zaplaceno, dodano,znacka.nazev as znacka from objednavka inner join produkt_bota on id_bota = produkt_bota.id inner join znacka on id_znacka = znacka.id where id_user = (%s)  order by produkt_bota.id"
        val = [id_user]
        self._mycursor.execute(sql, val)

        return self._mycursor.fetchall()

    def _delete_history_from_user(self,id_user = int):
        """
        Delete data from table objednavka where id_user = id_user
        :param id_user: int
        :return:
        """
        sql = "DELETE from objednavka where id_user = (%s)"
        val = [id_user]
        self._mycursor.execute(sql, val)
        self._connection.commit()
        return True

    def _insert_znacky(self,list_data):
        """
        Insert data into table produkt_bota
        :param list_data: list - list[list[data with deli , ]]
        """
        if len(list_data) < 1:
            return
        for x in list_data:
            if x == " " or x == "":
                return
            sql = "INSERT INTO znacka (nazev) values((%s))"
            val = [x]
            self._mycursor.execute(sql, val)

        self._connection.commit()

    def _insert_bota(self,list_data):
        """
        Insert data into table produkt_bota
        :param list_data: list - list[list[data with deli , ]]
        """
        if len(list_data) < 1:
            return
        list_data_split = []
        for x in list_data:
            list_data_split.append(x.split(","))
        Debug(list_data_split)

        for x in list_data_split:
            if x[0] == " " or x[0] == "":
                return
            sql = "INSERT INTO produkt_bota (id_znacka,nazev,cena,velikost,kus) values ((%s),(%s),(%s),(%s),(%s))"
            val = [int(x[0]),str(x[1]),int(x[2]),str(x[3]),int(x[4])]
            self._mycursor.execute(sql, val)

        self._connection.commit()