from ElementoParaHash import Elemento

class ListaEncadeada():
    def __init__(self) -> None:
        self.__cabeca = None
        self.__tamanho = 0

    def acessa_ultimo(self):
        if not self.esta_vazia():
            elemento = self.__cabeca
            for i in range(0, self.tamanho()):
                elemento = elemento.proximo()
            return elemento
        return "lista vazia"

    def acessa_primeiro(self):
        return self.__cabeca.info()

    def clear(self):
        pass

    #  TO-DO: criar os nós com chave e valor p usar no bucket
    def insere(self, info, chave, index):
        novo_elemento = Elemento(info, chave)
        if self.esta_vazia():
            self.__cabeca = novo_elemento
        else:
            if index == 0:
                novo_elemento.set_proximo(self.__cabeca)
                self.__cabeca = novo_elemento
            else:
                anterior = self.__cabeca
                for i in range(1, index):
                    anterior = anterior.proximo()
                novo_elemento.set_proximo(anterior.proximo())
                anterior.set_proximo(novo_elemento)
        self.__tamanho += 1

    def insere_no_fim(self, info, chave):
        self.insere(info, chave, self.tamanho())

    def insere_no_comeco(self, info, chave):
        self.insere(info, chave, 0)

    def insere_antes_de(self, referencia, info, chave):
        self.insere(info, chave, self.busca_posicao_por_info(referencia))

    def insere_depois_de(self, referencia, info, chave):
        self.insere(info, chave, (self.busca_posicao_por_info(referencia) + 1))

    def busca_info_por_posicao(self, index):
        if not self.esta_vazia():
            elemento = self.__cabeca
            for i in range(0, index):
                elemento = elemento.proximo()
            return elemento.info()
        return "lista vazia"

    def busca_posicao_por_info(self, info):
        elemento = self.__cabeca
        for i in range(0, self.tamanho()):
            if elemento.info() == info:
                print("encontrado em indice:" + str(i) + "o valor" + info)
                return i
            elemento = elemento.proximo()
        return None

    def busca_posicao_por_chave(self, chave):
        elemento = self.__cabeca
        for i in range(0, self.tamanho()):
            if elemento.chave() == chave:
                print("encontrado em indice:" + str(i) + "a chave" + chave)
                return i
            elemento = elemento.proximo()
        return None

    def pop(self, index):
        if not self.lista_vazia():
            anterior = self.__cabeca
            for i in range(1, index):
                anterior = anterior.proximo()
            info = anterior.proximo.info()
            anterior.set_proximo(anterior.proximo().proximo())
            return info
        return False

    def pop_do_fim(self):
        self.pop(self.tamanho() - 1)

    def pop_do_comeco(self):
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
        
    def imprime(self):
        array = []
        if self.__cabeca:	
            c = self.__cabeca
            for i in range(0, self.__tamanho):
                array.append(c.info())
                c = c.proximo()
            print(array)
        else:
            print("lista vazia")

