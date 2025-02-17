"""
8. Programa que gera uma lista em ordem crescente Escreva um programa que permaneça em laço lendo números inteiros 
enquanto os valores digitados forem diferentes de zero. Para cada valor digitado, adicione-o a uma lista na posição 
imediatamente anterior ao primeiro elemento da lista que seja maior ou igual a ele. Exiba a lista no final.
"""
import time

sleepsecond = 2
lista = []
n = int(input("digite por favor um numero: "))
if n != 0:
    lista.append(n)

    while True:
        n = int(input("digite por favor um número: "))
        if n != 0:
            if n not in lista:
                lista.append(n)
                for x in lista:
                    if n <= x:
                        temp = lista.index(x)
                        lista.insert(temp, n)
                        lista.pop()
                        break
            print("...:tamanho {}:... {}".format(len(lista), lista))
        else:
            print("\n\n -- parando o programa -- \n\n")
            time.sleep(sleepsecond)
            break
else:
    print("\n\n -- parando o programa -- \n\n")
    time.sleep(sleepsecond)
print("listagem: ", lista)