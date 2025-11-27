class Animal:
    def __init__(self, animal):
       self.animal = animal

    def falar(self):
        print("faz barulho")

class Cachorro(Animal):
    def falar(self):
        print("Auau")


class Gato(Animal):
   
   def falar(self): 
        print("Miau")

class Porco(Animal):
    def falar(self):
        print("oinc-oinc")


class Boi(Animal):
    def falar(self):
        print("Muuuh")


boi = Boi("Boi")
cao = Cachorro("Cachorro")
gato = Gato("Gato")
porco = Porco("Porco")

for x in (boi, cao, gato, porco):
    print(x.animal)
    x.falar()














