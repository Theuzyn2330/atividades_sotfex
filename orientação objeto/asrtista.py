class Artista:
    def apresentar(self):
        print("Sou artista")
        super().apresentar()

class Programador:
    def apresentar(self):
        print("Sou programador")

class PessoaMultiTalento(Artista, Programador):
    def apresentar(self):
        super().apresentar()

p = PessoaMultiTalento()
p.apresentar()
