class Tarefa:
    def __init__(self, descricao, concluida=False):
        self.descricao= descricao
        self.concluida= concluida
    
    def marcar_concluida(self):
        self.concluida=True
    
compras = Tarefa("Comprar arroz e feijao")

print(f"Estado inicial: {compras.descricao} | {compras.concluida}")

compras.marcar_concluida()

print(f"Estado final: {compras.descricao} | {compras.concluida}")