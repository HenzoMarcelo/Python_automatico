from datetime import datetime, timedelta

dia_final = datetime(datetime.now().year, 12, 31)
dia_atual = datetime.now()
print(dia_final.strftime(f'Faltam {(dia_final - dia_atual).days} dias para %d do mês %m de %Y'))