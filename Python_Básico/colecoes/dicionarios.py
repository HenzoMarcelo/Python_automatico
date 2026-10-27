pessoa = {
    "nome":"Júlio",
    "idade":25,
    "cidade":'São Paulo',
    "profissoes": ['Programador', 'Designer', 'Pintor']
}
# pessoa["idade"] = 26
# print(pessoa["idade"])
# del pessoa["cidade"]
# print(pessoa["profissoes"][1])

# valores = list(pessoa.values())
# print(valores)

# print(pessoa.items())

# print(pessoa.get("telefone", "Não existe"))

# item_removido = pessoa.pop("profissoes")
# print(f"Item removido: {item_removido}")
# print(pessoa)

produto = {
    "nome": "Notebook",
    "preco": 3500,
    "estoque": 12
}

# print(f"Ainda restam {produto['estoque']} unidades do produto {produto['nome']}")

playlists = { 
    'Rock': ['Slipknot', 'Andromeda', 'Asking-Alexandria'],
    'Sertanejo': ['Asas-Morenas', 'Devinho novais', 'Calcinha-Preta'],
    'luz': ['Somewhere-only-we-know','My love, mine, all mine']
 }

nome_playlist = input("Digite o nome da playlist: ")
index_musica = int(input("Dê a coordenada da música: "))

# print(f"{playlists.get(nome_playlist, 'A playlist digitada não existe')}\n{playlists.get(index_musica, 'A coordenada digitada não existe')}")

print(f'{playlists[nome_playlist][index_musica]}')

# print(pessoa.items())