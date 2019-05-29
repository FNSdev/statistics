import numpy as np
from scipy import stats
import random
import math
import matplotlib.pyplot as plt


n = 20
A = -3
B = 9

X = []
Y = []

LEVELS = [0.99, 0.95, 0.90, 0.85, 0.7]
N = [20, 30, 50, 70, 100, 150]

theory_expected_value = 3.75
theory_dispersion = 5.9375

def g(y):
    if y < 0:
        return 0
    if y < 3:
        return 1 / 6
    if y < 9:
        return 1 / 12
    return 0


def generate(n):
    X.clear()
    Y.clear()
    for i in range(n):
        x = random.uniform(A, B)
        X.append(x)
        Y.append(abs(x))


def get_student_epsilon(dispersion, alpha, n):
    t = stats.t.isf(alpha / 2, n - 1)
    eps = t * np.sqrt(dispersion / n)
    return eps


def get_normal_epsilon(dispersion, alpha, n):
    z = stats.norm.isf(alpha / 2)
    eps = z * np.sqrt(dispersion / n)
    return eps

for n in N:
    generate(n)
    Y = sorted(Y)
    a = Y[0]
    b = Y[-1]

    expected_value = np.mean(Y)
    dispersion = 1 / (n - 1) * np.sum([(y - expected_value) ** 2 for y in Y])

    print(f'Expected value : {expected_value}, dispersion : {dispersion}')
    points_x_1 = []
    points_y_1 = []
    points_y_2 = []
    for level in LEVELS:
        eps = get_student_epsilon(dispersion, 1 - level, n)
        print(f'alpha = {1 - level}, (student) epsilon = {eps}')
        points_x_1.append(level)
        points_y_1.append(eps * 2)
        print(f'Interval (student): {expected_value - eps} <= M <= {expected_value + eps}')

        eps = get_normal_epsilon(dispersion, 1 - level, n)
        print(f'alpha = {1 - level}, (normal) epsilon = {eps}')
        points_y_2.append(eps * 2)
        print(f'Interval (normal): {theory_expected_value - eps} <= M <= {theory_expected_value + eps}')

        print('-' * 40)
    plt.plot(points_x_1, points_y_1, '.', label='Student')
    plt.plot(points_x_1, points_y_2, '.', label='Normal')
    plt.legend()
    plt.show()
    print('#' * 40)
    print('-' * 40)

    print(f'Theoretical expected value : {theory_expected_value}, theoretical dispersion : {theory_dispersion}')
    