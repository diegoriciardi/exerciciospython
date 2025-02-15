import math

try:
    a = int(input("digite por favor o valor de A: "))
    b = int(input("digite por favor o valor de B: "))
    r = a / b
    if a < 0:
        c = math.cos(a)
        print("resultado: R = %.1f" % r)
except ZeroDivisionError:
    print("B não pode ser zero")
except ValueError:
    print("Digite números inteiros para A e B")
except Exception as e:
    print("Erro desconhecido. Não é possível calcular a divisão.\n{}".format(e))