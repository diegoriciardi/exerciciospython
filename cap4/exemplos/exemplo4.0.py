"""
Exemplo 4.20 Uso do operador multiplicativo “*” para produzir uma matriz - um erro comum
"""

Lin = 5
Col = 3
A = [0] * Col
print("A: ", A)
A[0] = 5
A[1] = 12
A[2] = 15
print("A: ", A)
M = [A] * Lin
print("M: ", M)
# como visto acima M tem 5 sublistas e agora pode ter preenchidos 
# seus demais elementos

M[1][0] = 9
print("M: ", M)
# todas as sublistas de M agora tem seu primeiro elemento = 9


