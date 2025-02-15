"""
1. Validando a entrada de dados numérica Escreva um programa que leia
 um string que deve conter, obrigatoriamente,um número inteiro e, caso 
 isso não aconteça, emita uma mensagem de erro.
"""

S = input("Digite por favor um numero inteiro: ")
if S.isnumeric():
    N = int(S)
    print("O número digitado {} foi".format(N))
else:
    print("Erro: digite apenas números")