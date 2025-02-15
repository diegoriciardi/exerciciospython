L = [2, 4, 6, 8, 10]
print("lista L: ", L)

V = L

print("lista V: ", V)

print(V[0])

V[0] = 15

print("lista L: ", L)
print("lista V: ", V)

print("id lista L", id(L))
print("id lista V", id(V))

C = L.copy()

print("lista C: ", C)

print("id lista C: ", id(C))

C[0] = 2

print("lista C: ", C)
print("id lista C", id(C))
