soma = 0
cont = 0
x = int(input("digite por favor o valor de x: "))
while x != 0:
    soma += x
    cont += 1
    x = int(input("digite por favor o valor de x: "))

print("total dos valores: {}".format(soma))
print("quantidade de valores: {}".format(cont))