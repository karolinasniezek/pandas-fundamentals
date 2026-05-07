from unittest.mock import inplace

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("diagrams/workers.csv", sep=";")

ndf = df[df.isna().any(axis=1)]
print(ndf)

df['Brilliance'] = df['Brilliance'].fillna(333)
df['Creativity'] = df['Creativity'].fillna(33)

n1 = len(df)
ndf = df.dropna()
n2 = len(ndf)

print(ndf.to_string())
print('Deleted:', n1 - n2)