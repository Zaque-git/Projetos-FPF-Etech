class funcionario:
    def __init__(self, nome, cargo):
        self.nome=nome
        self.cargo=cargo

funcionario1=funcionario("Isaque", "Top das galaxias")
print(funcionario1.nome)
print(funcionario1.cargo)