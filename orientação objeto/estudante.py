#Questões 7, 8 e 9

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Estudante(Pessoa):
    def __init__(self, nome, idade, matricula, curso):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.curso = curso

    def __str__(self):
        return f"Estudante: {self.nome}, Idade: {self.idade}, Matrícula: {self.matricula}, Curso: {self.curso}"

nome = input("Nome do estudante: ")
idade = int(input("Idade: "))
matricula = input("Matrícula: ")
curso = input("Curso: ")
aluno = Estudante(nome, idade, matricula, curso)
print(aluno)

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def decimo_terceiro(self):
        return self.salario

func = Funcionario("Carlos", 30, 2000)
print("13º salário:", func.decimo_terceiro())


class Professor(Funcionario):
    def __init__(self, nome, idade, salario, disciplina):
        super().__init__(nome, idade, salario)
        self.disciplina = disciplina

    def apresentar(self):
        print(f"Professor {self.nome} leciona {self.disciplina}")

prof = Professor("Ana", 40, 3500, "Matemática")
prof.apresentar()

