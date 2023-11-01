import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('test.csv')
df = df.head(1000)
missing_values = df.isnull().sum()
plt.boxplot(df['DistrictId'].apply(np.log))
plt.xlabel('Cnjk,tw')
plt.ylabel('Значения (логарифмическая шкала)')
plt.title('Ящик с усами')
plt.show()

plt.hist(df['DistrictId'].apply(np.log))
plt.xlabel('Столбец')
plt.ylabel('Частота')
plt.title('Гистограмма')
plt.show()

df['DistrictId'].fillna(df['DistrictId'].mean(), inplace=True)
Q1 = df['DistrictId'].quantile(0.25)
Q3 = df['DistrictId'].quantile(0.75)
IQR = Q3 - Q1
df = df[(df['DistrictId'] >= (Q1 - 1.5 * IQR)) & (df['DistrictId'] <= (Q3 + 1.5 * IQR))]
df = df[np.abs(df['DistrictId'] - df['DistrictId'].mean()) <= 3 * df['DistrictId'].std()]
room_counts = df['DistrictId'].value_counts()
pivot_table = pd.pivot_table(df, values='количество', index='районы', columns='комнаты', aggfunc=len)
df.to_csv('surname.csv', index=False)