lista_inteiros=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

pares=[]
impares=[]
soma_pares=0
soma_impares=0

for numero in lista_inteiros:
    if numero%2==0:
        pares.append(numero)
        soma_pares += numero


    else:
        impares.append(numero)
        soma_impares += numero


print("Os numeros pares sao: ", pares)
print("Os numeros impares sao: ", impares)
print("Soma dos numeros: ", soma_pares)
print("Soma dos impares: ", soma_impares)




#QUESTAO 2:
# palavra = str(input("Digite uma palavra: ")).lower().strip()
#
#
# vogais=[]
# consoantes=[]
#
# for letras in palavra:
#     if letras==" ": # nao conta espaco
#         continue
#     if letras in "aeiou": #percorre por cada index
#         vogais.append(letras)
#
#     else:
#         consoantes.append(letras)
#
# print("As vogais sao: ", vogais)
# print("As consoantes sao: ", consoantes)


#QUESTAO 3
#
# funcionarios=[]
#
# while True:
#     nome = input("Nome do funcionário: ").strip()
#     sexo = input("Sexo [M/F]: ").strip().upper()
#     salario = float(input("Salário: "))
#
#     funcionario={       #fiz com dicionario pq quero ser back end e nunca mexi com essa parte : )
#         "nome": nome,
#         "sexo": sexo,
#         "salario": salario
#     }
#
#     funcionarios.append(funcionario)
#
#     continuar=input("Deseja continuar? [S/N]: ").strip().upper()
#     if continuar == "N":
#         break
#
# soma_m=0
# soma_f=0
# for funcionario in funcionarios:
#     if funcionario["sexo"] == "M":
#         soma_m+=funcionario["salario"]
#     else:
#         soma_f+=funcionario["salario"]
#
# print(f"A soma dos salarios dos funcionarios masculinos é: {soma_m}")
# print(f"A soma dos salarios das funcionarias femininas é: {soma_f}")
#
#
#

