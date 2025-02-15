a = int(input("digite o valor de a: "))
b = int(input("digite o valor de b: "))

try:
    r = a / b
    print("Resultado de {} / {} é {:.1f}".format(a, b, r))
except:
    print("Não é possível calcular a divisão")

