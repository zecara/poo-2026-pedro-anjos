from veiculo import Veiculo


class Moto(Veiculo):
    def __init__(self, modelo, placa, valor_diaria, cilindradas):
        super().__init__(modelo, placa, valor_diaria)
        self.__cilindradas = None
        self.cilindradas = cilindradas

    @property
    def cilindradas(self):
        return self.__cilindradas

    @cilindradas.setter
    def cilindradas(self, valor):
        try:
            c = int(valor)
        except Exception:
            raise ValueError('cilindradas deve ser um número inteiro maior que 0')
        if c <= 0:
            raise ValueError('cilindradas deve ser maior que 0')
        self.__cilindradas = c

    def calcular_aluguel(self, dias):
        base = super().calcular_aluguel(dias)
        return base * 0.9
