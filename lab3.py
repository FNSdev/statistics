import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2 
import random
import math

n = 200
a = -3
b = 9

X = []
Y = []

def generate(n):
    X.clear()
    Y.clear()
    for i in range(n):
        x = random.uniform(a, b)
        X.append(x)
        Y.append(abs(x))

def F(x):
    if x < 0:
        return 0
    elif x < 3:
        return x / 6
    elif x < 9:
        return x / 12 + 0.25
    else:
        return 1

def G(y):
    val = 0
    for elem in Y:
        val += np.heaviside(y - elem, 1)
    return val / n

generate(n)
Y = sorted(Y)
a = Y[0]
b = Y[-1]

M = int(math.log2(n)) + 1
cnt = int(n / M)
v_i = cnt
l = a
chi2_test = 0
sanity_check = 0
for i in range(M):
    r = Y[(i + 1) * cnt - 1]
    delta = r - l    
    h = 1 / (delta * M)

    p_i_theory = F(r) - F(l)
    sanity_check += p_i_theory
    chi2_test += (v_i - n * p_i_theory) ** 2 / (n * p_i_theory)

    l = r

alpha = 0.01
chi2_critical = chi2.isf(q=alpha, df=(M - 1))
print('-' * 20)
print(f'M = {M}, count = {cnt}')
print(f'sanity check: {sanity_check}')
print(f'chi2 = {chi2_test}, hi_table (for alpha = {alpha}, k = {M - 1}) = {chi2_critical}')
print('accept' if chi2_test < chi2_critical else 'decline')

n = 30
generate(n)
Y = sorted(Y)
a = Y[0]
b = Y[-1]

#d = max(max([i / n - F(Y[i]) for i in range(n)]), max([F(Y[i]) - (i - 1) / n]))
d = max(abs(F(Y[i]) - G(Y[i])) for i in range(n))
l = math.sqrt(n) * d
critical_l = 1.63
print('-' * 20)
print(f'd = {d}, lambda = {l}, critical lambda = {critical_l}')
print('accept' if l < critical_l else 'decline')

n = 50
generate(n)
Y = sorted(Y)
a = Y[0]
b = Y[-1]

omega2_critical = 0.744
#omega2 = sum((F(Y[i]) - (i - 0.5) / n) ** 2 for i in range(n)) + 1 / (12 * n)
omega2 = sum((F(Y[i]) - G(Y[i])) ** 2 for i in range(n)) + 1 / (12 * n)
print('-' * 20)
print(f'omega2 = {omega2}, critical omega2 = {omega2_critical}')
print('accept' if omega2 < omega2_critical else 'decline')