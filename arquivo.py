import os

# crio um arquivo para escrita
test_file = open("test.txt", "wb")

# apresenta o modo que o arquivo se encontra, nesse caso pra escrita
print(test_file.mode)

# obtenho o nome do arquivo
print(test_file.name)

# escrevo algo no arquivo
test_file.write(bytes("Write me to the file\n", 'UTF-8'))

# fecha arquivo
test_file.close()

# abre arquivo para ler e escrever, ou seja, usamos "r+"
test_file = open("test.txt", "r+")

# lendo e printando na tela o conteúdo do arquivo
text_in_file = test_file.read()
print(text_in_file)
test_file.close()

os.remove("test.txt")   # tem que fechar o arquivo primeiro


