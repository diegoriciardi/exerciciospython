"""
11. Programa que ordena uma lista não ordenada. Escreva um programa que ordene uma lista não 
ordenada utilizando o algoritmo Bubble Sort. Em Python, para ordenar uma lista de qualquer tamanho, 
basta utilizar o método sort ou a função sorted, que estão prontos e já foram mencionados neste capítulo. 
Portanto, o objetivo deste exercício é mostrar e explicar a lógica do algoritmo para o leitor que está 
iniciando seus estudos de programação. Nesse algoritmo, a ideia é percorrer a lista comparando dois 
elementos vizinhos e verificando se o elemento à esquerda é maior que o da direita. Caso seja, eles devem
 ser trocados de posição. Considere-se o exemplo a seguir: ao comparar 17 com 4 será feita a troca, 
 e fica assim: 4, 17, 23, 8, 19, 12 ao comparar 17 com 23 nada muda ao comparar 23 com 8 será feita a 
 troca, e fica assim: 4, 17, 8, 23, 19, 12 ao comparar 23 com 19 será feita a troca, e fica 
 assim: 4, 17, 8, 19, 23, 12 ao comparar 23 com 12 será feita a troca, e fica assim: 4, 17, 8, 19, 12, 23
"""
import random

minimo = 1
maximo = 1000
N = int(input("digite por favor a quantidade de números para geração da lista: "))
lista = []

contador = 0

while contador < N:
    numtemp = random.randint(minimo, maximo)
    if numtemp not in lista:
        lista.append(numtemp)
    contador += 1

print("A lista é: ", lista)

print("agora vamos ordená-la")

necessario_trocar = True
quantidade_trocas = 0

while necessario_trocar:
    idx = 0
    quantidade_trocas = 0
    while idx < len(lista)-1:
        if lista[idx] > lista[idx+1]:
            temp = lista[idx]
            lista[idx] = lista[idx+1]
            lista[idx+1] = temp
            quantidade_trocas += 1
        idx += 1
    if quantidade_trocas == 0:
        necessario_trocar = False

print("lista ordenada: ", lista)

