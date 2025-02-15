"""
Exemplo 4.31 Comando for em conjunto com uma tupla de tuplas
"""

print("Início do programa\n")
T = ((3, 6), (5, 11), (7, 16))
for (a, b) in T:
    print(a, b)
print("\nFim do programa")