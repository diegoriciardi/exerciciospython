"""
20. Elabore um programa que apresente o somatório dos valores pares 
exis-tentes na faixa entre 1 e N, em que N é um número digitado pelo usuário 
e que deve ser no mínimo 100 (obrigatório garantir esse requisito).
"""

try:
    n = int(input("digite por favor um valor de faixa (minimo = 100): "))
    minimo = 10
    if n < minimo:
        print("** Alterando o número {} para o mínimo que é {} **".format(n, minimo))
        n = minimo
    contador = 1
    soma = 0
    print("vou somar os números: ", end="")
    while contador <= n:
        if contador % 2 == 0:
            print("{}, ".format(contador), end="")
            soma += contador
        contador += 1
    print("\n\n")
    print("A soma dos número pares é: {}".format(soma))
except Exception as e:
    print("Ocorreu um erro. {}".format(e))