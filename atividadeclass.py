class Dispositivo:
    rede_padrao= "Rede Doméstica V.2"
    total_ativos= 0

    def __init__(self,id_serie, localizacao):
        self.id_serie=id_serie
        self.localizacao=localizacao

        self.status= "Desconectado"
        Dispositivo.total_ativos += 1

id_input=int(input("Digite o ID de Serie do novo dispositivo: "))

local_input=int(input("Digite a o localizacao do dispositivo: "))

dispositivo_usuario=Dispositivo(id_input,local_input)

print(f"ID de Serie: {dispositivo_usuario.id_serie}")
print(f"Localizacao: {dispositivo_usuario.localizacao}")
print(f"Status: {dispositivo_usuario.status}")