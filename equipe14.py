import numpy as np
from math import e
import matplotlib.pyplot as plt
from suiteSn import suiteSn

equipe = 14

a = np.full((6, 1), 1)
print(a)

b = np.arange(1, 7)

c = a.reshape(1, 6)

d = equipe * c

I = np.identity(6)

J = np.full((6, 6), 1)

K = np.diag(b)

L = 55 * I - J + 2 * np.dot(a, c)

M = K.copy()
M[:, 0] = a.flatten()

dd = np.linalg.det(M)

x = np.linalg.solve(M, a)

M_transpose = M.T
N = np.linalg.solve(M, M_transpose)
