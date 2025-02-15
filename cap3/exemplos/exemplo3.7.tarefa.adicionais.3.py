p = int(input("digite por favor o primeiro termo: "))
r = int(input("digite por favor a razão: "))
q = int(input("digite por favor quantos termos devem ser impressos: "))
cont = 0
soma = 0
while cont < q:
    print("Termo {} da PA = {}".format(cont+1, p))
    soma += p
    p += r
    cont += 1

print("A soma total dos termos = {}".format(soma))