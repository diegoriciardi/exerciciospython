"""
7. Escreva um programa que leia três números reais e informe se eles constituem 
os lados de um triângulo. Em caso afirmativo, informe se o triângulo é equi-látero, 
isósceles ou escaleno. Para que três números formem um triângulo, a soma dos dois 
lados menores deve ser maior que o lado maior. Uma boa solução para esse problema 
envolve o uso dos operadores and e or.
"""

triangulo = False

try:
    n1 = float(input("digite por favor a primeira medida: "))
    n2 = float(input("digite por favor a segunda medida: "))
    n3 = float(input("digite por favor a terceira medida: "))

    if n1 < (n2 + n3) and n2 < (n1 + n3) and n3 < (n1 + n2):
        triangulo = True
        print("é triangulo {}".format(triangulo))
        if n1 == n2 and n2 == n3:
            print("equilátero")
        elif n1 != n2 and n2 != n3:
            print("escaleno")
        else:
            print("isóceles")
    else:
        print("essas medidas Não formam um triangulo")

    # if n1 >= n2 and n1 >= n3:
    #     if n2 >= n3:
    #         print(n1, n2, n3)
    #     else:
    #         print(n1, n3, n2)
    #     if n1 < n2 + n3:
    #         triangulo = True
    # if n2 >= n1 and n2 >= n3:
    #     if n1 >= n3:
    #         print(n2, n1, n3)
    #     else:
    #         print(n2, n3, n1)
    #     if n2 < n1 + n3:
    #         triangulo = True
    # if n3 >= n1 and n3 >= n2:
    #     if n1 >= n2:
    #         print(n3, n1, n2)
    #     else:
    #         print(n3, n2, n1)
    #     if n3 < n1 + n2:
    #         triangulo = True

except:
    print("por favor digite números reais")