import numpy as np
from math import e
import matplotlib.pyplot as plt
from suiteSn import suiteSn

equipe = 14

#a, le vecteur colonne de longueur 6 dont toutes les composantes valent 1.
a = np.full((6, 1), 1)
print("a", a)

#b, le vecteur ligne de longueur 6 dont les composantes valent 1, 2, ..., 6 (en uneseule ligne).
b = np.arange(1, 7)
print("b", b)


#c, le vecteur ligne de longueur 6 dont toutes les composantes valent 1. On obtiendra c à partir de a grâce à la transposition
c = a.reshape(1, 6)
print("c", c)

#d, le vecteur ligne de longueur 6 dont toutes les composantes valent le numéro de votre équipe. On obtiendra d en multipliant c par le numéro de votre équipe.
d = equipe * c
print("d", d)

#I, matrice identité de taille 6 × 6.
I = np.identity(6)
print('I', I)

#J, matrice de taille 6 × 6 dont toutes les composantes valent 1.
J = np.full((6, 6), 1)
print('J', J)

#K, la matrice de taille 6 × 6 dont la diagonale est le vecteur b
K = np.diag(b)
print('K', K)

#L, la matrice de taille 6 × 6
L = 55 * I - J + 2 * np.dot(a, c)
print('L', L)

#M, matrice obtenue en remplaçant la 1ère colonne de K par a.
M = K
M[:, 0] = a.reshape(1, 6)
print('M', M)

#dd, le déterminant de M (utiliser la commande np.linalg.det).
dd = np.linalg.det(M)
print("dd", dd)

#x, la solution de M x= a, sans calculer l'inverse de L 
x = np.linalg.solve(M, a)
print("x", x)
print(np.dot(M, x))

M_prime = M.T
N = np.dot(np.linalg.inv(M), M_prime)
print(np.dot(M, N)) 
print(M_prime)

plt.matshow(N)
plt.title('Matrice N')
plt.show()


def f(x) :
    f = -0.5*x**2 + np.exp(x) + np.sin(x)
    return f

x = np.linspace(0, 1, 101)

plt.plot(x, f(x))
plt.title('F(x)')
plt.show()


S19 = suiteSn(19)
#x_int = np.linspace(0, 19, 18)
plt.plot(S19)
plt.title('Intégrale (x**n)*(e**x) dx bornée en [0,1]')
plt.xlabel('Valeur de n')
plt.ylabel("Résultat de l'intégrale")
plt.show()

#Rapport mettre figures