from random import randint

numero_aleatorio = randint(1,10)
numero_escolhido = ''
tentativas = 0 

while numero_escolhido != numero_aleatorio:
    numero_escolhido = int(input("chute um numero: "))
    tentativas+=1
    if numero_escolhido > numero_aleatorio:
        print("Muito Alto!")
    elif numero_escolhido < numero_aleatorio:
        print("Muito Baixo!")
    else:
        print("Acertou!!")

print(f"Você tentou: {tentativas} vezes.")


#OU

while True:
    numero_escolhido = int(input("Digite um número: "))
    tentativas+=1
    if numero_escolhido == numero_aleatorio:
        print(f'Parabéns! Você acertou o número!\nTentativas: {tentativas}')
        break