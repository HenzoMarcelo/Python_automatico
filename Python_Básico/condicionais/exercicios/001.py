# Verificador de Nota Mínima: Crie um código que pergunte ao usuário qual foi sua nota em um teste. Defina uma nota mínima para aprovação (por exemplo, 6). Use uma estrutura if para verificar se a nota do usuário é maior ou igual à nota mínima. Se for, exiba a mensagem "Você atingiu a nota mínima!".

nota_usuario = float(input("Qual foi sua nota no teste? "))
nota_minima = 5

if nota_usuario >= nota_minima:
    print("Você atingiu a nota mínima!")
if nota_usuario < nota_minima:
    print("Infelizmente você não atingiu a nota mínima.")