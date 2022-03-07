import random

# gera um número aleatório de 0 até 100, mas sem incluir o 100, ou seja, de 0 a 99
random_num = random.randrange(0, 100)

# enquanto não tiver satisfeito a condição vai printar o número e gerar outro
while random_num != 99:
    print(random_num)
    random_num = random.randrange(0, 100)

print("-----------------------------------")

# uma forma de incrementar e testar os valores
i = 0
while i <= 20:
    if i % 2 == 0:
        print(i)
    elif i == 9:
        break
    else:
        i += 1  # i = i + 1
        continue  # ignora o restante abaixo e pula la pro começo do while
    i += 1

# os valores indentados especificam quem está no loop
print("Fora do loop")
