import numpy as np
from math import e
import matplotlib.pyplot as plt
# from suiteSn import suiteSn

#a, le vecteur colonne de longueur 6 dont toutes les composantes valent 1.
a = np.full((6, 1), 1)

#b, le vecteur ligne de longueur 6 dont les composantes valent 1, 2, ..., 6 (en uneseule ligne).
b = np.arange(1, 7)


#c, le vecteur ligne de longueur 6 dont toutes les composantes valent 1. On obtiendra c à partir de a grâce à la transposition
c = a.reshape(1, 6)
# print(c)

d = equipe_num * c

#I, matrice identité de taille 6 × 6.
I = np.identity(6)
print(I)

#J, matrice de taille 6 × 6 dont toutes les composantes valent 1.
J = np.full((6, 6), 1)
print(J)

#K, la matrice de taille 6 × 6 dont la diagonale est le vecteur b
K = np.diag(b)
print(K)

#L, la matrice de taille 6 × 6
L = 55 * I - J + 2 * np.dot(a, c)
print(L)

#M, matrice obtenue en remplaçant la 1ère colonne de K par a.
M = K.copy()
M[:, 0] = a.flatten()

dd = np.linalg.det(M)

x = np.linalg.solve(M, a)

M_transpose = M.T
N = np.linalg.solve(M, M_transpose)


print(a, b, c)