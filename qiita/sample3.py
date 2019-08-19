import numpy as np
import scipy.ndimage.filters
import matplotlib.pyplot as plt

lap = lambda X: scipy.ndimage.filters.laplace(X)
def update(U, V, Du=0.2, Dv=1.8):
    return (Du*lap(U) + U*(1.-U*U) - V,
            Dv*lap(V) + 3.*U - 2.*V)

size = (64, 64)
U = np.random.random(size)
V = np.random.random(size)
dt = 0.1

fig = plt.figure()
ax = fig.add_subplot(111)
img = ax.imshow(U, interpolation="nearest", cmap=plt.cm.gray)

view_interval = 10
for i in range(10000):
    dU, dV = update(U, V)
    U += dt*dU
    V += dt*dV
    if i % view_interval == 0:
        img.set_data(U)
        ax.set_title("t = {}".format(i))
        plt.pause(0.01)
plt.show()
