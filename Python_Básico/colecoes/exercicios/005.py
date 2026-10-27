# Peça para o usuário digitar nome e idade. Guarde esses dados em um dicionário chamado usuario.
# Depois, verifique se a idade é maior ou igual a 18:

# Se sim, imprima: "Acesso liberado para {nome}"

# # Se não, imprima: "Acesso negado para {nome}"

# nome = input("Digite seu nome: ")
# idade = int(input("Digite aqui sua idade: "))

# usuario = {
#     "nome": nome,
#     "idade": idade
# }

# OU

usuario = {
    'nome': input("Digite seu nome: "),
    'idade': int(input("Digite a sua idade: "))
}

if usuario['idade'] >= 18:
    print(f"Acesso liberado para {usuario['nome']}")
else:
    print(f"Acesso negado para {usuario['nome']}")