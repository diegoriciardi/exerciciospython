try:
    a = int(input("digite por favor um valor inteiro para A: "))
    b = int(input("digite por favor um valor inteiro para B: "))

    r = a / b

    print("{} dividido por {} resulta em {:.1f}".format(a, b, r))
except Exception as e:
    print("Não foi possível efetuar a divisão.\n{}".format(e))