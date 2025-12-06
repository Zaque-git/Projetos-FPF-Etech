# Produto com Preço (Encapsulamento Básico)

# Crie uma classe Produto com:

# Atributos

# nome

# preço (privado)

# Métodos

# set_preco(novo_preco) → atualiza o preço com validação (não aceita preço negativo)

# get_preco() → retorna o preço

# Tarefa

# Criar um produto

# Tentar definir um preço negativo (deve recusar)

# Definir um preço válido

# Mostrar o preço final


class Produto:
    def __init__(self, nome, preco):
        self.nome= nome
        self.preco= preco

    def descricao(self):
        return f"{self.nome}, {self.preco}"
    
lista_produtos=[]

for i in range(3):
    nome = str(input("Digite o nome do produto: "))
    preco = float(input("Digite o preco do produto: "))
    produto = Produto(nome, preco)
    lista_produtos.append(produto)

for produto in lista_produtos:
    print(produto.descricao())
