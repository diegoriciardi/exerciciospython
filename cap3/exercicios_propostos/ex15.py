"""
15. Escreva um programa que apresente todos os valores inteiros divisíveis por 5 situados 
no intervalo fechado [Min, Max], em que Min e Max são fornecidos pelo usuário. É obrigatório 
que o valor Max seja maior que Min e, se isso não ocorrer, o programa deve exibir uma mensagem 
de aviso ao usuário e inverter os valores.
"""

try:
    minimo = int(input("digite por favor um valor minimo (inteiro): "))
    maximo = int(input("digite por favor um valor maximo (inteiro): "))
    divisor = 5

    if minimo > maximo:
        print("O valor maximo precisa ser maior que o minimo")
        temp = maximo
        maximo = minimo
        minimo = temp

    contador = minimo
    while contador <= maximo:
        if contador % 5 == 0:
            print("o valor [{}] dentro do intervalo {}-{} é divisível por {}".format(
                contador,
                minimo,
                maximo,
                divisor
            ))
        contador += 1
except Exception as e:
    print("Ocorreu um erro. {}".format(e))