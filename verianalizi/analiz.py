import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
veri = pd.read_excel('dataset.xlsx')
veri.to_csv('datasset.csv', index=False)
print(veri.head())
sns.heatmap(veri.isnull(),cbar=False)

plt.figure(figsize=(10, 6))
sns.histplot(veri['SALDIRI_TİPİ'], kde=True)
plt.title('Saldırının Türü')
plt.xlabel('Saldırı')
plt.ylabel('Frekans')
plt.show()       