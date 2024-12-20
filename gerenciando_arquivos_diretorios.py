"""
Python tambem oferece funçoes para gerenciar arquivos e diretorios
podemos criar, renomear e excluir arquivos e diretorios
usando os modulos:
"os"
e
"shutil"
"""
import os
import shutil
from pathlib import Path


#criar diretorio
# os.mkdir("exemplo")
#dessa maneira vai ser criado na raiz do projeto
ROOT_PATH = Path(__file__).parent
# os.mkdir(ROOT_PATH / "novo_diretorio")
#dessa forma ira ser criado no diretorio em q estou

#renomear um arquivo
# arquivo = open(ROOT_PATH / "novo.txt", "w")
# arquivo.close()

# os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt")

#removendo um arquivo
# os.remove(ROOT_PATH/"alterado.txt")

#movendo um arquivo
# shutil.move(ROOT_PATH/"novo.txt", ROOT_PATH/"novo_diretorio"/"novo.txt")


