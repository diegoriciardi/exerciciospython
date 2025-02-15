"""
21. Reescreva o programa do Exercício resolvido 3.2 -
Sequência de Fibonacci fazendo a seguinte alteração: leia N 
que será a quantidade de termos a ser exibida e leia um número 
inteiro adicional chamado Prim. Essa versão do programa deverá 
apresentar N termos da sequência de Fibonacci imedia-tamente maiores que Prim.

    2. Programa que gera a sequência de Fibonacci
    Escreva um programa que leia um número inteiro N e, em seguida, mostre na tela os N 
    primeiros termos da sequência de Fibonacci. Faça o programa de modo que N seja no 
    mínimo 2.A sequência de Fibonacci é uma sequência de números inteiros que tem as seguintes 
    regras de formação: os dois primeiros termos são 0 e 1; do terceiro em diante cada 
    termo é a soma dos dois anteriores. 
    Se N = 10, então: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
"""

try:
    n = int(input("digite por favor a quantidade desejada de termos da sequencia fibonacci: "))
    addprim = int(input("digite por favor o Prim: "))

    a = 0
    b = 1
    contador = 2
    if addprim <= 0:
        print(f"{a} {b} ", end="")

    while contador < n:
        c = a + b
        if c > addprim:
            print(f"{c} ", end="")
        a = b
        b = c
        contador += 1

except Exception as e:
    print("Ocorreu um erro. {}".format(e))
