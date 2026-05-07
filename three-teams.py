from unittest.mock import inplace

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


np.random.seed(seed=1)
df = pd.DataFrame(np.random.rand(50, 6),
                  columns=['x1', 'y1', 'x2', 'y2', 'x3', 'y3'])

team1 = df.plot.scatter(x="x1", y="y1", color="red", label="Team 1")
team1AndTeam2 = df.plot.scatter(x="x2", y="y2", color="green", label="Team 2",
                                ax=team1)

team3 = df.plot.scatter(x="x3", y="y3", color="orange", label="Team 3",
                                ax=team1AndTeam2)

plt.xlabel("X coord")
plt.ylabel("Y coord")
plt.title("Three teams")
plt.savefig("figure.png")
plt.show()