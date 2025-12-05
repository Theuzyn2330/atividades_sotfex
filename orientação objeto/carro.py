#Questão 1

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f"Seu carro é da marca {self.marca} modelo {self.modelo}"
    
marca_carro = input("Qual a marca do seu carro?; ")
modelo_carro = input("Qual modelo?; ")
p1 = Carro(marca_carro, modelo_carro)
print(p1)