ph = float(input("Digite por favor um valor do PH: "))
if ph < 7.0:
    print("Solução ácida")
elif ph == 7.0:
    print("Solução neutra")
else:
    print("Solução básica")
