"""
Ao manipular arquivos em python existem algumas boas praticas que podemos seguir, 
vamos abordar as principais

Bloco with
use o gerenciamento de contexto (context manager) com a declaraçao 'with'.
o gerenciamento de contexto permite trabalhar com arquivos de forma segura, garantindo que eles sejam fechados
corretamente, mesmo em caso de exceçoes
"""
from pathlib import Path

ROOT_PATCH = Path(__file__).parent

with open(ROOT_PATCH / "texto.txt", "r") as texto:
    print ("trabalhando com o arquivo")

# print (texto.read())


"""
Verificar se o arquivo foi aberto com sucesso
É recomendado verificar se o arquivo foi aberto corretamente antes de executar operaçoes
de leitura ou gravaçao nele
"""
try:
    with open(ROOT_PATCH / "texto.txt", "r") as texto:
        print ("teste")
except IOError:
    print ("erro ao abrir o arquivo")


"""
Use a codificaçao correta
Certifique-se de usar codificaçao correta ao ler ou gravar arquivos de texto. O argumento
'encoding' da funçao 'open()' permite especificar a codificaçao
"""
try:
    with open(ROOT_PATCH / "arquivo-utf-8.txt", encoding="utf-8") as arquivo:
        arquivo.write("aprendendo a manipular aquivos usando python.")
except IOError as exc:
    print (f"Erro ao abrir o arquivo {exc}")


    


