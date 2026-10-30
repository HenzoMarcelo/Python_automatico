from pathlib import Path
import shutil

Path("exercicios/001/imagens").mkdir()
Path("exercicios/001/imagens/Ninja300").touch()
Path("exercicios/001/imagens/Tatsumi").touch()

imagens = Path("exercicios/001/imagens")

ninja300 = Path("exercicios/001/imagens/Ninja300")
tatsumi = Path("exercicios/001/imagens/Tatsumi")

resposta = input("0/1")

if resposta == "1":
    Path("exercicios/001/backup_imagens/").mkdir()
    backup_imagens = Path("exercicios/001/backup_imagens/")

    for arquivo in imagens.iterdir():
        if arquivo.is_file():
            shutil.move(arquivo, backup_imagens/arquivo.name)
else:
    print("ok")

try:
    while True:
        deletar = input("Deletar? S/N")

        if deletar == "S":
            shutil.rmtree(backup_imagens)
            shutil.rmtree(imagens)
            break
        else: 
            continue
except WindowsError:
    print("ops, ocorreu um erro ao deletar...")
    