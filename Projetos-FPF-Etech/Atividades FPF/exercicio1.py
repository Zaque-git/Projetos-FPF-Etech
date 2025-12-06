frequencia = int(input("Digite sua frequencia (EM %): "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
soma= nota1 + nota2 + nota3
media = soma / 3

if frequencia >75 and media > 7.0:
    print("Aluno Aprovado")

elif frequencia <75 or frequencia>= 75/100 and media < 7.0:
    print("Aluno Reprovado")

elif frequencia >= 75 and 5.0<media < 6.9:
    print("Aluno em recuperacao")


