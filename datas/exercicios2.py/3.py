from datetime import datetime, timedelta

intervalo = timedelta(days= 180)
data_fabricacao = input()

def data_validade(fabricacao):
    fabricacaoobj = datetime.strptime(fabricacao, '%d/%m/%Y')
    data_de_validade = fabricacaoobj + intervalo
    return data_de_validade

data_de_validade = data_validade(data_fabricacao)
dia_atual = datetime.now()
print(data_de_validade.strftime('Vence dia %d do mês %m de %Y'))

if dia_atual > data_de_validade:
    print('Este produto está vencido.')
    print(f'Venceu a {(dia_atual - data_de_validade).days} dias.')
else:
    print('O produto ainda é próprio para consumo')
    print(f'Faltam {(data_de_validade - dia_atual).days} dias para vencer.')