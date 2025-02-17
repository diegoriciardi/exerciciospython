"""
9. Busca sequencial de um valor em uma lista Escreva um programa que leia um
 número inteiro  N e gere uma lista com números pares de 2 até N. Se N for par, 
 deve estar incluído na lista. Em seguida, inicie um laço que deve  permanecer em execução 
 enquanto x for diferente de zero. Para cada  valor de x fornecido, o programa deve 
 informar se x está ou não na lista.
"""

import random

N = int(input("digite por favor um numero inteiro: "))

if N != 0:

    contador = 2
    lista = [contador]

    while contador <= N:
        aleatorio = random.randint(2, N)
        if aleatorio % 2 == 0:
        # if aleatorio not in lista:
            # print("o numero aleatorio eh {}".format(aleatorio))
            lista.append(aleatorio)
            contador += 1

    # print("Lista aleatoria gerada entre {} e {} ==> {}".format(
    #     2,
    #     N,
    #     sorted(lista)
    # ))

    x = 1
    while x != 0:
        x = int(input("digite por favor uma valor para busca na lista: "))
        if x == 0:
            print("\n\n -- parando o programa -- \n\n")
        else:
            if x not in lista:
                print("o número {} Não esta na lista".format(x))
            else:
                print("Parabéns...o número {} faz parte da lista".format(x))
                # break
else:
    print("Nenhuma execução feita porque foi digitado o número 0")
