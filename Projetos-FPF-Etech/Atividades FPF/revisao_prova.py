class Funcionario:

    def __init__(self,nome):
        self.__nome = nome # ATRIBUTO PRIVADO

    def get_nome(self):     # GETTER
        return self.__nome

    def calcular_salario(self):
        return 0  #  O METODO VAI SER SUBSCRITO (POLIMORFISMO)

class FuncionarioCLT(Funcionario):

    def __init__(self, nome, salario_fixo):
        super().__init__(nome)
        self.__salario = salario_fixo

    def get_salario(self):
        return self.__salario

    def calcular_salario(self):
        return self.__salario

class FuncionarioHorista(Funcionario):
    def __init__(self, nome, horas_trabalhadas, valor_hora):
        super().__init__(nome)
        self.__horas_trabalhadas = horas_trabalhadas
        self.__valor_hora = valor_hora

    def calcular_salario(self):
        return self.__horas_trabalhadas * self.__valor_hora


funcionarios = []
total_folha = 0

quantidade_funcionarios=int(input("Quantos funcionarios deseja cadastrar? "))

for i in range(quantidade_funcionarios):
    print("\n 1 - Funcionario CLT")
    print("2 - Funcionario Horista")
    tipo = int(input("Escolha o tipo de funcionario: "))

    nome = input("Informe o nome do funcionario: ")

    if tipo == 1:
        salario = float(input("Informe o salario do funcionario: "))
        funcionario = FuncionarioCLT(nome, salario)

    elif tipo == 2:
        horas = float(input("Informe o horas trabalhadas: "))
        valor = float(input("Informe o valor da hora trabalhada: "))
        funcionario = FuncionarioHorista(nome, horas, valor)

    else:
        print("Tipo invalido!")
        continue

    funcionarios.append(funcionario)

print("\n -- Folha de pagamento --")

for f in funcionarios:
    salario = f.calcular_salario()
    print(f"{f.get_nome()} - Salario: {salario : .2f}")
    total_folha += salario

print(f"Total de folha de pagamento: {total_folha:.2f}")

