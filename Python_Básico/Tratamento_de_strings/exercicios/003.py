# Detectando palavras proibidas
# Peça ao usuário para escrever uma mensagem. Verifique se ela contém a palavra "bomba", e imprima um alerta se sim.

mensagem = input("Digite uma mensagem: ")

if 'bomba' in mensagem.lower():
    print("Palavra perigosa detectada!!")
else:
    print("Tudo limpo...")