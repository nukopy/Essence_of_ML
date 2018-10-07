#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return (x ** 2 + y ** 2) / 4


if __name__ == '__main__':
    x = np.linspace(-5, 5, 300)
    y = np.linspace(-5, 5, 300)
    xmesh, ymesh = np.meshgrid(x, y)
    z = f(xmesh.ravel(), ymesh.ravel()).reshape(xmesh.shape)
    
    # plot
    fig, ax = plt.subplots()
    levels = [i for i in range(1, 6)]
    # prepare colors of which number is same as levels
    colors = [str(i) for i in np.linspace(0, 1, 4)]
    plt.subplot(1, 1, 1)  # designate subplot
    plt.contourf(x, y, z, levels=levels, colors=colors)
    fig.savefig("../output/contourf_plot.png")
    plt.show()  # must execute after savefig
