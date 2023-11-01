import numpy as np
import matplotlib as plt

def func1(x,y):
    return np.power(x,0.25)-np.power(y,0.25)

def func2(x,y):
    return np.power(x,2)-np.power(y,2)
def func3(x,y):
    return 2*x+3*y
def func4(x,y):
    return np.power(x, 2) + np.power(y, 2)
def func5(x,y):
    return 2+2*x+2*y-np.power(x,2)-np.power(y,2)

x=np.linspace(-10,10,100)
y=np.linspace(-10,10,100)
X,Y= np.meshgrid(x,y)
