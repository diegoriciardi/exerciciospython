"""
13. Escreva um programa que leia valores numéricos inteiros e 
totalize sepa-radamente os positivos e os negativos até que o usuário 
digite 0. Ao final, mostre na tela esses dois totais.
"""

positivos = 0
negativos = 0

try:
    while True:
        n = int(input("digite por favor um numero inteiro: "))
        if n > 0:
            positivos += n
        elif n < 0:
            negativos += n
        else:
            print("parando o programa...")
            break
    print("Total positivos: {}".format(positivos))
    print("Total negativos: {}".format(negativos))
except Exception as e:
    print("Ocorreu um erro. {}".format(e))