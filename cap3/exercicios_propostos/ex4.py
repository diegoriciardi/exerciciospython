"""
4. Escreva um programa que leia um número inteiro do teclado e diga se esse número é positivo ou negativo.
"""

mensagem = ""

try:

    n = int(input("digite por favor um número inteiro: "))

    if n > 0:
        mensagem = f"o número {n} é positivo"
    elif n < 0:
        mensagem = f"o número {n} é negativo"
    else:
        mensagem = "tanto número pra você digitar meu amigo, e você manda um zero?"
except ValueError:
    print("por favor, digite um número inteiro")
else:
    print(mensagem)
