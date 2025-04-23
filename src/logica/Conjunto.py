class Conjunto:
    def __init__(self, conjunto):
        self.__conjunto = conjunto

    def promedio(self):
        if len(self.__conjunto) == 0:
            return None
        if len(self.__conjunto) == 1:
            return self.__conjunto[0]
