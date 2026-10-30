from pathlib import Path
import shutil


shutil.unpack_archive("exercicios/003/arquivos_secretos.zip", "exercicios/003/extraido")

for arquivo in Path("exercicios/003/extraido").iterdir():
    if arquivo.is_file():
        print(arquivo)