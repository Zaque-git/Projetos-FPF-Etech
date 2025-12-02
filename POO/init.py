class Livro:
    def __init__(self, titulo_dado, autor_dado):
        self.titulo_dado = titulo_dado
        self.autor_dado = autor_dado

livro_1=Livro("interestrelar", "Isaque")
print(livro_1.titulo_dado)