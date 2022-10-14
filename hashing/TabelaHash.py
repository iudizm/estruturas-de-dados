from ListaEncadeadaParaHash import ListaEncadeada

class TabelaHash():
    def __init__(self, tamanho) -> None:
        self.__tamanho = tamanho
        self.__tabela = [None] * self.__tamanho
        for i in range (0, self.__tamanho):
            self.__tabela[i] = ListaEncadeada()

    def busca(self, chave):
        return self.__tabela[self.hash(chave)]

    def insere(self, chave, dado):
        grupo = self.hash(chave)
        if self.__tabela[grupo].esta_vazia():
            self.__tabela[grupo].insere_no_comeco(dado, chave)
        else:
            print(
                "colisão no grupo:" 
                + str(grupo) + " com a chave: " + str(chave)
                )

    def hash(self, chave):
        # assumindo que a chave é um valor numérico inteiro
        return chave % self.__tamanho

    def tabela(self):
        return self.__tabela

t = TabelaHash(100)
t.insere(192, "haha")
t.insere(195, "oi")
t.insere(191, "oi")
t.insere(193, "oi")

for grupo in t.tabela():
    if grupo.esta_vazia():
        print("vazia\n")
    else:
        print(str(grupo.cabeca().chave()))
    print("---->" + str(grupo.imprime()))
