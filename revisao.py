# 1. encapsulamento (classe)

class veiculo:
    def __init__(self, marca, modelo, valor_diaria):
        self.marca = marca
        self.modelo = modelo
        self.valor_diaria = valor_diaria
    def get_valor_diaria(self):
        return self.valor_diaria

    def calcular_aluguel(self, dias):
        return dias * self.valor_diaria




 # 2. herança e reuso de código (subclasse)
class carro(veiculo):
    def __init__(self, marca, modelo, valor_diaria, portas):
        super().__init__(marca, modelo, valor_diaria)
        self.portas = portas

    def calcular_aluguel(self, dias):
        # Adiciona um custo adicional de 10% para carros com 4 portas
        if self.portas == 4:
            return super().calcular_aluguel(dias) * 1.1
        return super().calcular_aluguel(dias)