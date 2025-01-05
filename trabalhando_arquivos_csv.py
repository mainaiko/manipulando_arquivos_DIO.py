"""
Arquivos CSV, formato de arquivo amplamente utilizado para armazenar dados tabulares.
CSV é a sigla para 'comma separated values' ou 'valores separados por virgula'
python fornece um modulo chamado 'csv' para lidar com esses arquivos
"""

import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open (ROOT_PATH / 'exemple.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print (row)
except IOError as exc:
    print (f"erro {exc}")

# exemplo de escrita

# with open('exemple.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["nome", "idade"])
#     writer.writerow(["Aiko", 23])
#     writer.writerow(["Kamille", 22])

"""
praticas recomendadas
Usar csv.reader e csv.writer para manipular arquivos csv.
Fazer o tratamento correto das exceçoes
Ao gravar arquivos CSV definir o argumento newline = '' no metodo open
"""
try:
    with open (ROOT_PATH / 'exemple.csv', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row ["nome"], row ["idade"]) # ele identifica pelo cabeçalho 
except IOError as exc:
    print (f"erro {exc}")


