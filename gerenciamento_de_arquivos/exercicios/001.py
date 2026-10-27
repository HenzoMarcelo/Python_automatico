from pathlib import Path

pastas = Path("minhas_pastas/dados/entrada")
pastas1 = Path("minhas_pastas/dados/saida")
pastas2 = Path("minhas_pastas/relatorios")
pastas.mkdir(exist_ok=True, parents=True)
pastas1.mkdir(exist_ok=True, parents=True)
pastas2.mkdir(exist_ok=True, parents=True)