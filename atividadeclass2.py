class Estrela:
    tipo_corpo= "Corpo Celeste"
    total_estrelas_catalogadas= 0

    def __init__(self, nome, massa):
        self.nome= nome
        self.massa= massa

        self.em_atividade= True
        Estrela.total_estrelas_catalogadas+=1

estrela_a = Estrela("Alpha Centauri", 1.1) 
estrela_b = Estrela("Sirius", 2.0)

print(f"O nome da estrela A :{estrela_a.nome}")
print(f"A massa da estrela A : {estrela_a.massa}")
print("-"*20)
print(f"O nome da estrela B :{estrela_b.nome}")
print(f"A massa da estrela B : {estrela_b.massa}")


