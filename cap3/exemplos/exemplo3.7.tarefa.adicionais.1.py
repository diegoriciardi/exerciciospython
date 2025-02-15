p = int(input("digite por favor o primeiro termo: "))
r = int(input("digite por favor a razão: "))
q = int(input("digite por favor quantos termos devem ser impressos: "))
cont = 0
while cont < q:
    print(p)
    p += r
    cont += 1
