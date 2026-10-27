# Peça ao usuário que vá digitando valores para guardar no cofrinho (em reais).
# Quando o usuário digitar 0, o programa para e mostra o total economizado.

# moeda = ''
# cofrinho = 0
# while moeda != 0:
#     moeda = float(input("Quanto deseja guardar no cofrinho? "))
#     cofrinho+=moeda
# print(f'O total economizado foi um valor de R$ {cofrinho:.2f} reais')

cofrinho = 0

while True:
    moeda = float(input("Valor a guardar: "))
    if moeda == 0:
        break
    cofrinho+=moeda
print(f"Suas economias resultam num total de: R${cofrinho:.2f} reais")