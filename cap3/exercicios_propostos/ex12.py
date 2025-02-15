"""
12. Escreva um programa que leia um número inteiro N e, em seguida, leia N números reais, 
calculando a soma de todos os valores positivos fornecidos e ignorando os negativos. 
Este exercício pode ser elaborado a partir do Exer-cício resolvido 3.1, no qual, em vez de 
gerar números aleatórios, os valores sejam lidos do teclado.
"""

try:
    n = int(input("digite por favor a quantidade de valores (inteiro): "))

    contador = 1
    soma = 0

    while contador <= n:
        r = float(input("digite por favor o {}º valor (real): ".format(contador)))
        if r > 0:
            soma += r
        contador += 1
    print("A soma dos valores positivos informados = {:.2f}".format(soma))

except Exception as e:
    print("Ocorreu um erro. {}".format(e))