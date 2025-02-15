a, b, c = 10, 15, 20

print("a: ", a)
print("b: ", b)
print("c: ", c)

d, e = a*2, b*3

print("d: ", d)
print("e: ", e)

x = 5
x, y = 10, x*3

print("x: ", x)
print("y: ", y)

L, m = [3, 6, 9], 14
print("L: ", L)
print("m: ", m)

# a, b, c = 2, 4, 6, 8 # erro

a, b = 17, -9
print("a: {}, b: {}".format(a, b))
print("invertendo a, b...")
a, b = b, a
print("a: {}, b: {}".format(a, b))


