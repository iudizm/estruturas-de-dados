class Elemento():
    def __init__(self, info) -> None:
        self.__info = info
        self.__anterior = None

    def info(self):
        return self.__info

    def anterior(self):
        return self.__anterior

    def set_anterior(self, Elemento):
        self.__anterior = Elemento
