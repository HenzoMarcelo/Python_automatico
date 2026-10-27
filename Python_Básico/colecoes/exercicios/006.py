# Crie um sistema de login com dois dicionários: um que guarda as credenciais corretas, e outro dicionário que guarde as informações inseridas pelo usuário. Peça ao usuário para digitar o usuário e senha, e verifique se está correto de acordo com o primeiro dicionário.

# Se o usuário e a senha estão corretos → "Login bem-sucedido"

# Senão → "Usuário ou senha incorretos"

# usuario_digitado = input("Digite o seu usuário: ")
# senha_digitada = str(input("Digite sua senha: "))

# dados_recebidos = {
#     "usuario": usuario_digitado,
#     "senha": senha_digitada
# }

# OU

credenciais = {
    "usuario": "LainRyzen",
    "senha": "PugLaio2"
}

dados_recebidos = {
    'usuario': input("Digite o seu usuario: "),
    'senha': str(input("Digite sua senha: "))
}


if dados_recebidos['usuario'] == credenciais['usuario'] and dados_recebidos['senha'] == credenciais['senha']:
    print("Login bem-sucedido")
else:
    print("Usuário ou senha incorretos")