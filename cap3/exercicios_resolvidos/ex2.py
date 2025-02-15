"""
2. Programa que gera a sequência de Fibonacci
Escreva um programa que leia um número inteiro N e, em seguida, mostre na tela os N 
primeiros termos da sequência de Fibonacci. Faça o programa de modo que N seja no 
mínimo 2.A sequência de Fibonacci é uma sequência de números inteiros que tem as seguintes 
regras de formação: os dois primeiros termos são 0 e 1; do terceiro em diante cada 
termo é a soma dos dois anteriores. 
Se N = 10, então: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
"""
n = int(input("digite por favor a quantidade desejada de termos da sequencia fibonacci: "))
contador = 0
termo = 1
lista = []
anterior = 1
numeros = ""

while contador < n:
    if contador == 0 or contador == 1:
        # lista.append(contador)
        # print(contador)
        numeros += str(contador) + ", "
    elif contador == 2:
        # print(anterior)
        numeros += str(anterior)
    else:
        termo += anterior
        # print(termo)
        numeros += ", " + str(termo)
        anterior = termo-anterior

        # lista.append(termo)
        # termo = lista[contador] + lista[contador-1]
        
    contador += 1

# print(lista)

print(numeros)