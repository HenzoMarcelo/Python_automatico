# Verificação de Diferença: Crie um código que peça para o usuário inserir dois nomes. Depois verifique se os dois nomes são diferentes. Se forem, exiba "Os nomes digitados são diferentes."

nome_1 = input("Digite o primeiro nome: ")
nome_2 = input("Digite o outro nome: ")

if nome_1 != nome_2:
    print("Os nomes digitados são diferentes.")
if nome_1 == nome_2:
    print("Os nome digitados são exatamente iguais, parabéns!")