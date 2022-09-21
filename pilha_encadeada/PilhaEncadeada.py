from Elemento import Elemento

class PilhaEncadeada():
    def __init__(self) -> None:
        self.__topo  = None
        self.__tamanho = 0

    def push(self, info):
        if not self.__topo:
            self.__topo = Elemento(info)
        else:
            novo = Elemento(info)
            novo.set_anterior(self.__topo)
            self.__topo = novo
        self.__tamanho += 1

    def pop(self):
        info = self.__topo.info()
        self.__topo = self.__topo.anterior()
        self.__tamanho -= 1
        return info