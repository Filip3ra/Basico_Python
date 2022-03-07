import sys


# definindo uma função
def addNumbers(fNum, lNum):
    sumNum = fNum + lNum  # sumNum só existe aqui dentro, está fora do escopo
    return sumNum


print(addNumbers(1, 4))
'''
# lendo dados do teclado
print("Whats your name")

name = sys.stdin.readline()

print("Hello", name)
'''

while inp != 0:
    inp = int(input('Informe um número: '))  # input trabalha bem com números, 'sys.stdin.readline()' não
    print(inp)

while inp != 0:
    inp = sys.stdin.readline()  # não sai do ‘loop’, pois a entrada é interpretada de outra forma
    # inp = int(sys.stdin.readline()) <-- con casting funciona
    print(inp)