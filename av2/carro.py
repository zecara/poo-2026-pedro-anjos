from veiculo import Veiculo


class Carro(Veiculo):
    def __init__(self, modelo, placa, valor_diaria, portas):
        super().__init__(modelo, placa, valor_diaria)
        self.__portas = None
        self.portas = portas

    @property
    def portas(self):
        return self.__portas

    @portas.setter
    def portas(self, valor):
        try:
            p = int(valor)
        except Exception:
            raise ValueError('portas deve ser um número inteiro maior que 0')
        if p <= 0:
            raise ValueError('portas deve ser maior que 0')
        self.__portas = p

    def calcular_aluguel(self, dias):
        base = super().calcular_aluguel(dias)
        return base + 50.0
