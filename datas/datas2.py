from datetime import datetime, timedelta

# hoje = datetime.now()
# um_dia = timedelta(days=1)
# amanha = hoje + um_dia
# ontem = hoje - um_dia
# print(ontem)

# prazo = datetime(2026, 5, 26)
# hoje = datetime.now()

# if hoje > prazo:
#     print("Prazo vencido.")
# else:
#     print("Ainda há tempo")

agora = datetime.now()
futuro = datetime(2027, 9, 23)
dias_restantes = futuro - agora
print(dias_restantes.days)
