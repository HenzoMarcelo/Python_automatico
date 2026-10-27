from datetime import datetime, timedelta

digitada = input("Digite a data do evento: ")

data_atual = datetime.now()
data_evento = datetime.strptime(digitada, '%d/%m/%Y')

if data_atual.date() == data_evento.date():
    print("O evento acontece hoje.")
elif data_atual > data_evento:
    print('O evento já passou.')
elif data_atual < data_evento:
    print(f'faltam {(data_evento - data_atual).days} dias para o evento.')