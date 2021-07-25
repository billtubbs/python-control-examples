# Test Python-control function

import numpy as np
from control import ss, hinfsyn


# Load state-space matrices
A = np.genfromtxt('data/A.csv', dtype=float, delimiter=',')
B = np.genfromtxt('data/B.csv', dtype=float, delimiter=',')
C = np.genfromtxt('data/C.csv', dtype=float, delimiter=',')
D = np.genfromtxt('data/D.csv', dtype=float, delimiter=',')
p = ss(A, B, C, D)

n = A.shape[0]
assert(A.shape == (n, n))
nu = B.shape[1]
ny = C.shape[0]

print(f"Number of inputs: {nu}")
print(f"Number of outputs: {ny}")
print(f"Number of states: {n}")

nmeas = 2
ncon = 1

k, cl, gam, rcond = hinfsyn(p, nmeas, ncon)

# Load state-space matrices of controller K produced
# by MATLAB's hinfsyn function
K1_A = np.genfromtxt('data/K1_A.csv', dtype=float, delimiter=',')
K1_B = np.genfromtxt('data/K1_B.csv', dtype=float, delimiter=',')
K1_C = np.genfromtxt('data/K1_C.csv', dtype=float, delimiter=',')
K1_D = np.genfromtxt('data/K1_D.csv', dtype=float, delimiter=',')

k1 = ss(K1_A, K1_B, K1_C, K1_D)





