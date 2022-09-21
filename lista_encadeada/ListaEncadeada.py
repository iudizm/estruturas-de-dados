from Elemento import Elemento

class ListaEncadeada():
    def __init__(self) -> None:
        self.__cabeca = None
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
    def insere(self, info, index):
        novo_elemento = Elemento(info)
        if self.__tamanho == 0:
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

    def insere_no_fim(self, info):
        self.insere(info, self.tamanho())

    def insere_no_comeco(self, info):
        self.insere(info, 0)

# -------
    def insere_ordenado(self, info):
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

lista = ListaEncadeada()
lista.imprime()
lista.insere_no_fim("oi1")
lista.imprime()
lista.insere_no_fim("oi2")
lista.imprime()
lista.insere_no_fim("oi3")
lista.imprime()
lista.insere_no_comeco("oi no começooo")
lista.imprime()
print("tamanho: " + str(lista.tamanho()))
print("head: " + lista.cabeca().info())
lista.imprime()
