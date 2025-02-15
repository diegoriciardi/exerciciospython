"""
1. Uso de condições simples: considerando os valores fornecidos, 
avalie cada condição e informe se o resultado é falso (False) ou verdadeiro (True). 
Avalie cada condição e anote o resultado que teste essas condições no IDLE do Python, 
conforme mostrado na Figura 3.2.

Valores para o teste	        Condição
1) Para A = 0 e B = -3                A > B
2) Para X = 3.7                       X <= 10.0
3) Para A = 9 e B = 16                A - B >= 0
4) Para A = 2, B = 4 e N = 10         A * B < N
5) Para A = 3, B = 9 e C = 5          10 * A >= B * C
6) Para A = 3, B = 6 e C = 5          10 * A >= B * C
7) Para N = 7                         N % 2 == 0
8) Para N = 8                         N % 2 == 0
9) Para T = "MORANGO"                 T == "BANANA"
10) Para T = "MORANGO"                T > "BANANA"
"""

# #1
# A = 0
# B = -3
# print("[{}] > [{}] = {}".format(A, B, A > B))

# #2
# X = 3.7
# print("[{}] <= 10.0 = {}".format(X, X <= 10.0))

# #3
# A = 9
# B = 16
# print("[{}] - [{}] >= 0 = {}".format(A, B, A - B >= 0))

# #4
# A = 2
# B = 4
# N = 10
# print("[{}] * [{}] < [{}] = {}".format(A, B, N, A * B < N))

# #5
# A = 3
# B = 9
# N = 5
# print("[{}] * [{}] < [{}] = {}".format(A, B, N, A * B < N))

# #6
# A = 3
# B = 6
# C = 5
# print("10 * [{}] >= [{}] * [{}] = {}".format(A, B, C, 10 * A >= B * C))

# #7
# N = 7
# print("[{}] % 2 == 0 = {}".format(N, N % 2 == 0))

# #8
# N = 8
# print("[{}] % 2 == 0 = {}".format(N, N % 2 == 0))

# #9
# T = "MORANGO"
# print("[{}] == 'BANANA' = {}".format(T, T == "BANANA"))

# #10
# T = "MORANGO"
# print("[{}] > 'BANANA' = {}".format(T, T > "BANANA"))

"""
condições simples
"""

resultado = False

#1
A = 0
B = -3
if A > B:
    resultado = True
else:
    resultado = False
print("[{}] > [{}] = {}".format(A, B, resultado))

#2
X = 3.7
if X <= 10.0:
    resultado = True
else:
    resultado = False
print("[{}] <= 10.0 = {}".format(X, resultado))

#3
A = 9
B = 16
if A - B >= 0:
    resultado = True
else:
    resultado = False
print("[{}] - [{}] >= 0 = {}".format(A, B, resultado))

#4
A = 2
B = 4
N = 10
if A * B < N:
    resultado = True
else:
    resultado = False
print("[{}] * [{}] < [{}] = {}".format(A, B, N, resultado))

#5
A = 3
B = 9
N = 5
if A * B < N:
    resultado = True
else:
    resultado = False
print("[{}] * [{}] < [{}] = {}".format(A, B, N, resultado))

#6
A = 3
B = 6
C = 5
if  10 * A >= B * C:
    resultado = True
else:
    resultado = False
print("10 * [{}] >= [{}] * [{}] = {}".format(A, B, C, resultado))

#7
N = 7
if  N % 2 == 0:
    resultado = True
else:
    resultado = False
print("[{}] % 2 == 0 = {}".format(N, resultado))

#8
N = 8
if N % 2 == 0:
    resultado = True
else:
    resultado = False
print("[{}] % 2 == 0 = {}".format(N, resultado))

#9
T = "MORANGO"
if T == "BANANA":
    resultado = True
else:
    resultado = False
print("[{}] == 'BANANA' = {}".format(T, resultado))

#10
T = "MORANGO"
if T > "BANANA":
    resultado = True
else:
    resultado = False
print("[{}] > 'BANANA' = {}".format(T, resultado))