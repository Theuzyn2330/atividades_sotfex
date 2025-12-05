class Conta:
    def __init__(self, saldo):
        self.__saldo = saldo  # atributo privado

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
       if valor >= 0:
           self.__saldo  = valor
       else:
           print("Valor invalido")

# Uso
c = Conta(100)
print(c.saldo)
c.saldo = 200
print(c.saldo)
c.saldo = -50
# conta.__saldo  --> Isso dá erro! (encapsulamento)
