# Usando loops, peça 5 números ao usuário (com input()), some todos e mostre o resultado.

resultado = 0

# for n in range(5):
#     numero = int(input("Digite um número: "))
#     resultado+=numero
# print(resultado)

contador = 0

while contador != 5:
    numero = int(input("Digite um número: "))
    resultado+=numero
    contador+=1
print(resultado)

# FEITO DE DOIS MODOS DIFERENTES(COM OS DOIS TIPOS DE LOOPS, WHILE E FOR.)