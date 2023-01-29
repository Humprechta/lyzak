from os.path import exists
class File_ha():
    """
    Class for file handling and parsing data from csv
    """

    def __init__(self,path):

        self._path = path

    def _check_file(self):
        if not exists(self._path):
            raise Exception("Soubor se nenašel")

    def _read_file(self):
        with open(self._path, "r") as file:
            return file.read()

    def load_file(self):
        """
        Load file, if file not found or isn´t readable raise Exeption
        Return list in list, first index is znacky, second is boty
        :return: list
        """
        self._check_file()
        try:
            data = self._read_file()
        except:
            raise Exception("Soubor se nepovedlo otevřít")
        return self._parse_data(data)

    def _parse_data(self,data):

        data = data.split("\n##\n")
        data[0] = data[0].split(";\n")
        data[1] = data[1].split(";\n")

        temp_list_znacky = []
        temp_list_bot = []

        for x in data[0]:
            temp_list_znacky.append(x.strip())

        for x in data[1]:
            temp_list_bot.append(x.strip())

        print(temp_list_bot)

        return [temp_list_znacky,temp_list_bot]






