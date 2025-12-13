class Programador:
    def __init__(self, nome, linguagem, produtividade= 100):
        self.nome= nome
        self.linguagem= linguagem
        self.produtividade= produtividade

    def codificar(self, horas):
        self.pontos_perdidos= horas * 5
        self.produtividade-=self.pontos_perdidos
        print(f"Sua produtividade apos {horas} de trabalho é: {self.produtividade}")

    def tomar_cafe(self):
        self.produtividade = self.produtividade + 15
        print(f"A sua produtividade foi restaurada: {self.produtividade}")
    
    def verificar_produtividade(self):
        print(f"A sua produtividade atual é: {self.produtividade}")

programador=Programador("Isaque", "Python")

programador.codificar(8) # Quantidade de horas
programador.tomar_cafe()
programador.verificar_produtividade()

