print("Pesquisa sequencial\n")
N = int(input("Digite N: "))
L = list(range(2, N+1, 2))
print("Lista gerada: ", L)

x = int(input("Digite x: "))
while x != 0:
    ini = 0
    fim = len(L)-1
    meio = (ini + fim) // 2
    while ini <= fim:
        if x == L[meio]:
            print("{} está na lista".format(x))
            break
        if x < L[meio]:
            fim = meio - 1
        else:
            ini = meio + 1
        meio = (ini + fim) // 2
    else:
        print("{} não está na lista".format(x))
    x = int(input("Digite x: "))

print("Fim do programa")