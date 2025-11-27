class Carro:
   def __init__(self, marca, modelo):
       self.marca = marca
       self.modelo = modelo

   def mover(self):
       print(f"O carro {self.marca} {self.modelo} está se movendo.")

class Aviao:
   def __init__(self, marca, modelo):
       self.marca = marca
       self.modelo = modelo

   def mover(self):
       print(f"O avião {self.marca} {self.modelo} está voando.")

class Barco:
   def __init__(self, marca, modelo):
       self.marca = marca
       self.modelo = modelo

   def mover(self):
       print(f"O barco {self.marca} {self.modelo} está navegando.")

carro = Carro("Toyota", "Corolla")
aviao = Aviao("Boeing", "747")
barco = Barco("Ferry", "Express")

for x in (carro, aviao, barco):
   x.mover()