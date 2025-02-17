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

N = int(input("Digite por favor valor de N: "))
L = list(range(2, N+1, 2))
print("Lista gerada: ", L, len(L))
contador_iteracoes = 0

x = int(input("Digite um número para pesquisar: "))

while len(L) > 1:
    
    contador_iteracoes += 1

    meio = L[len(L) // 2]

    # print("o meio da lista é: ", meio)

    achei = x == meio

    if achei:
        print("achei o número {}".format(x))
        break
    else:
        if x > meio:
            L=L[L.index(meio):]
        else:
            L=L[:L.index(meio)]
    print("interacao {}º".format(contador_iteracoes))
else:
    print("Não achei o número {} na lista".format(x))