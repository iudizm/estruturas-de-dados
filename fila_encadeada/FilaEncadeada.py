from Elemento import Elemento

class PilhaEncadeada():
    def __init__(self) -> None:
        self.__inicio  = None
        self.__fim = None
        self.__tamanho = 0

    def enqueue(self, info):
        if self.__tamanho == 0:
            self.__inicio = Elemento(info)
            self.__fim = self.__inicio
        else:
            novo = Elemento(info)
            self.__fim.set_proximo(novo)
            self.__fim = novo
            self.__tamanho += 1

    def dequeue(self):
        if self.__inicio:
            info = self.__inicio.info()
            self.__inicio = self.__inicio.proximo()
            self.__tamanho -= 1
            return info
        return False