import random
import math
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from matplotlib import colors


n = 200
a = -3
b = 9

X = []
Y = []

for i in range(n):
    x = random.uniform(a, b)
    X.append(x)
    Y.append(abs(x))

Y = sorted(Y)
a = Y[0]
b = Y[-1]

M = int(math.sqrt(n) + 1 if n <= 100 else 3 * math.log10(n))
print(f'M = {M}')

delta_y = (b - a) / M

def count(l, r):
    cnt = 0
    for elem in Y:
        if l < elem and elem < r:
            cnt +=1
        elif l == elem or r == elem:
            cnt += 0.5
    return cnt

g = plt.figure()
g1 = g.add_subplot('231')
g2 = g.add_subplot('232')
g3 = g.add_subplot('233')
g4 = g.add_subplot('234')
g5 = g.add_subplot('235')

g1.set_title('Равноинтервальный метод')
g2.set_title('Равновероятностный метод')
g3.set_title('Равноинтервальный метод, plt.hist()')
g4.set_title('Полигон, равноинтервальный метод')
g5.set_title('Полигон, равновероятностный метод')

g1.set_ylim(bottom=0)
g2.set_ylim(bottom=0)

l = a
x = []
y = []
for i in range(M):
    r = l + delta_y

    cnt = count(l, r)
    
    h = cnt / (delta_y * n)
    g1.plot((l, r), (h, h), color='red')
    x.append((r + l) / 2)
    y.append(h)
    print(f'#{i} : l = {l}, r = {r}, h = {h}, count = {cnt}')

    l = r

g4.plot(x, y, color='red')
x.clear()
y.clear()


cnt = int(n / M)
l = a
for i in range(M):
    #r = (Y[(i + 1) * cnt - 1] + Y[(i + 1) * cnt]) / 2 if (i + 1) * cnt != len(Y) else Y[(i + 1) * cnt - 1]
    r = Y[(i + 1) * cnt - 1]
    delta = r - l    
    h = 1 / (delta * M)
    g2.plot((l, r), (h, h), color='green')
    x.append((r + l) / 2)
    y.append(h)

    print(f'#{i} : l = {l}, r = {r}, delta = {delta}, h = {h}, s = {delta * h}')

    l = r
    
g5.plot(x, y, color='green')
x.clear()
y.clear()

N, bins, patches = g3.hist(Y, bins=M, density=True)
fracs = N / N.max()
norm = colors.Normalize(fracs.min(), fracs.max())

for thisfrac, thispatch in zip(fracs, patches):
    color = plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)

g3.yaxis.set_major_formatter(PercentFormatter(xmax=1))

g1.plot((0, 3), (1 / 6, 1 / 6), color='black')
g1.plot((3, 9), (1 / 12, 1 / 12), color='black')
g1.set_ylim(0, 0.2)

g2.plot((0, 3), (1 / 6, 1 / 6), color='black')
g2.plot((3, 9), (1 / 12, 1 / 12), color='black')
g2.set_ylim(0, 0.2)

plt.show()

