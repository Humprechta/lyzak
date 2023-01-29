import mysql.connector
from Debug import Debug
from Print import Print
from Napoveda import Napoveda

class Conn():
    """
    Singleton class to load config data and connect to db
    """
    _instance = None
    def __init__(self):
        self._static_path = "../config/config.csv"

    def _configRead(self):
        """
        Read all data from file
        :retrun: str
        """
        with open(self._static_path, "r") as file:
            return file.read()
    def _get_config_data(self):
        """
        (Private) function to get and split data from file
        :return: list
        """
        data = self._configRead()

        Debug(data)

        data = data.split(";\n")

        if int(data[0]) <= 0:
            raise Exception("bad config data - port")

        if len(data) > 5 or len(data) < 4:
            raise Exception("bad config data")

        Debug(data[4])

        return data

    def getConn(self):
        """
        Function to get connection
        """
        data = self._get_config_data()
        try:

            self._connection = mysql.connector.connect(
                host=data[1],
                user=data[2],
                password=data[3],
                database=data[4]
            )

            self._connection.autocommit = False

            return self._connection

        except Exception as e:
            pp = Print("Nepovedlo se připojit k DB, po zmáčknutí klávesy enter se program ukončí...\nzkuste přenastavit config soubor")
            pp.deli()
            pp.print("Vypisuji nápovědu...")
            pp.deli()
            pp.print(Napoveda().get_napoveda())
            input()
            exit(0)

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance