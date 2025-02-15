"""
4. Criação de uma lista contendo números inteiros Escreva um programa que permaneça em laço lendo números inteiros
enquanto os valores digitados forem diferentes de zero. Cada número não zero digitado deve ser incluído em uma lista. 
Ao final, exiba a lista e seu tamanho.
"""
lista = []

while True:
    n = int(input("digite por favor um número inteiro: "))
    if n != 0:
        lista.append(n)
    else:
        print("\nparando o programa...\n")
        break
print("o tamanho da lista é: {}".format(len(lista)))
print(lista)