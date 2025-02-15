"""
19. Escreva um programa que contenha um laço que será executado enquanto o número 
digitado for diferente de zero. Para cada número digitado pelo usuário, mostrar na tela 
apenas os que forem divisíveis por 2 e por 3
"""

try:

    primeiro_divisor = 2
    segundo_divisor = 3

    while True:
        x = int(input("digite por favor um numero: "))
        if x != 0:
            if x % 2 == 0 and x % 3 == 0:
                print("O numero {} é divisível por {} e {}".format(
                    x,
                    primeiro_divisor,
                    segundo_divisor
                ))
        else:
            break

except Exception as e:
    print("Ocorreu um erro. {}".format(e))