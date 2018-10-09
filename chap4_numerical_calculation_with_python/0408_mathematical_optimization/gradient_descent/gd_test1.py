#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import gd
import importlib; importlib.reload(gd)


def f(x_vec):
    """
    This function is 2-variable-function.
    :param x_vec:
    :return: scholar
    """
    x1 = x_vec[0]
    x2 = x_vec[1]
    return 5*x1**2 - 6*x1*x2 + 3*x2**2 + 6*x1 - 6*x2


def df(x_vec):
    """
    This function calculate grad f.
    :param x_vec: 2-dim vector
    :return: 2-dim vector(grad f = [af/ax1, af/ax2])
    """
    x1 = x_vec[0]
    x2 = x_vec[1]
    return np.array([10*x1 - 6*x2 + 6, -6*x1 + 6*x2 - 6])


def mesh(x_range: list, y_range: list, fxy: "func obj"):
    xstart, xstop = x_range
    ystart, ystop = y_range
    x = np.linspace(start=xstart, stop=xstop, num=1000)
    y = np.linspace(start=ystart, stop=ystop, num=1000)
    xmesh, ymesh = np.meshgrid(x, y)
    x_vec = np.vstack([xmesh.ravel(), ymesh.ravel()])
    z = fxy(x_vec).reshape(xmesh.shape)
    return xmesh, ymesh, z


if __name__ == '__main__':
    # solve
    algo = gd.GradientDescent(f, df)
    initial = np.array([1, 1])
    algo.solve(initial)
    
    # plot alpha = 0.01
    x_range, y_range = [-2, 2], [-2, 2]
    xmesh, ymesh, z = mesh(x_range, y_range, fxy=f)
    levels = [-3, -2.9, -2.8, -2.6, -2.4,
              -2.2, -2, -1, 0, 1, 2, 3, 4]
    fig, ax = plt.subplots(1, 1)
    ax.scatter(initial[0], initial[1], marker="o", s=20)
    ax.plot(algo.path[:, 0], algo.path[:, 1], ls="-", color="k")
    map_ax = ax.contour(xmesh, ymesh, z, linestyles="dotted", colors="b", levels=levels)  # cmap="jet"
    # config
    ax.set_title("contour_gradient_descent\n$f(x, y) = 5x^2 - 6xy + 3y^2 + 6x - 6y$")
    ax.set(xlabel="x", ylabel="y")
    # save
    fig.savefig("../../output/implement_gradient_descent_1.png")
    plt.close()
