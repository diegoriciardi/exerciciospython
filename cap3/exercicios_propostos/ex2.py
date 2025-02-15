"""
2. Uso de condições compostas: considerando os valores fornecidos, 
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
if A < B and A < C:
    resultado = True
else:
    resultado = False
print("[{}] < [{}] and [{}] < [{}] = {}".format(A, B, A, C, resultado))


#2
A = 10
B = 15
C = 4
if A < B or A < C:
    resultado = True
else:
    resultado = False
print("[{}] < [{}] or [{}] < [{}] = {}".format(A, B, A, C, resultado))

#3
A = 1
B = 9
C = 0
if A >= 0 and B == C:
    resultado = True
else:
    resultado = False
print("[{}] >= [{}] and [{}] == [{}] = {}".format(A, 0, B, C, resultado))

#4
A = 1
B = 9
C = 9
if A >= 0 and B == C:
    resultado = True
else:
    resultado = False
print("[{}] >= [{}] and [{}] == [{}] = {}".format(A, 0, B, C, resultado))

#5
A = 1
B = 9
C = 0
if A >= 0 or B == C:
    resultado = True
else:
    resultado = False
print("[{}] >= [{}] or [{}] == [{}] = {}".format(A, 0, B, C, resultado))

#6
A = 1
B = 9
C = 9
if A >= 0 or B == C:
    resultado = True
else:
    resultado = False
print("[{}] >= [{}] or [{}] == [{}] = {}".format(A, 0, B, C, resultado))

#7
A = 0
B = 0
C = 0
if B != 0 and A != C:
    resultado = True
else:
    resultado = False
print("[{}] != [{}] and [{}] != [{}] = {}".format(B, 0, A, C, resultado))

#8
A = 0
B = 0
C = 25
if B != 0 and A != C:
    resultado = True
else:
    resultado = False
print("[{}] != [{}] and [{}] != [{}] = {}".format(B, 0, A, C, resultado))

#9
A = 0
B = 0
C = 0
if B != 0 or A != C:
    resultado = True
else:
    resultado = False
print("[{}] != [{}] or [{}] != [{}] = {}".format(B, 0, A, C, resultado))

#10
A = 0
B = 0
C = 25
if B != 0 or A != C:
    resultado = True
else:
    resultado = False
print("[{}] != [{}] or [{}] != [{}] = {}".format(B, 0, A, C, resultado))
