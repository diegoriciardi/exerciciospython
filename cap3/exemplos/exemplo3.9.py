x = 1
while x != 0:
    x = int(input("digite por favor um valor: "))
    if x <= 0:
        continue
    print("exibindo o valor de x = {}".format(x))