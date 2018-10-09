#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


def newton1dim(f, df, x0, eps=1e-10, max_iter=1000):
    x_k = x0
    iter_ = 0
    while True:
        x_new = x_k - f(x_k)/df(x_k)
        if abs(x_k - x_new) < eps:
            break
        x_k = x_new  # update
        iter_ += 1
        if iter == max_iter:
            break
    return x_new


def f(x):
    return x**3 - 5*x + 1


def df(x):
    return 3*x**2 - 5


if __name__ == '__main__':
    # calculation
    init = np.array([2, 0, -3])
    result = np.array([newton1dim(f, df, i) for i in init])
    
    # plot
    x = np.linspace(-3, 3)
    fig, ax = plt.subplots()
    ax.plot(x, f(x), color="r")
    ax.hlines(y=0, xmin=x.min(), xmax=x.max(), colors="k", linestyles="dotted")
    ax.scatter(result, f(result), marker="o", color="b", s=20)
    
    # config
    ax.set(title="newton_method\n$x^3 - 5x + 1$", xlabel="x", ylabel="y")
    # save
    fig.savefig("../../output/newton_method1.png", dpi=200)
    plt.close()
