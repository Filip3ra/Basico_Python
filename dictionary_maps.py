"""
Dicionários funcionam como uma chave associada a um valor.
No exemplo abaixo tenho uma lista de super-vilões, de modo que
seu nome de vilão está associado com sua identidade secreta.

'Captain Cold' está associado com a identidade 'Leonard Snart',
logo, temos a chave associada com seu valor.

"""

super_villains = {'Fiddler': 'Isaac Bowin',
                  'Captain Cold': 'Leonard Snart',
                  'Pied Piper': 'Thomas Peterson',
                  'Mirror Master': 'Sam sam'}

# printa um valor específico
print(super_villains['Captain Cold'])

# deleta um valor específico usando sua chave
del super_villains['Pied Piper']
print(super_villains)

# altera um valor específico
super_villains['Mirror Master'] = 'Hartley Rathaway'
print(super_villains)

# printar o tamanho
print(len(super_villains))

print(super_villains.get("Mirror Master"))

print(super_villains.keys())

print(super_villains.values())
