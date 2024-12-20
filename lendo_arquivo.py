# lendo um arquivo

file = open("texto.txt", "r")
# print (file.readline())

"""
O metodo 'readline()' le uma linha por vez, enquanto o 'readlines()' retorna uma lista onde cada
elemento é uma linha do arquivo
"""
for line in file.readlines():
    print (line)

file.close()