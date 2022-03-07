"""
    Não ficou muito claro ainda o que é uma tupla.
    Uma tupla é um vetor de informação que não pode sofrer alterações.
"""

# tuple não pode sofrer alterações dos seus dados visto que foram criados
pi_tuple = (3, 1, 4, 5, 9)

# transforma numa lista ou vice-versa
new_tuple = list(pi_tuple)
new_list = tuple(new_tuple)

# obter informações básicas de uma tupla
len(tuple)
min(tuple)
max(tuple)