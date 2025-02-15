"""
Exemplo 4.26 Uso de tupla como registro
"""

P = (12336, "Sabão", 1337, 1.37)
L = []
L.append(P)
P = (13446, "Arroz 1kg", 3554, 2.65)
L.append(P)
P = (13956, "Fubá 500g", 439, 1.19)
L.append(P)
print(L)

"""
    >>> L
    # seja a lista L carregada no Exemplo 4.25
    [(12336, "Sabão", 1337, 1.37), (13446, "Arroz 1kg", 3554, 2.65), (13956, "Fubá 500g", 439, 1.19)]
    # deseja-se recuperar os dados do segundo elemento de L (L[1]) # fazendo que variáveis separadas recebam
    # os valores contidos # na tupla. Então, tem-se: 
"""

Codigo, Nome, Quantidade, PrecoUnitario = L[1]

print("Codigo: ", Codigo)
print("Nome: ", Nome)
print("Quantidade: ", Quantidade)
print("PrecoUnitario: ", PrecoUnitario)


