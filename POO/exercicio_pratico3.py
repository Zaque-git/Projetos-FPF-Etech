class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.salario_novo = salario * 0.10


    def calcular_bonus(self):
        return self.salario + self.salario_novo

    def exibirinfo(self):
        print(f"Nome: {self.nome}")
        print(f"Cargo: {self.cargo}")
        print(f"Salario: {self.salario}")
        print(f"Salario novo (10% de bonus): {self.salario_novo}")
        print(f"Salário final: {self.calcular_bonus()}")

print("-"*20)
nome=input("Digite seu nome: ")
cargo=input("Digite sua cargo: ")
salario=float(input("Digite sua salario: "))
print("-"*20)

func=Funcionario(nome, cargo, salario)
func.exibirinfo()



