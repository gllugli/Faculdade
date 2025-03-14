class Bateria:
    def __init__(self, voltagem, capacidade):
        self.voltagem = voltagem
        self.capacidade = capacidade 

    def status(self):
        return 'Voltagem: ', self.voltagem, '| Capacidade: ', self.capacidade

class Motor:
    def __init__(self, potencia, tensao):
        self.potencia = potencia
        self.tensao = tensao

    def status(self):
        return 'Potência: ', self.potencia, '| Tensão: ', self.tensao    
