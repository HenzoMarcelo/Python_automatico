# Crie uma função chamada verificar_par(numero) que retorna:

# "Par" se o número for par

# "Ímpar" se for ímpar

# Peça um número ao usuário com input(), chame a função e mostre o resultado.

N = int(input('Digite um número inteiro: '))

def verificar_par(numero):
    if numero % 2 == 0:
        numero = 'Par'
    else:
        numero = 'Ímpar'
    return numero

print(f"O número que você digitou é {verificar_par(N)}!")