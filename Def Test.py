import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv('C:/Users/Travvy/Desktop/Jupyter Notebook/AppleStore.csv')

x = data['prime_genre'].values
y = data['price'].values
i = 0
fin = np.array([])

for i in range(len(x)):
    gen = x[i]
    games = data[data['prime_genre'] == gen]
    fin = np.append(fin, np.mean(games['price']))

print(x[0])

plt.figure(figsize=(70, 40))
plt.bar(x, fin)

plt.show()