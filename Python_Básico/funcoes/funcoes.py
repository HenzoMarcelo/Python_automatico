# def saudacao():
#     print("Olá, seja bem vindo!")

# # def saudacao(nome):
# #     print(f"Olá, {nome} seja bem vindo!")

# # saudacao('Henzo')

# def somar(numero1, numero2):
#     resultado = numero1 + numero2
#     print(f'O resultado da soma entre {numero1} e {numero2} é: {resultado}')

# somar(6, 8)

# def somar(numero1, numero2):
#     resultado = numero1 + numero2
#     return resultado

# print(somar(3, 5))

def calcular_desconto(preco, percentual):
    desconto = preco * (percentual/100)
    preco_final = preco - desconto
    return preco_final

print(calcular_desconto(200, 100))