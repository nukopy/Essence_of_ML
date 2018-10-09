#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cvxopt
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.axes_grid1 import make_axes_locatable


def mesh(x_range: list, y_range: list, fxy: "func obj"):
    xstart, xstop = x_range
    ystart, ystop = y_range
    x = np.linspace(start=xstart, stop=xstop, num=1000)
    y = np.linspace(start=ystart, stop=ystop, num=1000)
    xmesh, ymesh = np.meshgrid(x, y)
    z = fxy(xmesh.ravel(), ymesh.ravel()).reshape(xmesh.shape)
    return xmesh, ymesh, z


def fxy(x, y):
    return 5*x**2 - 6*x*y + 3*y**2 + 6*x - 6*y
    

if __name__ == '__main__':
    x_range = [-3, 3]
    y_range = [-2, 4]
    xmesh, ymesh, z = mesh(x_range, y_range, fxy)

    # plot
    # imshow
    fig, axes = plt.subplots(1, 2)  # (width, height)
    img = axes[0].imshow(z, vmin=z.min(), vmax=z.max(),
                         origin="lower", cmap=cm.jet)  # cmap="jet"
    axes[0].set_title("img_gradient_descent\n$f(x, y) = 5x^2 - 6xy + 3y^2 + 6x - 6y$")
    # colorbar config
    divider = make_axes_locatable(axes[0])
    cax = divider.append_axes("right", "5%", pad="3%")
    plt.colorbar(mappable=img, ax=axes[0], cax=cax)

    # contour
    levels = [-2, 0, 2, 4, 6]
    ax = axes[1].contour(xmesh, ymesh, z, levels=levels,  cmap=cm.jet)  # cmap="jet"
    axes[1].set_title("contour_gradient_descent\n$f(x, y) = 5x^2 - 6xy + 3y^2 + 6x - 6y$")
    # colorbar config
    divider = make_axes_locatable(axes[1])
    cax = divider.append_axes("right", "5%", pad="3%")
    plt.colorbar(mappable=ax, ax=axes[1], cax=cax)

    # save
    fig.tight_layout()
    fig.savefig("../../output/gradient_descent.png", dpi=200)
    plt.close(fig)
