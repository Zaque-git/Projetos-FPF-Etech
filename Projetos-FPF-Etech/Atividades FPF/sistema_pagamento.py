class Pagamento:
    def __init__(self, valor):
        self.valor = valor

    def calcular_valor(self):
        # GARANTE QUE O POLIMORFISMO ACONTECA
        return self.valor

class Pagamentocartao(Pagamento):
    def __init__(self,valor, taxa=0.15):
     #  CHAMA O METODO CONSTRUTOR DA CLASSE MAE
        super().__init__(valor)
        self.__taxa = taxa


    def calcular_valor(self):
        return self.valor + (self.valor * self.__taxa)

class PagamentoPix(Pagamento):
    def __init__(self, valor, desconto = 0.20):
        super().__init__(valor)
        self.__desconto= desconto
    
    def calcular_valor(self):
        return self.valor-(self.valor*self.__desconto)


pagamentos=[]

quantidade = int(input("Informe a quantidade de pagamentos: "))

valor = float(input("Digite o valor da compra: "))

for i in range(quantidade):
    print("\n 1 - PAGAMENTO POR CARTAO")
    print("2 - PAGAMENTO POR PIX")
    tipo = int(input("Selecione o tipo de pagamento: "))

    if tipo == 1:
        pagamento = Pagamentocartao(valor)
    
    elif tipo == 2:
        pagamento= PagamentoPix(valor)

    else:
        print("\n Tipo invalido!")
    
    pagamentos.append(pagamento)

    total_geral = 0
for f in pagamentos:
    valor_final = pagamento.calcular_valor()

    print(f"Total final do pagamento: {valor_final}")

    total_geral =+ valor_final

    print(f"Total processado: {total_geral}")






