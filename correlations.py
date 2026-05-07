from unittest.mock import inplace

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# if user inputs
# X = list(map(float, input().split()))
# Y1 = list(map(float, input().split()))
# Y2 = list(map(float, input().split()))

X = [1, 2, 3, 4, 5]
Y1 = [1.1, 2, 3.1, 4, 5.1]
Y2 = [2, 3.9, 6.3, 7.8, 10]

npx = np.array(X)
npy1 = np.array(Y1)
npy2 = np.array(Y2)

Y1series = pd.Series(data=Y1, index=X)
Y2series = pd.Series(data=Y2, index=X)
correlation = Y1series.corr(Y2series)

plt.plot(npx, npy1, color="red", label="Set 1", marker="o")
plt.plot(npx, npy2, color="green", label="Set 2", marker="o")

plt.xlabel("X")
plt.xlabel("Y")
plt.title(f"Two sets - correlation: {correlation:.3f}")
plt.legend()
plt.savefig("figures/correlation-figure.png")
plt.show()