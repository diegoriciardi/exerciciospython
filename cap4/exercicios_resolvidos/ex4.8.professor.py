"""
Exercício resolvido 4.8 – Gerador de lista em ordem crescente
"""

print("Gera lista em ordem crescente\n")
L = []
x = int(input("digite um valor: "))
while x != 0:
    p = 0
    while p < len(L) and L[p] < x:
        p += 1
    L.insert(p, x)
    x = int(input("digite um valor: "))

print("Lista gerada: ", L)
print("Fim do programa")

