from datetime import datetime
#arquivo_relatorio = Path("exercicios/001/relatorio.txt").touch()

with open("exercicios/001/relatorio.txt", 'w', encoding='utf-8') as relatorio:
    relatorio.write("Este é meu relatório\n")
with open("exercicios/001/relatorio.txt", "a", encoding='utf-8') as relatorio:
    relatorio.write(f"data: {datetime.now().strftime("%d/%m/%Y")}\nhora: {datetime.now().strftime("%H:%M")}")