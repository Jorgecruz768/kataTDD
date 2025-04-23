class Conjunto:
    def __init__(self, conjunto):
        self.__conjunto = conjunto

    def promedio(self):
        if not self.__conjunto:
            return None  # o lanzar una excepción
        return sum(self.__conjunto) / len(self.__conjunto)
