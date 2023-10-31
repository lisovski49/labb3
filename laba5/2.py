import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


dataset =pd.read_csv("test.csv")
sample= dataset.sample(n=1000)

missing_values =sample.isnull().sum()
print("Пропущенные значения")
print(missing_values)

for column in sample.select_dtypes(include=np.number):
    plt.figure(figsize=(8,4))
    plt.subplot(1,2,1)
    sample.boxplot(column=column,vert=False)
    plt.subplot(1,2,2)
    np.log1p(sample[column]).hist()
    plt.xlabel(column)
    plt.show()

sample=sample.fillna(sample.mean())
room_counts=sample['Количество комнат'].value_counts()
print("Количество комнат:")
print(room_counts)
pivot_table=pd.pivot_table(sample,index='район',columns='Количество комнат',aggfunc='size',fill_value=0)
print("Сводная таблица:")
print(pivot_table)

sample.to_csv("surname.csv",index=False)
print("Файл 'surname.csv' сохранен.")