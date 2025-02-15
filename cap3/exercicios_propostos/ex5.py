"""
5. Escreva um programa que leia um número inteiro do teclado e diga se esse 
número é par ou ímpar. Para saber se um número é par, deve-se verificar se o 
resto de sua divisão por 2 é igual a zero. Para calcular o resto da divisão 
de um número por outro deve-se utilizar o operador %. Por exemplo: ao escrever 
a expressão em negrito a seguir e supondo que A e B tenham conteúdo inteiro.
"""

mensagem = ""

try:
    n = int(input("digite por favor um número: "))

    if n % 2 == 0:
        mensagem = f"o número {n} é PAR"
    else:
        mensagem = f"o número {n} é ÍMPAR"
except ValueError:
    print("digite por favor um número inteiro")
else:
    print(mensagem)
