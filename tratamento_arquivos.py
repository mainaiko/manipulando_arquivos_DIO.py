"""
tratar erros é uma parte importante da manipulaçao de arquivos. Python oferece uma variedade
de exceçoes que nos permitem lidar com erros comuns

filenotfounderror:
lançada quando o arquivo que esta sendo aberto nao pode ser encontrado no
diretorio especificado

permissionerrror:
lançada quando ocorre uma tentativa de abrir um arquivo sem permissoes adequadas
para leitura ou gravaçao

IOerror:
lançada quando ocorre um erro geral de E/s (entrada e saida) ao trabalhar com o arquivo
como problemas de permissao, falta de espaço no disco, entre outros

unicodedecodeerror:
lançada quando ocorre um erro ao tentar decodificar os dados de um arquivo de texto
usando uma codificaçao inadequada

UnicodeEncodeError:
lançada quando ocorre um erro ao tentar codificar dados em uma determinada codificaçao ao gravar em um arquivo
de texto

IsADirectoryError:
lançada quando é feita uma tentativa de abrir um diretorio em vez de um arquivo de texto

"""
from pathlib import Path


try:
    arquivo = open("meu_arquivo.py")
except FileNotFoundError as exc:
    print ("Arquivo nao encontrado")
    print (exc)

ROOT_PATH = Path(__file__).parent

try:
    arquivo = open(ROOT_PATH/"meu_diretorio")
except IsADirectoryError as exc:
    print (f"Nao foi possivel abrir o arquivo: {exc}")





