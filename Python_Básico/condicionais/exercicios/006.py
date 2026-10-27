# Crie um menu com 3 opções:

# 1. Pizza

# 2. Sushi

# 3. Salada

# O usuário digita um número. O programa mostra o prato escolhido. Se digitar qualquer outro número, exiba: "Opção inválid."

opcao = int(input("Digite 1 >> (pizza)  2 >> (Sushi)  3 >> (Salada): "))

match opcao:
    case 1:
        print("O prato escolhido foi pizza!")
    case 2:
        print("O prato escolhido foi Sushi!")
    case 3:
        print("O prato escolhido foi Salada!")
    case _:
        print("Opção de prato inválida")

