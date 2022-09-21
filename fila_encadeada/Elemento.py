class Elemento():
    def __init__(self, info) -> None:
        self.__info = info
        self.__proximo = None

    def info(self):
        return self.__info

    def proximo(self):
        return self.__proximo

    def set_proximo(self, Elemento):
        self.__proximo = Elemento
