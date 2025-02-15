"""
6. Refaça o exercício 5 alterando-o de modo que a base e a 
altura do triângulo sejam lidas do teclado. 
Considere-as números reais.
"""

base = float(input("Digite por favor a base do triangulo: "))
altura = float(input("Digite por favor a altura do triangulo: "))
area = base * altura / 2

print("A area do triangulo = {}".format(area))