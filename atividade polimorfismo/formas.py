import math

# Classe base
class Forma:
    def area(self):
        pass  # Método genérico, será sobrescrito pelas classes filhas

# Classe filha Quadrado
class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

# Classe filha Círculo
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * self.raio ** 2

# Função para imprimir áreas de uma lista de formas
def imprimir_areas(lista_formas):
    for forma in lista_formas:
        print(f"{forma.__class__.__name__}: Área = {forma.area():.2f}")

# Testando
formas = [
    Quadrado(4),
    Circulo(3),
    Quadrado(10),
    Circulo(5)
]

imprimir_areas(formas)
