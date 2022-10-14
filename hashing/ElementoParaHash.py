class Elemento():
    def __init__(self, info, chave) -> None:
        self.__info = info
        self.__chave = chave
        self.__proximo = None

    def info(self):
        return self.__info
    
    def chave(self):
        return self.__chave

    def proximo(self):
        return self.__proximo

    def set_proximo(self, Elemento):
        self.__proximo = Elemento
