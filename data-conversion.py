import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = {
    "extension": [403, 390, 490, 890],
    "income": [50000, 40000, 45000, 52000],
    "name": ['Andy', 'Yusuf', 'Eva', 'Anna']
}

df = pd.DataFrame(data)
print(df)
print(list(df.columns))
print((df.loc[0].to_string()))
print((df.loc[len(df) - 1]).to_string())
