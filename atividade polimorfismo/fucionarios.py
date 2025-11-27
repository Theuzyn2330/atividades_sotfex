class Funcionario:
        def salario(self):
                pass
        
class Gerente(Funcionario):
               def salario(self):
                  return 5000.0

class Estagiario(Funcionario):
           def salario(self):
                  return 1500


funcionario = [Gerente(), Estagiario(), Gerente()]

for i, funcionario in enumerate(funcionario, start=1):
    print(f"Funcionário {i}: Salário = R${funcionario.salario()}")