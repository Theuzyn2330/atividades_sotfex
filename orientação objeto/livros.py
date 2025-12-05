class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def exibir_livro(self):
        print(f"{self.titulo:<20} {self.autor:<15} {self.ano:<5}")

livros = [
    Livro("Dom Casmurro", "Machado de Assis", 1899),
    Livro("1984", "George Orwell", 1949),
    Livro("O Alquimista", "Paulo Coelho", 1988)
]

print(f"{'Título':<20} {'Autor':<15} {'Ano Publicado':<5}")
print("-" * 45)

for livro in livros:
    livro.exibir_livro()
