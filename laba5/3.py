import math
import numpy as np
import matplotlib.pyplot as plt

def calculate_f(x,a):
    return math.exp(a*x)-3,45*a
def generate_data():
    x=3.67
    a_values = np.arange(0,2.2,0.2)
    f_values = [calculate_f(x,a) for a in a_values]
    return a_values, f_values
def print_values(a_values,f_values):
    print("значение аргумента и функции")
    for a, f in zip(a_values,f_values):
        print(f"a={a:.2f}, f = {f:.2f}")
    print()
def find_extremes(a_values,f_values):
    min_value =min(f_values)
    max_value=max(f_values)
    return min_value, max_value
def calculate_average(f_values):
    return sum(f_values)/len(f_values)
