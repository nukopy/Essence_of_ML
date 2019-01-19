import numpy as np
import matplotlib.pyplot as plt


def reg1dim(x: np.ndarray, y: np.ndarray):
    """
    y = b1*a
    """
    a = np.dot(x, y) / (x**2).sum()
    return a


if __name__ == "__main__":
    x = np.array([1, 2, 4, 6, 7])
    y = np.array([1, 3, 3, 5, 4])
    xmax = x.max()

    # fit
    a = reg1dim(x, y)  # a = x^T * y / ||x||^2
    fig, ax = plt.subplots(nrows=1, ncols=1)
    ax.scatter(x, y, color='k')
    ax.plot([0, xmax], [0, a*xmax], color='b')  # plot reg-line
    fig.savefig('output/reg1dim.png', dpi=200)
