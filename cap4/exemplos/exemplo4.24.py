P = (14, 26, [0, 0, 0], 31)
print("P: ", P)

print("P[2]: ", P[2])

print("type(P[2]): ", type(P[2]))

P[2][1] = 39

print("P[2][1] = 39: ", P)

P[2].append(16)

print("P[2].append(16): ", P)

P[2].remove(0)

print("P[2].remove(0): ", P)

P[2].clear()

print("P[2].clear(): ", P)

P[2] = 'outra coisa' # erro tuplas são imutáveis

