class Interruptor:
    def __init__(self, ligada=False):
        self.ligada= ligada

    def alternar(self):
        if self.ligada==False:
            self.ligada=True
        else: 
            self.ligada=False
        

interruptor= Interruptor()

print(f"Estado inicial: {interruptor.ligada}")

interruptor.alternar()

print(f"Estado final:{interruptor.ligada}")