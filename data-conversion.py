import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

N = int(input())
L = [x * x for x in range(2*N + 1)]
C = [x*x*x*x for x in range(-N, N + 1)]
Lab = [chr(65 +  x) for x in range(2*N + 1)]

P = pd.Series(L, index=Lab)
Q = pd.Series(C, index=Lab)

for c in P.index:
    print(c, P[c], Q[c])


Gt = P.gt(Q)
print(Gt)




