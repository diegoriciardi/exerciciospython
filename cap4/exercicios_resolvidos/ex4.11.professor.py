print("Ordenação bolha\n")
L = [17, 4, 23, 8, 19, 12]
print("Lista gerada: ", L)

Trocou = 1
while Trocou:
    Trocou = 0
    i = 0
    while i < len(L)-1:
        if L[i] > L[i+1]:
            L[i], L[i+1] = L[i+1], L[i]
            Trocou = 1
        i += 1
    print("  estado parcial de L: ", L)
print("Situação Final")
print("Lista ordenada: ", L)
print("Fim do programa")