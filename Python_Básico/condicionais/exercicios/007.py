# Peça para o usuário digitar um meio de transporte. Mostre uma mensagem conforme a entrada:

# "carro" → "Veículo terrestre"

# "bicicleta" → "Transporte sustentável"

# "avião" ou "helicóptero" → "Transporte aéreo"

# Qualquer outro → "Transporte desconhecido"

veiculo = input("Digite o seu transporte aqui: ")
match veiculo:
    case "carro":
        print("Veículo terrestre")
    case "bicicleta":
        print("Transporte sustentável")
    case "avião" | "helicóptero":
        print("Transporte aéreo")
    case _: 
        print("Transporte desconhecido")