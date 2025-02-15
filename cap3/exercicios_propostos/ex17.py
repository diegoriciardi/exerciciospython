"""
17. Reescreva um programa do exercício 16 ignorando os números negativos fornecidos pelo usuário.

    16. Escreva um programa que leia um número inteiro N e, em seguida, leia N números reais, 
    separando o menor e o maior, apresentando-os na tela.
"""

try:
    n = int(input("digite por favor a quantidade de numeros reais a ser inserida: "))

    contador = 1
    mensagem = "maior {} e menor {}"

    valor = float(input("digite por favor o {}º valor: ".format(contador)))
    maior = menor = valor
    contador += 1

    while contador <= n:

        valor = float(input("digite por favor o {}º numero real: ".format(contador)))

        if valor > 0:
            if valor >= maior:
                maior = valor
            elif valor <= menor:
                menor = valor
            contador += 1

    print(mensagem.format(maior, menor))


except Exception as e:
    print("Ocorreu um erro. {}".format(e))