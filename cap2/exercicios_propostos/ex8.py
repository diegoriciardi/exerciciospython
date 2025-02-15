"""
8. Escreva em Python as seguintes expressões aritméticas para as 
fórmulas a seguir e teste as quatro primeiras 
para os valores A = 4, B = 5, C = 1 e a última para os valores x1
= 1, y1
"""

# deixamos uma png com a relação das fórmulas

from math import sqrt

a = 4
b = 5
c = 1

R = (a + b) / 2

print("Valor de R = {}".format(R))

x = (-b + sqrt(b**2 - 4*a*c)) / 2*a

print("Valor de x = {}".format(x))

R = (3*a + 2*b) / a+b

print("Valor de R = {}".format(R))

z = 7.6*a - b**1.7

print("Valor de z = {}".format(z))

x1, y1, x2, y2 = 0.0, 0.0, 3.0, 4.0
d = sqrt(((x2 - x1)**2) + (y2 - y1)**2)
print("Resultado para os números {:7f}, {:7f}, {:7f}, {:7f} = {:.3f}".format(x1, y1, x2, y2, d))

x1, y1, x2, y2 = 2.0, 1.0, 0.0, 5.0
d = sqrt(((x2 - x1)**2) + (y2 - y1)**2)
print("Resultado para os números {:7f}, {:7f}, {:7f}, {:7f} = {:.3f}".format(x1, y1, x2, y2, d))

x1, y1, x2, y2 = -3.0, 1.5, 7.1, 5.5
d = sqrt(((x2 - x1)**2) + (y2 - y1)**2)
print("Resultado para os números {:7f}, {:7f}, {:7f}, {:7f} = {:.3f}".format(x1, y1, x2, y2, d))

x1, y1, x2, y2 = 0.0, 3.5, 0.0, 7.0
d = sqrt(((x2 - x1)**2) + (y2 - y1)**2)
print("Resultado para os números {:7f}, {:7f}, {:7f}, {:7f} = {:.3f}".format(x1, y1, x2, y2, d))

x1, y1, x2, y2 = 8.2, 2.5, -5.0, -5.0
d = sqrt(((x2 - x1)**2) + (y2 - y1)**2)
print("Resultado para os números {:7f}, {:7f}, {:7f}, {:7f} = {:.3f}".format(x1, y1, x2, y2, d))

x1, y1, x2, y2 = 6.9, 2.0, 16.0, -1.8
d = sqrt(((x2 - x1)**2) + (y2 - y1)**2)
print("Resultado para os números {:7f}, {:7f}, {:7f}, {:7f} = {:.3f}".format(x1, y1, x2, y2, d))
