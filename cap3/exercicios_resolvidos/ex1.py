"""
1. Programa que totaliza um conjunto de valores
Escreva um programa que leia um número inteiro N e, em seguida, 
gere N números aleatórios no intervalor [1, 50] e totalize-os. 
Para gerar números aleatórios, use a função randint, disponível na biblioteca random.
"""

import random

try:
    quantity_numbers = int(input("digite por favor um número inteiro N: "))
    sum_numbers = 0
    count = 0
    initial_limit = 1
    while count < quantity_numbers:
        temp_number = random.randint(initial_limit, quantity_numbers)
        print("({}º) execution generated [{}] number".format(count+1, temp_number))
        sum_numbers += temp_number
        count += 1
except ValueError:
    print("Please type a number.")
else:
    print("The sum of these number is = {}".format(sum_numbers))
finally:
    print("End of the program")
    