"""
Faça a leitura de uma linha de dados que contenha quatro números separados
por espaços em branco e carregue os objetos A, B, C com os valores individuais. 
Exemplo: linha a ser digitada 35 22 87 o programa deve carregar: A com 35, B com 22, C com 87
"""

entrada_de_dados = input("digite por favor os número separados por espaço em branco: ")

A = int(entrada_de_dados.split()[0])
B = int(entrada_de_dados.split()[1])
C = int(entrada_de_dados.split()[2])

print("Valor de A = {}".format(A))
print("Valor de B = {}".format(B))
print("Valor de C = {}".format(C))