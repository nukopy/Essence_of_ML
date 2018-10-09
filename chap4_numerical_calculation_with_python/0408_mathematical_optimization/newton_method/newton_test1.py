#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import importlib;
import newton; importlib.reload(newton)


def f1(x, y):
    return x**3 - 2*y


def f2(x, y):
    return x**2 + y**2 - 1


def f(xy_vec):
    """
    :param xy_vec: nd-array.shape(2, 1)
    :return: f(xy_vec)
    """
    x = xy_vec[0][0]
    y = xy_vec[1][0]
    return np.array([f1(x, y), f2(x, y)])


def df(xy_vec):
    """
    :param xy_vec: nd-array.shape(2, 1)
    :return:
    """
    x = xy_vec[0][0]
    y = xy_vec[1][0]
    # partial derivative
    df1dx = lambda x, y: 3*x**2
    df1dy = lambda x, y: -2  # constant
    df2dx = lambda x, y: 2*x
    df2dy = lambda x, y: 2*y
    # jacobi matrix
    j_11, j_12, j_21, j_22 = df1dx(x, y), df1dy(x, y), \
                             df2dx(x, y), df2dy(x, y)
    jacob = np.array([[j_11, j_12],
                      [j_21, j_22]])
    return jacob


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
    # constant
    x_range, y_range = [-3, 3], [-3, 3]
    xmesh, ymesh, z1 = mesh(x_range, y_range, fxy=f1)
    _, _, z2 = mesh(x_range, y_range, fxy=f2)
    
    # plot f1, f2
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111, projection="3d")
    map_ax = ax.plot_wireframe(xmesh, ymesh, z1, color="r", alpha=0.2)
    ax.plot_wireframe(xmesh, ymesh, z2, color="b", alpha=0.2)
    ax.plot_surface(xmesh, ymesh, np.zeros_like(xmesh), edgecolor="none", alpha=0.7)
    # contour
    fig_cont = plt.figure(figsize=(5, 6))
    ax_cont = fig_cont.subplots()
    CS = ax_cont.contour(xmesh, ymesh, z1, levels=[0],
                         colors="r", alpha=0.5, label="$f1(x, y) = x^3 - 2y$")
    ax_cont.clabel(CS=CS, inline=1, fmt="%d", fontsize=10)
    CS = ax_cont.contour(xmesh, ymesh, z2, levels=[0],
                         colors="b", alpha=0.5, label="$f2(x, y) = x^2 +2y - 1$")
    ax_cont.clabel(CS=CS, inline=1, fmt="%d", fontsize=10)
    ax_cont.legend()
    
    # calculation
    solver = newton.Newton(f, df)
    initial = [np.array([1, 1]),
               np.array([-1, -1]),
               np.array([1, -1])]
    markers = "ox^"
    for x0, marker in zip(initial, markers):
        sol = solver.solve(x0)
        ax.scatter(xs=solver.path_[:, 0], ys=solver.path_[:, 1],
                   zs=f1(solver.path_[:, 0], solver.path_[:, 1]),
                   label="x0 = ({}, {})".format(x0[0], x0[1]),
                   marker=marker, s=10, alpha=0.5)
        ax_cont.scatter(x=solver.path_[:, 0], y=solver.path_[:, 1],
                        marker=marker, s=20, alpha=0.5)
        ax_cont.set(xlabel="x", ylabel="y",
                    xlim=x_range, ylim=y_range,
                    title="contour_plot\n"
                          "$f1(x, y) = x^3 - 2y$\n"
                          "$f2(x, y) = x^2 +2y - 1$")
    
        # convergence
        fig_conv, ax_conv = plt.subplots()
        ax_conv.plot(f1(solver.path_[:, 0], solver.path_[:, 1]))
        ax_conv.set(xlabel="steps", ylabel="optimal value",
                    title="convergence_(x, y) = ({}, {})".format(x0[0], x0[1]))
        fig_conv.tight_layout()
        fig_conv.savefig("../../output/newton/convergence_xy{}_{}".format(x0[0], x0[1]))
        plt.close(fig_conv)
    fig_cont.savefig("../../output/newton/contour_f1f2.png", dpi=200)
    plt.close(fig_cont)
    
    # config
    ax.legend()
    ax.set(xlabel="x", ylabel="y", zlabel="f(x, y)",
           xlim=x_range, ylim=y_range, zlim=[-10, 10])
    ax.set_title(label="$f1(x, y) = x^3 - 2y$\n"
                       "$f2(x, y) = x^2 +2y - 1$")

    # save
    for angle in range(0, 360, 30):
        ax.view_init(5, angle)
        fig.savefig("../../output/newton/newton_method_{}.png".format(angle), dpi=200)
    plt.close()
