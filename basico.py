import random
import sys
import os

print("Hello World")

# comentário

'''
multiline 
comment
'''

# variáveis não precisam de um tipo definido
name = "Filipi"
print(name)
num = 15

print("5 + 2 =", 5 + 2)
print("5 - 2 =", 5 - 2)
print("5 * 2 =", 5 * 2)
print("5 / 2 =", 5 / 2)
print("5 % 2 =", 5 % 2)
print("5 ** 2 =", 5 ** 2)
print("5 // 2 =", 5 // 2)

# ordem de operações importa
print("1+2-3*2 = ", 1 + 2 - 3 * 2)
print("(1+2-3)*2 = ", (1 + 2 - 3) * 2)

# \" coloca aspas no print
quote = "\"Lembre-se sempre de que você é único!\"\n"

# aparentemente se você quebrar a linha ele entende como um \n
multi_line_quote = '''igual a
todo mundo\n'''

# uma forma de juntar duas strings
new_string = quote + multi_line_quote

print(quote, multi_line_quote, new_string)

# outra forma de printar strings
print("%s %s %s" % ('I like the quote', quote, multi_line_quote))

# forma de printar sem quebra de linha
print("I don't like ", end="")
print("newlines")

# printar várias quebras de linha
print('>\n' * 5)

