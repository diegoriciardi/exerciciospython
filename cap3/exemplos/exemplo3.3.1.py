"""
O que se deseja fazer no Exemplo 3.4 é que três números sejam carregados
em A, B e C, e o programa deve mostrá-los em ordem crescente.
"""

a = float(input("digite por favor o numero 1: "))
b = float(input("digite por favor o numero 2: "))
c = float(input("digite por favor o numero 3: "))

if a >= b and a >= c:
    if b >= c:
        print(c, b, a, sep=" > ")
    else:
        print(b, c, a, sep=" > ")
elif b >= a and b >= c:
    if a >= c:
        print(c, a, b, sep=" > ")
    else:
        print(a, c, b, sep=" > ")
else:
    if a >= b:
        print(b, a, c, sep=" > ")
    else:
        print(a, b, c, sep=" > ")
