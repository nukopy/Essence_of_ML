import numpy as np
import matplotlib.pyplot as plt


def reg1dim2(x, y):
    """
    y = b0 + b1*a
    """
    n = len(x)
    numer = n * np.dot(x, y) - x.sum()*y.sum()  # numerator / denominator
    denom = n * (x**2).sum() - (x.sum())**2
    a = numer / denom
    b = (y.sum() - a*x.sum()) / n
    return a, b


if __name__ == "__main__":
    x = np.array([1, 2, 4, 6, 7])
    y = np.array([1, 3, 3, 5, 4])
    xmax = x.max()

    # fit
    a, b = reg1dim2(x, y)
    fig, ax = plt.subplots(nrows=1, ncols=1)
    ax.scatter(x, y, color='k')
    ax.plot([0, xmax], [b, a*xmax + b], color='b')  # plot reg-line
    fig.savefig('output/reg1dim2.png', dpi=200)
