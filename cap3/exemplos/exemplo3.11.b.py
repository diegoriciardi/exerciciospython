n = int(input("digite por favor um número inteiro: "))
i = 2
while i < n:
    r = n % i
    if r == 0:
        print("{} Não é primo".format(n))
        break
    i += 1
else:
    print("{} é um número primo".format(n))
