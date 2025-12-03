class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def exibirinfo(self):
        print(f"O titulo: {self.titulo}")
        print(f"O autor: {self.autor}")

print("-"*20)
titulo= input("Insira o titulo: ")
autor = input("Insira o autor: ")
print("-"*20)

livro= Livro(titulo, autor)
livro.exibirinfo()

