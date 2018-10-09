#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
# import importlib;


def f(x, y):
    return 5*x**2 + 6*x*y + 5*y**2 - 26*x - 26*y


def g(x, y):
    return x**2 + y**2 - 4


def mesh(x_range: list, y_range: list, fxy: "func obj"):
    xstart, xstop = x_range
    ystart, ystop = y_range
    x = np.linspace(start=xstart, stop=xstop, num=1000)
    y = np.linspace(start=ystart, stop=ystop, num=1000)
    xmesh, ymesh = np.meshgrid(x, y)
    # x_vec = np.vstack([xmesh.ravel(), ymesh.ravel()])
    z = fxy(xmesh.ravel(), ymesh.ravel()).reshape(xmesh.shape)
    return xmesh, ymesh, z


if __name__ == '__main__':
    x_range = [-5, 5]
    y_range = [-5, 5]
    xmesh, ymesh, z1 = mesh(x_range, y_range, f)
    _, _, z2 = mesh(x_range, y_range, g)
    
    # plot f1, f2
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111, projection="3d")
    map_ax = ax.plot_surface(xmesh, ymesh, z1, cmap=cm.jet, alpha=0.2)
    ax.plot_surface(xmesh, ymesh, z2, cmap=cm.viridis, alpha=0.2)
    ax.plot_surface(xmesh, ymesh, np.zeros_like(xmesh), edgecolor="none", alpha=0.7)
    ax.set(xlabel="x", ylabel="y", zlim=[-50, 25],
           title="$f1(x, y) = 5x^2 + 6xy + 5y^2 - 26x - 26y$\n"
                 "$f2(x, y) = x^2 + y^2 - 4$")

    # contour
    fig_cont = plt.figure(figsize=(5, 6))
    ax_cont = fig_cont.subplots()
    CS = ax_cont.contour(xmesh, ymesh, z1, levels=np.linspace(-40, 20, 5),
                         colors="r", alpha=0.5)
    ax_cont.clabel(CS=CS, inline=1, fmt="%d", fontsize=10)
    CS = ax_cont.contour(xmesh, ymesh, z2, levels=[0],
                         colors="b", alpha=0.5)
    ax_cont.clabel(CS=CS, inline=1, fmt="%d", fontsize=10)
    ax_cont.set(xlabel="x", ylabel="y",
                title="$f1(x, y) = 5x^2 + 6xy + 5y^2 - 26x - 26y$\n"
                      "$f2(x, y) = x^2 + y^2 - 4$")
    
    # save
    for angle in range(0, 120, 15):
        ax.view_init(10, angle)
        fig.savefig("../../output/laglange/3d_sur_f1_f2_{}.png".format(angle), dpi=200)
    fig_cont.savefig("../../output/laglange/contour_f1_f2.png", dpi=200)
    plt.close(fig)
    plt.close(fig_cont)
