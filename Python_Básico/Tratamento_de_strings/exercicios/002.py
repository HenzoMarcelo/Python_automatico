# Peça ao usuário uma frase e dois números: início e fim. Mostre o fatiamento da frase entre esses índices.

frase = input("Digite uma frase: ")
numero_1 = int(input("Ínicio do fatiamento: "))
numero_2 = int(input("Final do fatiamento: "))

print(frase[numero_1 : numero_2])