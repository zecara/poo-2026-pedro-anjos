from abc import ABC, abstractmethod


class Veiculo(ABC):
    def __init__(self, modelo):
        self.modelo = modelo

    @abstractmethod
    def acelerar(self):
        pass


class Carro(Veiculo):
    def acelerar(self):
        print(f"{self.modelo}: O carro acelera com potência e deixa uma trilha de fumaça.")


class Moto(Veiculo):
    def acelerar(self):
        print(f"{self.modelo}: A moto ganha velocidade com agilidade e derrapa na curva.")


class Caminhao(Veiculo):
    def acelerar(self):
        print(f"{self.modelo}: O caminhão arranca devagar, mas com muita força e peso.")


class CarroEletrico(Veiculo):
    def acelerar(self):
        print(f"{self.modelo}: O carro elétrico acelera silenciosamente com máxima eficiência.")


if __name__ == "__main__":
    pista_de_corrida = [
        Carro("Ferrari F40"),
        Moto("Yamaha R1"),
        Caminhao("Volvo FH"),
        CarroEletrico("Tesla Model S"),
    ]

    print("Simulação de Corrida\n")
    for veiculo in pista_de_corrida:
        veiculo.acelerar()
