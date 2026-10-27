from datetime import datetime
hora_atual = datetime.now().hour
print(f'São {hora_atual} horas')
if hora_atual < 12:
    print('Bom dia!')
elif hora_atual < 18:
    print("Boa tarde!")
else:
    print("Boa noite!")