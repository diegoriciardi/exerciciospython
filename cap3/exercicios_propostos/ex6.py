"""
6. Escreva um programa que leia dois números quaisquer e mostre na tela qual é o menor e qual é o maior.
"""

mensagem = "{} é maior que {}"

try:
    n1 = int(input("digite por favor o primeiro numero: "))
    n2 = int(input("digite por favor o segundo numero: "))

    if n1 > n2:
        print(mensagem.format(n1, n2))
    elif n2 > n1:
        print(mensagem.format(n2, n1))
    else:
        print("os número {} e {} são iguais".format(n1, n2))
except:
    print("por favor digite número inteiros")
