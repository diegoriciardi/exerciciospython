"""
6. Programa para criar e exibir uma matriz Escreva um programa que leia dois números 
inteiros Lin e Col, que representam, respectivamente, a quantidade de linhas e colunas 
em uma matriz. Utilizando listas aninhadas, crie uma representação para essa matriz, 
utilizando a função randint para gerar números para cada posição da matriz. 
Apresente-a na tela com uma aparência matricial.
"""

import random

inicio_range = 0
fim_range = 20
Lin = int(input("digite por favor a quantidade de linhas: "))
Col = int(input("digite por favor a quantidade de colunas: "))
M = []
i = 0
while i < Lin:
    M.append([])
    j = 0
    while j < Col:
        M[i].append(random.randint(inicio_range, fim_range))
        j += 1
    i += 1

print("\nEsta é a lista M gerada: ")
print("M = ", M)

print("Exibindo como matriz fica assim: ")
i = 0
while i < Lin:
    j = 0
    print("|", end="")
    while j < Col:
        print("{0:4}".format(M[i][j]), end="")
        j += 1
    print(" |")
    i += 1

