#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return (x**2 + y**2) / 4


if __name__ == '__main__':
    x = np.linspace(-5, 5, 300)
    y = np.linspace(-5, 5, 300)
    xmesh, ymesh = np.meshgrid(x, y)
    z = f(xmesh.ravel(), ymesh.ravel()).reshape(xmesh.shape)
    
    # plot
    fig, ax = plt.subplots()
    levels = [1, 2, 3, 4, 5]
    plt.subplot(1, 1, 1)  # designate subplot
    plt.contour(x, y, z, levels=levels, colors="b")
    fig.savefig("../output/contour_plot.png")
    plt.show()  # must execute after savefig
