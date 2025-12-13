def calcular_combustivel(missao_base, *gastos_adicionais):
    combustivel = missao_base*100
    total_gastos = 0
    for gastos in gastos_adicionais:
        total_gastos+=gastos

    total= combustivel + gastos

    print(f"O total de combustivel necessario vai ser: {total}")
    return total

missao_base= int(input("Digite a quantidade de missao bases realizadas: "))

lista_gastos= []
contador= 0

while contador < 3 :
    gastos_adicionais = int(input("Digite os gastos adicionais: "))
    lista_gastos.append(gastos_adicionais)
    contador+=1

total=calcular_combustivel(missao_base, *lista_gastos)

print (total)