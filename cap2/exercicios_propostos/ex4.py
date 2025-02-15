"""
4. Reproduza em um programa todos os casos de operações 
aritméticas do Quadro 2.1, para A = 14 e B = 5, e compare os 
valores obtidos por você com os valores esperados constantes do quadro.

** Quadro 2.1 Operadores aritméticos em Python.
Operação			Operador	Exemplo			Resultado esperado
Adição					+		C = A + B			19
Subtração				-		C = A – B			9
Multiplicação			*		C = A * B			70
Divisão					/		C = A / B			2.8
Divisão inteira			//		C = A // B			2
Resto (módulo)			%		C = A % B			4
- unário				-		C = – A				-14
Potenciação				**		C = A ** B			537824

"""

# exercício página 47
# quadro 2.1 página 36

a = 14
b = 5

C = a + b
print(C)
C = a - b
print(C)
C = a * b
print(C)
C = a / b
print(C)
C = a // b
print(C)
C = a % b
print(C)
C = - a
print(C)
C = a ** b
print(C)