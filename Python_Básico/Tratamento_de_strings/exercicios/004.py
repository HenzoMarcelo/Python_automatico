# Arrumando o texto
# Dada uma variável frase = "    @prendendo @ progr@m@r   "  com espaços nas pontas e letras bagunçadas, o programa deve:

# Remover espaços do início/fim

# Trocar todas as letras "@" por "a"

# Colocar a primeira letra de cada palavra em maiúsculo


frase = "    @prendendo @ progr@m@r    "

# frase = frase.strip()
# frase = frase.replace('@', 'a')
# frase = frase.title()

# OU MAIS SIMPLES:

frase = frase.strip().replace('@', 'a').title()

print(frase)

