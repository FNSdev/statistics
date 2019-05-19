import random
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


n = 30
a = -3
b = 9

X = []
Y = []

for i in range(n):
    x = round(random.uniform(a, b), 1)
    X.append(x)
    Y.append(abs(x))

for x, y in zip(X, Y):
    print(f'x = {x}, y = {y}')

Y = sorted(Y)
print(f'Вариационный ряд: \n{Y}')

def G(y):
    val = 0
    for elem in Y:
        val += np.heaviside(y - elem, 1)
    return val / n 

a = Y[0]
b = Y[-1]

f = plt.figure()
f1 = f.add_subplot('311')
f2 = f.add_subplot('312')
f3 = f.add_subplot('313')

space = np.arange(a - 5, b + 5, 0.01)
f1.plot(space, G(space), '.')
f1.set_xlim(a - 5, b + 5)

y = sp.symbols('y')
g1 = sp.lambdify(y, y / 6, 'numpy')
g2 = sp.lambdify(y, y / 12 + 0.25, 'numpy')

space1 = np.linspace(0, 3)
space2 = np.linspace(3, 9)

f2.plot([-5, 0], [0, 0])
f2.plot(space1, g1(space1))
f2.plot(space2, g2(space2))
f2.plot([9, 14], [1, 1])
f2.set_xlim(-5, 14)

f3.set_xlim(a - 5, b + 5)
f3.plot([-5, 0], [0, 0])
f3.plot(space1, g1(space1))
f3.plot(space2, g2(space2))
f3.plot([9, 14], [1, 1])
space = np.arange(a - 5, b + 5, 0.01)
f3.plot(space, G(space), '.')

plt.show()