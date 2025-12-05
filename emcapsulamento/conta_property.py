class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo  # atributo protegido

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, novo_saldo):
        if novo_saldo >= 0:
            self._saldo = novo_saldo
        else:
            print("O saldo não pode ser negativo!")

# Teste
conta = ContaBancaria("Matheus", 100)
print("Saldo atual:", conta.saldo)

conta.saldo = 200
print("Novo saldo:", conta.saldo)

conta.saldo = -50  # não permite
