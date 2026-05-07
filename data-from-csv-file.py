import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('diagrams/diagram.csv')
print(df)

columnsList = list(df.columns)

for c in columnsList:
    D = df[c]
    a = sum(D) / len(D)
    print(f"{c}: Max={max(D)} Min={min(D)} Avg={a: .5}")
