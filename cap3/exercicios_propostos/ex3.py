"""
3. Uso de condições mistas: considerando os valores fornecidos, 
avalie cada condição composta e informe se o resultado é falso (False) ou verdadeiro (True). 
Faça o teste dessas condições no IDLE do Python.
"""

"""
condições compostas
"""

resultado = False

#1
A = 10
B = 15
C = 4
if A < B and A < C or C != 0:
    resultado = True
else:
    resultado = False
print("[{}] < [{}] and [{}] < [{}] or [{}] != [{}] = {}".format(A, B, A, C, C, 0, resultado))


#2
A = 10
B = 15
C = 4
if A < B and (A < C or C != 0):
    resultado = True
else:
    resultado = False
print("[{}] < [{}] and ([{}] < [{}] or [{}] != [{}]) = {}".format(A, B, A, C, C, 0, resultado))

#3
A = 1
B = 9
C = 0
if not (A >= 0 and B == C):
    resultado = True
else:
    resultado = False
print("not ([{}] >= [{}] and [{}] == [{}]) = {}".format(A, 0, B, C, resultado))

#4
A = 1
B = 9
C = 9
if not (A >= 0) and not (B == C):
    resultado = True
else:
    resultado = False
print("not ([{}] >= [{}]) and not ([{}] == [{}]) = {}".format(A, 0, B, C, resultado))

#5
A = 1
B = 9
C = 0
if (A >= 0 or B == C) and B > A:
    resultado = True
else:
    resultado = False
print("([{}] >= [{}] or [{}] == [{}]) and [{}] > [{}] = {}".format(A, 0, B, C, B, A, resultado))

#6
A = -2
B = 0
C = 2
if not (A <= B) or C > B:
    resultado = True
else:
    resultado = False
print("not ([{}] <= [{}]) or [{}] > [{}] = {}".format(A, B, C, B, resultado))

#7
A = -2
B = 0
C = 2
if not (A <= B or C > B):
    resultado = True
else:
    resultado = False
print("not ([{}] <= [{}] or [{}] > [{}]) = {}".format(A, B, C, B, resultado))

#8
A = 0
B = 1
C = 0
if A == 0 and B != 0 and C == 0:
    resultado = True
else:
    resultado = False
print("[{}] == [{}] and [{}] != [{}] and [{}] == [{}] = {}".format(A, 0, B, 0, C, 0, resultado))

#9
A = 5
B = 0
C = 0
if A == 0 and B != 0 and C == 0:
    resultado = True
else:
    resultado = False
print("[{}] == [{}] and [{}] != [{}] and [{}] == [{}] = {}".format(A, 0, B, 0, C, 0, resultado))

#10
A = 5
B = 0
C = 0
if A == 0 or B != 0 or C == 0:
    resultado = True
else:
    resultado = False
print("[{}] == [{}] or [{}] != [{}] or [{}] == [{}] = {}".format(A, 0, B, 0, C, 0, resultado))
