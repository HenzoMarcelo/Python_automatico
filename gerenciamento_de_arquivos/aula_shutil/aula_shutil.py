import shutil
from pathlib import Path
#shutil.copy2("arquivinho.txt", "backup/arquivinho_backup.txt")

#shutil.copytree("meus_arquivos", "meus_arquivos_backup", dirs_exist_ok=True)
#shutil.move("arquivo_teste.txt", "meus_arquivos")

#arquivo_teste = Path("arquivo_teste.txt")
#shutil.move(arquivo_teste, "meus_arquivos")

#shutil.move("meus_arquivos/arquivo_teste.txt", "meus_arquivos/arquivo.txt")

#shutil.rmtree("meus_arquivos_backup")

#shutil.make_archive("meus_arquivos", "zip", "meus_arquivos")

#shutil.unpack_archive("meus_arquivos.zip", "arquivos")

#arquivos = Path("arquivos")
#arquivos_backup = Path("arquivos_backup")


#shutil.copytree(arquivos, arquivos_backup)

#shutil.make_archive("arquivos", "zip", "arquivos")

#shutil.unpack_archive("arquivos.zip", "descompacto")

if Path("descompacto").exists():
    shutil.make_archive("descompacto", "zip", "descompacto")
    shutil.move("descompacto.zip", "compactado.zip")
    existe = 1

else:
    existe = 0
    print("A pasta a compactar não existe...")

if existe == 1:
    decisao = input("O que deseja fazer com o arquivo compactado?\n 2 Backup\n 1 Deletar\n 0 Nada\n\n")

    match decisao:

        case "1":
            if decisao == "1":
                if Path("compactado.zip").exists():
                    Path("compactado.zip").unlink()

        case "2":
            if decisao == "2":
                if Path("compactado.zip").exists() and Path("arquivos_backup").exists():
                    shutil.copy("compactado.zip", "arquivos_backup/compactado_backup.zip")