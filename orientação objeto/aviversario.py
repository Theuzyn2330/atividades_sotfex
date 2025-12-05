class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1
        print("Nova idade:", self.idade)

dog = Cachorro("Bolt", 5)
dog.aniversario()
