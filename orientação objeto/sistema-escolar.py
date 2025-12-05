class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.notas = []

    def cadastrar_nota(self, nota):
        self.notas.append(nota)

    def media(self):
        return sum(self.notas) / len(self.notas)

class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina, salario):
        super().__init__(nome, idade)
        self.disciplina = disciplina
        self.salario = salario

# Criando objetos
aluno1 = Aluno("Matheus", 20, "A123")
aluno1.cadastrar_nota(8)
aluno1.cadastrar_nota(9)

prof1 = Professor("Ana", 40, "Python", 3000)

print("Aluno:", aluno1.nome)
print("Média:", aluno1.media())
print("Professor:", prof1.nome, "-", prof1.disciplina)
