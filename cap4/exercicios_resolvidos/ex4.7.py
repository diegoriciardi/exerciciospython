"""
7. Programa que gera uma lista com a sequência de Fibonacci A sequência de Fibonacci 
já foi explicada no Exercício resolvido 3.7. Escreva um programa que gere os N primeiros 
termos dessa sequência utilizando uma lista para armazená-los. N é um número inteiro a 
ser lido do teclado e deve, obrigatoriamente, ser maior ou igual a 2.
"""

try:
    N = int(input("digite por favor a quantidade desejada de termos fibonacci (mínimo 2): "))
    if N < 2:
        print("\nAlterando o valor da quantidade para o mínimo = 2")
        N = 2
    lista = [0, 1, 1]
    contador = 0

    mensagem = "A lista é: {}"

    if N == 2:
        print(mensagem.format(lista))
    else:
        contador = 2
        while contador < N-1:
            proximo = lista[-1] + lista[-2]
            lista.append(proximo)
            contador += 1
        print("A lista eh: ", lista)
    
except Exception as e:
    print("Ocorreu um erro. {}".format(e))
    