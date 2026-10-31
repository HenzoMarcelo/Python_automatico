import time
while True:

    with open("exercicios/003/acesso.log", "r", encoding='utf-8') as acesso_logs:

            pesquisa = input("O QUE VOCE QUER PESQUISAR?\nERROR\nWARNING\nINFO\n\n")

            if pesquisa == "fechar":
                break

            for linha in acesso_logs.readlines():
                if pesquisa.upper() in linha.upper():
                    time.sleep(0.2)
                    print(linha)
                    
                    