# Seu programa deve verificar se o usuário tem direito a frete grátis. As regras são:

# O valor da compra deve ser maior ou  a 100 igual

# E o cliente precisa estar cadastrado no programa de fidelidade

# Se as duas condições forem verdadeiras, mostre: "Frete grátis aplicado!"
# Caso contrário: "Frete não disponível gratuitamente."

valor_compra = float(input())

cadastrado = input("Se está cadastrado no programa frete grátis, digite: Sim, se não, digite: Não...: ")

if valor_compra >= 100 and cadastrado == "Sim":
    print("Frete grátis aplicado")
else:
    print("Frete não disponível gratuitamente")