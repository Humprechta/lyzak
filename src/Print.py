
class Print:
    """
    Class for print into console
    """
    _file_content = None
    _instance = None

    def __init__(self,input = None):
        self.print(input)

    def print(self,input):
        if input == None:
            return
        print(input)

    def array_to_str(self,array):
        """
        array into redable string
        :param array: list
        :return: str
        """
        string = ""
        for x in array:
            string = string + x + ", "
        return (string[:-2])#odstraneni posledni carky a mezery

    def deli(self):
        print("----------")
