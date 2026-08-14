"""
aula04_sobrescrita

Implementa a Superclasse Funcionario e as subclasses Gerente e Vendedor
conforme as regras do negócio:

- Funcionario: atributos `nome`, `salario_base`; `calcular_bonus()` = 5% do salario_base
- Gerente: sobrescreve `calcular_bonus()` somando R$ 1.000,00 ao bônus padrão
- Vendedor: possui `total_vendas` e sobrescreve `calcular_bonus()` retornando 10% de total_vendas
"""

class Funcionario:
    def __init__(self, nome: str, salario_base: float):
        self.nome = nome
        self.salario_base = float(salario_base)

    def calcular_bonus(self) -> float:
        """Retorna 5% do salario_base como bônus padrão."""
        return 0.05 * self.salario_base


class Gerente(Funcionario):
    def calcular_bonus(self) -> float:
        """Bônus padrão + R$ 1.000,00 fixos."""
        return super().calcular_bonus() + 1000.0


class Vendedor(Funcionario):
    def __init__(self, nome: str, salario_base: float, total_vendas: float = 0.0):
        super().__init__(nome, salario_base)
        self.total_vendas = float(total_vendas)

    def calcular_bonus(self) -> float:
        """Ignora o bônus padrão; retorna 10% do total_vendas."""
        return 0.10 * self.total_vendas


if __name__ == "__main__":
    f = Funcionario("Ana", 3000.0)
    g = Gerente("Carlos", 8000.0)
    v = Vendedor("Maria", 2500.0, total_vendas=20000.0)

    print(f"{f.nome}: R$ {f.calcular_bonus():.2f}")
    print(f"{g.nome}: R$ {g.calcular_bonus():.2f}")
    print(f"{v.nome}: R$ {v.calcular_bonus():.2f}")
