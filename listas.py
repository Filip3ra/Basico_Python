grocery_list = ['Juice', 'Tomatoes', 'Potatoes',
                'Bananas']

print('First item', grocery_list[0])

grocery_list[0] = "Green Juice"

print('First item', grocery_list[0])

# printou um subset de itens, sem incluir o último, mas incluindo o primeiro
print(grocery_list[1:3])

# se mandar printar até uma posição que não existe, ou seja,
# uma posição maior que o tamanho do vetor, ele não da pau e
# printa até seu tamanho máximo
print(grocery_list[0:5])

# listas dentro de listas
other_events = ['Wash Car', 'Puck Up Kids', 'Cash Check']
to_do_list = [other_events, grocery_list]
print(to_do_list)

''' uma lista de listas é uma matriz, logo
       [0]           [1]             [2]              [3]
   [0] [['Wash Car',   'Puck Up Kids', 'Cash Check'], 
   [1] ['Green Juice', 'Tomatoes',     'Potatoes',   'Bananas']]
'''
# se eu mando printar [1][1] deve sair 'tomatoes'
print(to_do_list[1][1])

# se eu mando printar [0][0] deve sair 'wash car'
print(to_do_list[0][0])

# mandar printar um elemento de uma posição que não existe, da erro:
# erro: 'list index out of range'
# print(to_do_list[0][3])

# usando o comando append podemos adicionar um elemento
grocery_list.append('Onions')
print(to_do_list)

print(">\n" * 5)

# inserir em um índice específico
grocery_list.insert(1, 'Pickle')
print(grocery_list)

# remove um item
grocery_list.remove('Pickle')
print(grocery_list)

# randomiza a lista
grocery_list.sort()
print(grocery_list)

# inverte a lista
grocery_list.reverse()
print(grocery_list)

# deleta um item da lista e ela afeta outras listas
del grocery_list[4]
print(to_do_list)

# outras coisas que da pra fazer com listas
to_do_list2 = other_events + grocery_list

# printar seu tamanho
print(len(to_do_list2))
# printar o elemento máximo
print(max(to_do_list2))
# printar o elemento mínimo
print(min(to_do_list2))

''' Um ponto interessante, se as strings dentro dessas listas
    estiverem com palavras iniciadas com letras maiúsculas e
    outras em minúsculas, o resultado pode ser diferente.

    Exemplo: Se a lista for 'Wash Car', 'Pick up kids' e 'cash check'
    o max dessa lista é 'cash check' e o min é 'Pick up kids'. 
    Por outro lado, se tiver 'Wash Car', 'Puck Up Kids', 'Cash Check'
    o max é 'Wash Car' e o min é 'Cash Check'. 

    Investigar isso depois...    
'''



