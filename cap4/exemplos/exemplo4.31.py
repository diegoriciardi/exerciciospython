"""
Exemplo 4.32 Comando for em conjunto com uma tupla listas de tuplas
"""
P = (12336, "Sabão", 1337, 1.37)
L = []
L.append(P)
P = (13446, "Arroz 1kg", 3554, 2.65)
L.append(P)
P = (13956, "Fubá 500g", 439, 1.19)
L.append(P)
print(L)

print("Início do programa")

print("\nLista dos produtos em Estoque: \n")

for (Cod, Nome, Qtde, PcUnit) in L:
    print("Identificação do produto: ", Cod)
    print("Descrição: ", Nome)
    print("Estoque = {0} a R$ {1:.2f}".format(Qtde, PcUnit))
    print("Total desse produto: R$ {0:.2f}".format(Qtde * PcUnit))
    print()

print("Fim do programa")