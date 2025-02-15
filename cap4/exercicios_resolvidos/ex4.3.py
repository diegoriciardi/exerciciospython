"""
3. Criação de uma progressão aritmética Escreva um programa que leia três dados de entrada: o primeiro termo, a
razão e a quantidade de termos de uma P.A., todos números inteiros. O programa deve calcular todos os termos, 
colocando-os em uma lista, e exibi-la no final.
"""

try:
    termo1 = int(input("digite por favor o primeiro termo: "))
    razao = int(input("digite por favor a razão: "))
    quantidade_termos = int(input("digite por favor a quantidade de termos: "))
    proximo_termo = termo1
    lista_termos = []
    contador = 0

    while contador < quantidade_termos:
        lista_termos.append(proximo_termo)
        proximo_termo += razao
        contador += 1

except Exception as e:
    print("Ocorreu um erro. {}".format(e))
else:
    print("lista dos termos: {}".format(lista_termos))