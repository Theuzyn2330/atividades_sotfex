from abc import ABC, abstractmethod

class Cancelavel(ABC):
    @abstractmethod
    def cancelar_pagamento(self):
        pass


class Pagamento(ABC):
    def __init__(self, valor):
        self.valor = valor

    @abstractmethod
    def processar_pagamento(self):
        pass

class CartaoCredito(Pagamento, Cancelavel):
    def __init__(self, valor, numero_cartao, nome_titular):
        super().__init__(valor)

        self.numero_cartao = numero_cartao
        self.nome_titular = nome_titular


    def processar_pagamento(self):
            print(f"Processando pagamento  de R${self.valor} com o cartão {self.nome_titular}.")

    def cancelar_pagamento(self):
         print(f"Pagamento de R${self.valor} com cartão de credito foi cancelado")

class Pix(Pagamento, Cancelavel):
     def __init__(self, valor, chave_pix):
          super().__init__(valor)
          self.chave_pix = chave_pix

     def processar_pagamento(self):
            print(f"Processando pagamento  de R${self.valor} via Pix com o a chave:({self.chave_pix}.)") 

     def  cancelar_pagamento(self):
         print(f"Pagamento de R${self.valor} via Pix foi cancelado")

class Boleto(Pagamento, Cancelavel):
     def __init__(self, valor, numero_boleto):
          super().__init__(valor)
          self.numero_boleto = numero_boleto

     def processar_pagamento(self):
            print(f"Processando pagamento  de R${self.valor} via boleto com o numero {self.numero_boleto}.)") 

     def  cancelar_pagamento(self):
         print(f"Pagamento de R${self.valor} via boleto foi cancelado")


# def testar_pagamentos():
    #pagamento_cartao = CartaoCredito(150.0, "1234-5678-9876-5432", "João Silva")
    #pagamento_pix = Pix(200.0, "joaosilva@pix.com")
    #pagamento_boleto = Boleto(120.0, "987654321")

   # pagamento_cartao.processar_pagamento()
   # pagamento_pix.processar_pagamento()
   # pagamento_boleto.processar_pagamento()

  # pagamento_cartao.cancelar_pagamento()
   # pagamento_pix.cancelar_pagamento()
   # pagamento_boleto.cancelar_pagamento()

#testar_pagamentos()



