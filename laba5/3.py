import math
import numpy as np
import matplotlib.pyplot as plt

def calculate_f(x,a):
    return math.exp(x*a)-3.45*a
def generate_data():
    x=3.67
    a_values = np.arange(0,2.2,0.2)
    f_values = [calculate_f(x,a) for a in a_values]
    return a_values, f_values
def print_values(a_values,f_values):
    print("значение аргумента и функции")
    for a, f in zip(a_values,f_values):
        print(f"a = {a:.2f}, f = {f:.2f}")
    print()
def find_extremes(a_values,f_values):
    min_value =min(f_values)
    max_value=max(f_values)
    return min_value, max_value
def calculate_average(f_values):
    return sum(f_values)/len(f_values)
def plot_graph(a_values, f_values):
    plt.plot(a_values,f_values,'bo',label='f(x)',markersize=5)
    average_value=calculate_average(f_values)
    plt.axhline(y=average_value,color='red',linestyle='--',label='average')
    plt.xlabel('a')
    plt.ylabel('f(x)')
    plt.title('График функции f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

a_values, f_values = generate_data()
print_values(a_values,f_values)
min_value,max_value=find_extremes(a_values,f_values)
average_value=calculate_average(f_values)
sorted_values=sorted(f_values,reverse=(len(a_values)%2==0))

print(f"Наибольшее значение: {max_value:.2f}")
print(f"Наименьшее значение: {min_value:.2f}")
print(f"Среднее значение: {average_value:.2f}")
print(f"Количество элементов в массиве: {len(f_values)}")
print(f"Отсортированный массив: {sorted_values}")

plot_graph(a_values, f_values)