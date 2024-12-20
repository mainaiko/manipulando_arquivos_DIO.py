"""
podemos usar write() ou writelines() para escrever em um arquivo
lembre-se, no entando, de abrir o arquivo do modo correto
"""

file = open('texto.txt', 'w')
file.write("teste ")
file.writelines(["python ", "esta ", "facil"])

file.close()

