import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from scipy import linalg


class LinearRegression:
    def __init__(self):
        self.w_ = None

    def fit(self, X, t):
        """
        y = Xtil*w (X: n x d matrix, w: d x 1 vector, y: n x 1 vector)
        E(w) = ||y - Xtil*w||^2
        w = (X~^T * X)
        """

        Xtil = np.concatenate([np.ones(shape=(X.shape[0], 1)), X], axis=1)
        A = np.dot(Xtil.T, Xtil)
        b = np.dot(Xtil.T, t)
        self.w_ = linalg.solve(A, b)  # solve A*w_ = b

    def predict(self, X):
        if X.ndim == 1:
            X = X.reshape(1, -1)
        # MUST be np.ones().ndim = 2
        Xtil = np.concatenate([np.ones(shape=(X.shape[0], 1)), X], axis=1)
        return np.dot(Xtil, self.w_)


if __name__ == "__main__":
    # const
    n = 100
    scale = 10

    # data
    np.random.seed(0)
    X = np.random.random((n, 2)) * scale
    w0, w1, w2 = 1, 2, 3
    error = np.random.randn(n)
    y = w0 + w1 * X[:, 0] + w2 * X[:, 1] + error

    # model
    model = LinearRegression()

    # fitting
    model.fit(X, y)
    print('Regression-Coefficients:\n{}\n'.format(model.w_))
    print('Prediction of (x1, x2) = (1, 1):\n{}'.format(
        model.predict(np.array([1, 1]))))

    # plot
    xmesh, ymesh = np.meshgrid(
        np.linspace(0, scale, 20),
        np.linspace(0, scale, 20)
    )
    zmesh = (
        model.w_[0] + model.w_[1]*xmesh.ravel() + model.w_[2]*ymesh.ravel()
    ).reshape(xmesh.shape)  # values of prediction

    # fig, ax = plt.subplots(nrows=1, ncols=1)
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(X[:, 0], X[:, 1], y, color='k')
    ax.plot_wireframe(xmesh, ymesh, zmesh, color='r')

    fig.savefig('output/linear_reg.png', dpi=200)
