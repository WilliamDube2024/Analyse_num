import numpy as np
from math import e

def suiteSn(n):
    S = np.array([e-1])
    for i in range(1, n+1):
        Sn = e - i*S[-1]
        S = np.append(S, Sn)
    return S

