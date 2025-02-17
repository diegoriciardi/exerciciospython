print("Pesquisa sequencial: ")
N = int(input("Digite N: "))
L = list(range(2, N+1, 2))
print("Lista gerada: ", L)

x = int(input("Digite x: "))
while x != 0:
    if x in L:
        print("{} está na lista".format(x))
    else:
        print("{} Não está na lista".format(x))
    x = int(input("Digite x: "))

print("Fim do programa")