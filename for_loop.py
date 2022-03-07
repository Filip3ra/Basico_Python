
# vamos rodar dez posições, mas indo de 0 até 9 e não até 10
for x in range(0, 10):
    print(x, ' ', end="")

# o print sozinho já tem \n
print('\n')

# se o 'end' estiver vazio ele printa um ao lado do outro
# se o 'end' estiver com um '\n' ele printa um após o outro

grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']

# por padrão o print já vem com '\n'
for y in grocery_list:
    print(y)

# posso usar o x novamente sem problemas
for x in [2, 4, 5, 6, 8, 10]:
    print(x)

# criação de matriz e como percorrer
# aspas duplas sem espaço no meio já é um espaço
num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]
for x in range(0, 3):
    print()
    for y in range(0, 3):
        print(num_list[x][y], '', end="")

# usando while
while inp != 0:
    inp = int(input())
    print(inp)

