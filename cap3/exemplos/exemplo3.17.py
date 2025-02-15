n = 0
while n < 100 or n > 500:
    try:
        s = input("digite por favor N no intervalo [100, 500]: ")
        n = int(s)
    except:
        print("{} não é um número.".format(s))
        n = 0
    else:
        if n < 100 or n > 500:
            print("o valor lido [{}] está fora do intervalo.".format(n))
        else:
            print("o valor lido [{}] está OK.".format(n))
    finally:
        print("\n\n")