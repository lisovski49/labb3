import pandas as pd
import matplotlib.pyplot as plt
# 1. Импортировать датасет.
data = pd.read_csv('price_prepared.csv')

# 2. Взять 1000 значений из выбранного датасета.
data = data.sample(n=1000, random_state=42)

# 3. Проверить данные на пропуски.
missing_values = data.isnull().sum()
print(f'Пропуски в данных:')
print(missing_values)

# 4. Проверить на нормальность распределения и выбросы с помощью боксплотов и гистограмм
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
data['Square'].plot(kind='box', logy=True)
plt.title('Боксплот (логарифмическая шкала)')

plt.subplot(1, 2, 2)
data['Square'].plot(kind='hist', bins=30, logy=True)
plt.title('Гистограмма (логарифмическая шкала)')
plt.show()

# 5. Заполнить пропуски и обработать аномальные значения.
numeric_columns = ['Square', 'LifeSquare', 'KitchenSquare', 'Healthcare_1']
data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].mean())
data = data[(data['Square'] > 20) & (data['Square'] < 200)]

# 6. Определить сколько в выборке 1, 2, 3 комнатных квартир.
room_counts = data['Rooms'].value_counts()
print('Количество квартир по количеству комнат:')
print(room_counts)

# 7. Построить сводную таблицу.
pivot_table = data.pivot_table(index='DistrictId', columns='Rooms', values='Id', aggfunc='count')
print("Сводная таблица:")
print(pivot_table)

# 8. Сохранить обработанный массив без выбросов и пропусков в файл "surname.csv".
data.to_csv("surname.csv", index=False)