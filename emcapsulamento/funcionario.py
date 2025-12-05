class Funcionario:
    def __init__(self, salario):
        self.__salario = salario  # atributo privado

    def get_salario(self):
        return self.__salario

class Gerente(Funcionario):
    def __init__(self):
        super().__init__(5000)

class Estagiario(Funcionario):
    def __init__(self):
        super().__init__(1500)

funcionarios = []

quantidade = int(input("Quantos funcionários deseja cadastrar? "))

for i in range(quantidade):
    print(f"\nFuncionário {i+1}:")
    tipo = input("É um Gerente ou Estagiario? (G/E): ").strip().upper()

    if tipo == 'G':
        funcionario = Gerente()
    elif tipo == 'E':
        funcionario = Estagiario()
    else:
        print("Tipo inválido! Pulando este funcionário.")
        continue

    funcionarios.append(funcionario)

print("\n--- Lista de Salários ---")
for i, funcionario in enumerate(funcionarios, start=1):
    print(f"Funcionário {i}: Salário = R${funcionario.get_salario()}")
