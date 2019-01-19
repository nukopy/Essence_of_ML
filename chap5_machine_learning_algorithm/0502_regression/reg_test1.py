import linearreg
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

"""Linear Regression
y = w0 + w1*x1 + w2*x2
"""

n = 100
scale = 10
np.random.seed(0)
X = np.random.random((n, 2)) * scale
w0, w1, w2 = 1, 2, 3
error = np.random.randn(n)
y = w0 + w1 * X[:, 0] + w2 * X[:, 1] + error

model = linearreg.LinearRegression()
model.fit(X, y)
print('regression-coefficient\n{}'.format(model.w_))
print('-'*20)
print('prediction of (x1, x2) = (1, 1)\n{}'.format(model.predict([1, 1])))
print('-'*20)

# plot
xmesh, ymesh = np.meshgrid(
    np.linspace(0, scale, 20),
    np.linspace(0, scale, 20)
)
zmesh = (
    model.w_[0] + model.w_[1]*xmesh.ravel() + model.w_[2]*ymesh.ravel()
).reshape(xmesh.shape)

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 8))
ax.scatter(X[:, 0], X[:, 1], y, color='k')
ax.plot_wireframe(xmesh, ymesh, zmesh, color='r')
fig.savefig('output/reg_test1.py')
