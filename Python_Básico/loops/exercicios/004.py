# Crie um sistema de votação onde o usuário escolhe entre:

# 1."Pizza"

# 2."Hambúrguer"

# 3."Sair"

# Enquanto ele não digitar "3", continue perguntando

# No final, mostre quantos votos cada item recebeu

# print("Visualize os valores numéricos e a que se referem:\n1. Pizza\n2. Hamburguer\n3. Sair")

# voto = ''
# lista_de_votos = []
# while voto != '3':
#     voto = input("Digite um voto ou aperte 3 para sair: ")
#     lista_de_votos.append(voto)

# lista_de_votos.remove('3')

# print(f'Quantidade de votos para Pizza: {lista_de_votos.count('1')}')
# print(f'Quantidade de votos para Hambúrguer: {lista_de_votos.count('2')}')


pizza = 0
hamburguer = 0

while True:
    voto = input("Voto:\n1. Pizza;\n2. Hambúrguer;\n3 >> sair.\nDigite aqui: ")
    match voto:
        case '1':
            pizza+=1
        case '2':
            hamburguer+=1
        case '3':
            break
        case _:
            print('Opção inválida.')
print(f"Quantidade de votos para pizza: {pizza}")
print(f"Quantidade de votos para hambúrguer: {hamburguer}")


