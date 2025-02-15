n = int(input("digite por favor um número: "))
cont = 0
i = 2
while i < n:
    r = n % i
    if r == 0:
        cont += 1
    i += 1

if cont == 0:
    print("{} é primo".format(n))
else:
    print("{} Não é primo".format(n))