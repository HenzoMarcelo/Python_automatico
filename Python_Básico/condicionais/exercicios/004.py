# Peça ao usuário uma nota de 0 a 10 para um filme. Classifique a avaliação assim:

# Nota 9 ou 10: "Excelente!"

# Nota 7 ou 8: "Muito bom"

# Nota 5 ou 6: "Regular"

# Menor que 5: "Ruim"

nota_filme = int(input("Digite a nota direcionada ao filme: "))

if nota_filme == 9 or nota_filme == 10:
    print("Excelente!")
elif nota_filme == 7 or nota_filme == 8:
    print("Muito bom")
elif nota_filme == 5 or nota_filme == 6:
    print("Regular")
else:
    print("Ruim")