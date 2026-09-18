class Veiculo:
    def __init__(self, modelo, placa, valor_diaria):
        self.__modelo = None
        self.__placa = None
        self.__valor_diaria = None
        self.modelo = modelo
        self.placa = placa
        self.valor_diaria = valor_diaria

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError('modelo não pode ser vazio')
        self.__modelo = valor.strip()

    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError('placa não pode ser vazia')
        self.__placa = valor.strip()

    @property
    def valor_diaria(self):
        return self.__valor_diaria

    @valor_diaria.setter
    def valor_diaria(self, valor):
        try:
            v = float(valor)
        except Exception:
            raise ValueError('valor_diaria deve ser numérico e maior que 0')
        if v <= 0:
            raise ValueError('valor_diaria deve ser maior que 0')
        self.__valor_diaria = v

    def calcular_aluguel(self, dias):
        try:
            d = int(dias)
        except Exception:
            raise ValueError('dias deve ser um número inteiro maior que 0')
        if d <= 0:
            raise ValueError('dias deve ser maior que 0')
        return self.__valor_diaria * d
