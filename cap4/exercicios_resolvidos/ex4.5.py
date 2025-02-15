"""
5. Criação de uma lista contendo números inteiros Escreva um programa que leia um número inteiro
 N e gere uma lista com N elementos aleatórios (utilize a função randint explicada no Exercício 
 resolvido 3.7) entre 10 e 50. Exiba a lista gerada e exiba também a mesma lista com seus 
 elementos ordenados em ordem crescente.

    Tarefa adicional

    Essa solução tem um problema. Caso o dado digitado não seja um número inteiro, o uso da função de 
    conversão int causará um erro. Faça um teste. Isso pode ser resolvido com o comando try-except 
    (Capítulo 3, Item 3.3). Como desafio, sugere-se ao leitor que faça tal alteração.

        Como foi visto, a execução desse programa para N = 8 gerou uma lista con-tendo duas ocorrências do valor 50. 
        Nada foi dito no enunciado sobre isso. A tarefa é alterar esse programa de modo que não haja valores 
        duplicados na lista gerada. Dica: lembre-se dos operadores in e not in.
"""

import random

try:
    quantidade = int(input("digite por favor a quantidade (inteiro) para geração de números aleatórios: "))
    contador = 0
    lista = []
    inicio = 10
    fim = 50

    while contador < quantidade:
        x = random.randint(inicio, fim)
        if x not in lista:
            lista.append(x)
        # else:
        #     print("esse {} veio duplicado meu fio".format(x))
        contador += 1
except Exception as e:
    print("Ocorreu um erro. {}".format(e))
else:
    print("lista gerada: {}".format(lista))
    print("lista gerada ordenada (crescente): {}".format(sorted(lista)))