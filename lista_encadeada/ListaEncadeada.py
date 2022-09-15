from Elemento import Elemento

class ListaEncadeada():
    def __init__(self) -> None:
        self.__cabeca = Elemento(None)
        self.__tamanho = 0

    def ultimo_elemento(self):
        elemento = self.__cabeca
        for i in range(0, self.tamanho()):
            elemento = elemento.proximo()
            i += 1
        return elemento

# -------
    def clear(self):
        pass

# -------
    def insert(self, info, index):
        novo_elemento = Elemento(info)
        if index == 0:
            novo_elemento.set_proximo(self.__cabeca)
            self.__cabeca = novo_elemento
        else:
            anterior = self.__cabeca
            for i in range(0, index):
                anterior = anterior.proximo()
                i += 1
            novo_elemento.set_proximo(anterior.proximo())
            anterior.set_proximo(novo_elemento)
        self.__tamanho += 1

    def push_fim(self, info):
        self.insert(info, self.tamanho())

    def push_comeco(self, info):
        self.insert(info, 0)

# -------
    def insert_sorted(self, info):
        pass

# -------
    def busca_info_por_posicao(self, index):
        pass

# -------
    def busca_posicao_por_info(self, info):
        pass

# -------
    def pop(self, index):
        pass

    def pop_fim(self):
        self.pop(self.tamanho() - 1)

    def pop_comeco(self):
        self.pop(0)

    def remover_elemento_por_info(self, info):
        self.pop(self.busca_posicao_por_info(info))

    def esta_vazia(self):
        return self.tamanho() == 0

    def contem(self, info):
        return self.busca_posicao_por_info(info) != self.tamanho()

    def tamanho(self):
        return self.__tamanho

    def cabeca(self):
        return self.__cabeca        


lista = ListaEncadeada()

print(lista.tamanho())
print(lista.ultimo_elemento().info())
lista.push_fim("oi1")
lista.push_fim("oi2")
lista.push_fim("oi3")
lista.push_comeco("oi no começooo")
print(lista.tamanho())
print(lista.cabeca().info())