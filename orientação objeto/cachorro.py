class Dog():
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade

    def cachorro_fala(self):
        print(f"AuAu, Meu nome é {self.nome} e eu tenho {self.idade} anos, AuAu")

nome_input = input("Digite o nome do cachorro: ")
idade_input = int(input("Digite a idade do cachorro: "))  

p1 = Dog(nome_input, idade_input)
p1.cachorro_fala()
