from datetime import datetime

# agora = datetime.now()

# print(agora.day)
# print(agora.month)
# print(agora.year)

# print(agora.hour)
# print(agora.minute)
# print(agora.second)
# print(agora.microsecond)

# aniversário = datetime(2000, 5, 20)

# print(aniversário.day)

agora = datetime.now()
print(f'Hoje é dia {agora.day} mês {agora.month} ano {agora.year}')
print(agora.strftime("Hoje é dia %d do mês %m do ano %Y"))
print(agora.strftime("Agora são %H horas e %M minutos"))

data_str = "20/04/2025"
data_convertida = datetime.strptime(data_str, '%d/%m/%Y')
print(data_convertida)

print(datetime.now().strftime('Agora são %H horas e %M minutos'))

print(datetime(2024,5,6))