from carro import Carro
from moto import Moto


def criar_veiculos():
    veiculos = []
    try:
        veiculos.append(Carro('Carro AV2 A', 'AV2-0001', 120.0, 4))
        veiculos.append(Carro('Carro AV2 B', 'AV2-0002', 150.0, 4))
        veiculos.append(Moto('Moto AV2 A', 'AV2-0003', 80.0, 125))
        veiculos.append(Moto('Moto AV2 B', 'AV2-0004', 100.0, 250))
    except ValueError as e:
        print('Erro ao criar veículos de exemplo:', e)
    return veiculos


def listar_veiculos(veiculos):
    if not veiculos:
        print('Nenhum veículo disponível.')
        return
    for idx, v in enumerate(veiculos, start=1):
        try:
            print(f"{idx} - Modelo: {v.modelo} | Placa: {v.placa} | Diária: R$ {v.valor_diaria:.2f}")
        except Exception:
            print(f"{idx} - veículo com dados inválidos")


def escolher_veiculo(veiculos):
    listar_veiculos(veiculos)
    try:
        escolha = int(input('Escolha o número do veículo: '))
    except ValueError:
        raise ValueError('Escolha inválida: digite um número')
    if escolha < 1 or escolha > len(veiculos):
        raise IndexError('Veículo inexistente')
    return veiculos[escolha - 1]


def calcular_fluxo(veiculos):
    if not veiculos:
        print('Nenhum veículo para calcular aluguel.')
        return
    try:
        veiculo = escolher_veiculo(veiculos)
        dias_in = input('Quantidade de dias: ')
        try:
            dias = int(dias_in)
        except ValueError:
            raise ValueError('dias deve ser um número inteiro')
        valor = veiculo.calcular_aluguel(dias)
    except (ValueError, IndexError) as e:
        print('Erro:', e)
    else:
        print(f'Valor total do aluguel: R$ {valor:.2f}')
    finally:
        print('Operação finalizada. Retornando ao menu.')


def menu():
    veiculos = criar_veiculos()
    while True:
        try:
            print('\n--- Locadora AV2 ---')
            print('1 - Listar veículos')
            print('2 - Calcular aluguel')
            print('3 - Sair')
            opc = input('Escolha uma opção: ')
            try:
                opc_int = int(opc)
            except ValueError:
                print('Digite apenas números.')
                continue

            if opc_int == 1:
                listar_veiculos(veiculos)
            elif opc_int == 2:
                calcular_fluxo(veiculos)
            elif opc_int == 3:
                print('Saindo...')
                break
            else:
                print('Opção inexistente.')
        except Exception as e:
            print('Ocorreu um erro:', e)
        finally:
            pass


if __name__ == '__main__':
    menu()
