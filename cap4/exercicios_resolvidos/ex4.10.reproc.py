"""
10. Busca binária de um valor em uma lista. Reescreva o programa do exercício anterior, 
trocando o algoritmo de busca sequencial pelo algoritmo de busca binária. O algoritmo de 
busca binária é significativamente mais rápido que o de busca sequencial quando aplicado 
a grandes conjuntos de dados. Porém, ele requer que a lista esteja ordenada. A ideia básica
implementada nesse algoritmo é verificar se o valor procurado “x” está na posição central 
da lista. Se estiver, então, o valor foi encontrado e o algoritmo termina. Caso não esteja
e x seja menor que o valor central, então, a busca prossegue na metade à esquerda do centro;
caso seja maior, a busca prossegue na metade à direita.
"""

quantidade = int(input("Digite por favor o valor de N: "))
lista = list(range(2, quantidade+1, 2))
print("A lista gerada foi...: ", lista)

numero = int(input("Digite por favor o número para busca binária: "))

while numero != 0:
    inicio = 0
    fim = len(lista)-1
    meio = (inicio + fim) // 2
    while inicio <= fim:
        if numero == lista[meio]:
            print("achei o número {}".format(numero))
            break
        if numero < lista[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1
        meio = (inicio + fim) // 2
    else:
        print("Não achei o número {}".format(numero))
    numero = int(input("Digite por favor o número para busca binária: "))
