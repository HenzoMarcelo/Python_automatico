from pathlib import Path
import shutil

Path("exercicios/002/relatorios").mkdir()
Path("exercicios/002/relatorios/relatorio.txt").touch()

arquivo_relatorio = Path("exercicios/002/relatorios/relatorio.txt")

Path("exercicios/002/relatorios_antigos").mkdir()
backup_relatorios = Path("exercicios/002/relatorios_antigos")

if arquivo_relatorio.exists():
   shutil.move(arquivo_relatorio, backup_relatorios) 