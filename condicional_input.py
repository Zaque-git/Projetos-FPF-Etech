idade= int(input(" Digite sua idade: "))


if idade>=18:
    CNH = str(input("Voce tem CNH?: {SIM / NAO}")).lower().strip()
    confirma=(CNH=="sim")

    if confirma:
        print("Voce é maior de idade e tem CNH. Pode dirigir")

    else:
        print("Voce é maior de idade e nao tem CNH. Nao pode dirigir")


else:
    print(f"Voce tem {idade} anos. É menor de idade e nao pode dirigir")
