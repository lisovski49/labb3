import numpy as np
import matplotlib.pyplot as plt

def func1(x,y):
    return np.power(x, 0.25)+np.power(y, 0.25)
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

Z1=func1(X,Y)
Z2=func2(X,Y)
Z3=func3(X,Y)
Z4=func4(X,Y)
Z5=func5(X,Y)
fig=plt.figure()
#1
ax1=fig.add_subplot(231, projection='3d')
ax1.plot_surface(X,Y,Z1,cmap='plasma')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_title('z = x^0.25 + y^0.25')
#2
ax2 = fig.add_subplot(232, projection='3d')
ax2.plot_surface(X, Y, Z2, cmap='plasma')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.set_title('z = x^2 - y^2')
#3
ax3 = fig.add_subplot(233, projection='3d')
ax3.plot_surface(X, Y, Z3, cmap='plasma')
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_zlabel('Z')
ax3.set_title('z = 2x+3y')
#4
ax4 = fig.add_subplot(234, projection='3d')
ax4.plot_surface(X, Y, Z4, cmap='plasma')
ax4.set_xlabel('X')
ax4.set_ylabel('Y')
ax4.set_zlabel('Z')
ax4.set_title('z = x^2+y^2')
#5
ax5 = fig.add_subplot(235, projection='3d')
ax5.plot_surface(X, Y, Z5, cmap='plasma')
ax5.set_xlabel('X')
ax5.set_ylabel('Y')
ax5.set_zlabel('Z')
ax5.set_title('z = 2+2x+2y-x^2-y^2')

plt.tight_layout()
plt.show()
