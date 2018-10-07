#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


def softplus(x):
    """
    x >> 0, softplus(x) ~ x (approximate)
    """
    return np.log(1 + np.exp(x))


if __name__ == '__main__':
    print(softplus(-1))
    print(softplus(0))
    print(softplus(1000))
    
    # plot
    x = np.linspace(-10, 10, 1000)
    y = softplus(x)
    
    fig = plt.figure()
    ax = fig.gca()
    ax.plot(x, y, linewidth=5, label="$y = log(1 + e^x)$")
    ax.plot(x, x, color="k", linestyle="--", label="$y = x$")
    ax.legend()
    ax.set_aspect("equal", "datalim")
    ax.set(xlabel="x", ylabel="y", title="softplus_function")
    fig.savefig("../output/softplus_function.png")
