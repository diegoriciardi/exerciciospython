"""
14. Escreva um programa que calcule os N primeiros termos de uma PG com razão R 
e o primeiro termo P1 fornecidos pelo usuário. Também deve ser calculada e 
apresentada a soma desses N termos.
"""

try:
    quantidade_termos = int(input("digite por favor a quantidade de termos: "))
    razao = int(input("digite por favor a razao: "))
    termo = int(input("digite por favor o primeiro termo: "))

    contador = 1

    print(termo)
    while contador < quantidade_termos:
        termo *= razao
        print(termo)
        contador += 1


except Exception as e:
    print("Ocorreu um erro. {}".format(e))