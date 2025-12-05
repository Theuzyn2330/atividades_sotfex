class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def dirigir(self):
        print("O carro está em movimento")

carro = Carro("Fiat", "Uno")
carro.dirigir()
