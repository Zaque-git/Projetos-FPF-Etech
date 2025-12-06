numero1=float(input("Digite um numero: "))
numero2=float(input("Digite outro numero: "))

ocasiao=str(input("Deseja adicionar mais um numero?")).upper()
n=0

def adicao(*numeros):
    return sum(numeros)

def subtracao(*numeros):
    resultado= numeros[0]
    for n in numeros[1:]:
        resultado-= n
    return resultado

def multiplicacao(*numeros):
    resultado= numeros[0]
    for n in numeros[1:]:
        resultado*=n
    return resultado

def divisao(*numeros):
    resultado=numeros[0]
    for n in numeros[1:]:
        if n==0:
            print("Erro! divisao por zero")
        else:
            resultado/=n
    return resultado 


if ocasiao=="SIM":
    numero3=float(input("Digite outro numero: "))
    numeros = (numero1, numero2, numero3)

else:
    print("Ok! Vamos continuar a operacao..")
    numeros= (numero1, numero2)

print("Selecione a operacao: ")
print("1 - ADICAO ")
print("2 - SUBTRACAO")
print("3 - MULTIPLICACAO ")
print("4 - DIVISAO ")

operacao=int(input("Digite qual operacao voce quer: "))

if operacao == 1:
    print("Resultado:", adicao(*numeros))
elif operacao == 2:
    print("Resultado:", subtracao(*numeros))
elif operacao == 3:
    print("Resultado:", multiplicacao(*numeros))
elif operacao == 4:
    print("Resultado:", divisao(*numeros))
else:
    print("Operacao incorreta. Reinicie o programa e tente novamente.")