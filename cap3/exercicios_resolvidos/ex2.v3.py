"""
2. Programa que gera a sequência de Fibonacci
Escreva um programa que leia um número inteiro N e, em seguida, mostre na tela os N 
primeiros termos da sequência de Fibonacci. Faça o programa de modo que N seja no 
mínimo 2.A sequência de Fibonacci é uma sequência de números inteiros que tem as seguintes 
regras de formação: os dois primeiros termos são 0 e 1; do terceiro em diante cada 
termo é a soma dos dois anteriores. 
Se N = 10, então: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
"""

print("Sequencia de Fibonacci\n")
# leitura do numero de termos

N = 0
while N < 2:
    try:
        N = int(input("digite por favor um número inteiro N >= 2: "))
        if N < 2:
            print("digite por favor N >= 2: ")
    except:
        print("O dado digitado deve ser um número inteiro")

A = 0
B = 1
print("0, 1", end="")

i = 0

while i < N-2:
    C = A + B
    print(", {}".format(C), end="")
    A = B
    B = C
    i += 1

print("\n\nFim do programa")
