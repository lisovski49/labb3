import numpy as np
x=0.24
a=5.8
z=np.arctan(x**2)+np.cos(np.pi/2-a)**3/np.abs(x-a**(1/5))
print(z)

X=np.ones((12,3))
X[:,1]=np.arange(13,25)
X[:,2]=np.random.randint(60,83, size=(12))

Y=np.random.uniform(13.5,18.6,size=(12,1))

A=np.linalg.inv(X.T @ X) @ (X.T @ Y)

Y_predicted=X @ A

print("Вектор оценок A:")
print(A)
print("Результаты проверки:")
print(Y_predicted)
print("Исходные значения Y:")
print(Y)