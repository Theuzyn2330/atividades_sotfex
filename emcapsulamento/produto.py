class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    @property
    def nome(self):
        return self.__nome  # só leitura

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco >= 0:
            self.__preco = novo_preco
        else:
            print("O preço não pode ser negativo!")

# Teste
produto = Produto("Notebook", 2500)

print("Produto:", produto.nome)
print("Preço:", produto.preco)

produto.preco = 3000
print("Novo preço:", produto.preco)

produto.preco = -100  # não permite
