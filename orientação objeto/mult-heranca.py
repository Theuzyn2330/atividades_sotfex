class Artista:
    def apresentar(self):
        print("Sou artista")

class Programador:
    def apresentar(self):
        print("Sou programador")

class PessoaMultiTalento(Artista, Programador):
    pass

p = PessoaMultiTalento()
p.apresentar()  
