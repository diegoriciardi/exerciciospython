L = [3, 6, 9]
print(L)

L.append(5)
print(L)

L.append(2)
print(L)

L.insert(2, 15)
print(L)

L.insert(99, 21)
print(L)

L.append(6)
print(L)

print("count 6: ", L.count(6))

print("count 45: ", L.count(45))

print("index objeto 15: ", L.index(15))

print("index objeto 6: ", L.index(6))

# print("index objeto 45: ", L.index(45)) # erro

L.pop(3)
print(L)

L.remove(6)
print(L)

A = [22, 32, 42]
print(A)

L.extend(A)
print(L)

L.reverse()
print(L)

L.reverse()
print(L)

L.sort()
print(L)

L.sort(reverse=True)
print(L)

L.clear()

print("lista após o clear: ", L)

L = ["dado", "uva", "caixa", "lata", "casa"]

print(L.sort())

L = [23, 7.7, 3.9, 3, 35, "txt", "3em1"]

# L.sort() # erro





