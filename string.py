

long_string = "I'll Catch You if You Fall - The Floor"

# printar os 4 primeiros caracteres
print(long_string[0:4])

# printar os últimos 5 caracteres
print(long_string[-5:])

# printar tudo exceto os últimos 5 caracteres
print(long_string[:-5])

# printar apenas os primeiros 5 caracteres
print(long_string[:5])

# concatenar string
print(long_string[:4] + " be there for you!")

# outra forma de lidar com formatação, lembrando dos parenteses internos!
print("%c is my %s letter and my numer %d numer is %.5f" % ('X', 'favorite', 1, .14))

# primeiro caractere fica caixa alta e os outro em caixa baixa, não altera a string original
print(long_string.capitalize())

# retorna o menor índice onde a substring especificada está na string original
print(long_string.find("Floor"))
print(long_string[33:])

# outra forma legal de fazer o mesmo acima é usando variáveis
posicao = long_string.find("Catch")
print(long_string[posicao:])

# se a string for alfabética retorna true
print(long_string.isalpha())

# se a string for alfanumérica retorna true
print(long_string.isalnum())

# tamanho da string
print(len(long_string))

# troca uma cópia com a substring substituída por outra, mas não substitui a string original
print(long_string.replace("Floor", "Ground"))
print(long_string)

# ?
print(long_string.strip())

# transforma a string numa lista
quote_list = long_string.split()
print(quote_list)
