"""
11. Escreva um programa que leia um número inteiro e, em seguida, apresen-te na tela
a tabuada de 0 a 10 para esse número fornecido. 
Siga o formato apresentado a seguir (supondo que foi digitado 4): 

4 x 1 = 4
4 x 2 = 8
"""

try:
    n = int(input("digite por favor um numero inteiro: "))

    contador = 1
    limite = 10

    while contador <= 10:
        print("{} x {} = {}".format(
            n,
            contador,
            (n*contador)
        ))
        contador += 1
except Exception as e:
    print("Ocorreu um erro. {}".format(e))