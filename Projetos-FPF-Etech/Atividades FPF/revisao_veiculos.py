class VeiculoEspacial: # CLASSE MAE

    def __init__(self,nome,combustivel):   # METODO CONSTRUTOR
        self.__combustivel = combustivel
        self.__nome = nome

    def get_nome(self): # RETORNA O NOME DA NAVE
        return self.__nome
    
    def consumir_combustivel(self, quantidade): # METODO DE CONSUMO DO COMBUSTIVEL
        if self.__combustivel >= quantidade: # VERIFICA SE HÁ COMBUSTIVEL
            self.__combustivel -= quantidade
            return True # RETORNA SUCESSO
        else:
            self.__combustivel = 0 # EVITA VALORES NEGATIVOS
            return False # RETORNA FALHA
    
    def get_combustivel_restante(self):
        return self.__combustivel # RETORNA O RESULTADO DO METODO DE CONSUMO DO COMBUSTIVEL

    
class NaveCarga(VeiculoEspacial): # CLASSE FILHAS

    TAXA_CONSUMO = 20 # TAXA DE CONSUMO DA NAVE

    def __init__(self,nome,combustivel): # METODO CONSTRUTOR DA CLASSE FILHA
        super().__init__(nome,combustivel) # PUXA OS ATRIBUTOS DA CLASSE MAE 
       

    def consumir_combustivel(self):   # METODO DE CONSUMO APARTIR DA TAXA DE CONSUMO
        super().consumir_combustivel(self.TAXA_CONSUMO)


class NaveExploracao(VeiculoEspacial): # CLASSE FILHA 

    TAXA_CONSUMO= 45 # TAXA DE CONSUMO DA NAVE 

    def __init__(self,nome,combustivel): # METODO CONSTRUTOR DA CLASSE FILHA
       return super().__init__(nome,combustivel) # PUXA OS ATRIBUTOS DA CLASSE MAE
        
    
    def consumir_combustivel(self): # METODO DE CONSUMO APARTIR DA TAXA DE CONSUMO
        return super().consumir_combustivel(self.TAXA_CONSUMO)
    


lista_nave = [] # LISTA NA QUAL ARMAZENA AS INFORMACOES DA NAVE


quantidade = int(input("Informe a quantidade de naves que deseja: "))

for i in range(quantidade):

    nome = str(input("Informe o nome da nave: "))
    print("1 - NAVE CARGA")
    print("2 - NAVE EXPLORACAO")
    tipo = int(input("Selecione o tipo de nave: "))
    
    if tipo == 1:
        combustivel = int(input("Informe a quantidade de combustivel na nave: "))
        nave = NaveCarga(nome,combustivel)
        lista_nave.append(nave)

    elif tipo == 2:
        combustivel = int(input("Informe a quantidade de combustivel na nave: "))
        nave = NaveExploracao(nome,combustivel)
        lista_nave.append(nave)
    else:
        print("Tipo invalido!")
    

for nave in lista_nave:
    
    nave.consumir_combustivel() 

    # Exibe o status final
    print(f"Status da NAVE {nave.get_nome()}:")
    print(f"   Taxa de consumo: {nave.TAXA_CONSUMO}")
    print(f"   Combustível restante: {nave.get_combustivel_restante()}")