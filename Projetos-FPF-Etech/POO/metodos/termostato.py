class Termostato:
    def __init__(self, temperatura=20):
        self.temperatura= temperatura
    
    def aumentar(self,graus):
        self.temperatura= self.temperatura + graus
    
    def diminuir(self,graus):
        self.temperatura= self.temperatura - graus

meutermostato= Termostato()
print(f"A temperatura inicial é: {meutermostato.temperatura} ")

meutermostato.aumentar(3)
print(f"A temperatura aumentada fica: {meutermostato.temperatura}")

meutermostato.diminuir(5)
print(f"A temperatura diminuida fica: {meutermostato.temperatura}")
