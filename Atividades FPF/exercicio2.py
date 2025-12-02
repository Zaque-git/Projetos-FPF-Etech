lista_inteiros=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

pares=[]
impares=[]

for numero in lista_inteiros:
    if numero%2==0:
        pares.append(numero)

    else:
        impares.append(numero)


print("Os numeros pares sao: ", pares)
print("Os numeros impares sao: ", impares)
        