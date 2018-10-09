#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cvxopt
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.axes_grid1 import make_axes_locatable

"""


# 3D-plot
Axes3D is not used explicitly,
but if you don't import it the Error " KeyError: '3d' " will be caused.

"""


def f(x, y, P_a, P_b, q_a, q_b):
    """
    :param x: int or float
    :param y: int or float
    :param P: ndarray, shape(2, 2) symmetric matrix
    :param q: ndarray, shape(2,)
    :return:
    """
    qp_std_form = 1/2 * (P_a*x**2 + 2*P_b*x + P_a*y**2) \
                  + (q_a*x + q_b*y)
    return qp_std_form


def min_max_norm(x: np.ndarray, axis=None):
    min = x.min(axis=axis)
    max = x.max(axis=axis)
    result = (x - min) / (max - min)
    return result


def quadratic_optimization(P: np.ndarray, q: np.ndarray):
    # minimize 1 / 2 * x ^ T * P * x + q ^ T * x
    P_mat = cvxopt.matrix(P)
    q_mat = cvxopt.matrix(q)
    sol_dic = cvxopt.solvers.qp(P=P_mat, q=q_mat)
    sol = np.array(sol_dic["x"])  # 2-dim vector
    value = np.array(sol_dic["primal objective"])
    print("--- optimal solution ---\n{}".format(sol))
    print("--- optimal value ---\n{}".format(value))
    return sol, value


if __name__ == '__main__':
    # Numpy ufunc
    num_argument = 6
    num_return = 1
    univ_f = np.frompyfunc(f, num_argument, num_return)
    
    # function f(x, y) calculation
    x = np.linspace(start=-5, stop=5, num=1000)
    y = np.linspace(start=-5, stop=5, num=1000)
    P = np.array([[2, 1], [1, 2]], dtype=np.float64)
    p_a, p_b = P[0, 0], P[0, 1]
    q = np.array([2, 4], dtype=np.float64)
    q_a, q_b = q[0], q[1]
    xmesh, ymesh = np.meshgrid(x, y)
    z = univ_f(xmesh.ravel(), ymesh.ravel(),
               p_a, p_b, q_a, q_b).reshape(xmesh.shape).astype(np.float64)
    
    # quadratic optimization
    sol, value = quadratic_optimization(P=P, q=q)
    
    # plot
    # 2d-plot
    fig1 = plt.figure(figsize=(8, 8))  # (width, height)
    ax1 = fig1.add_subplot(1, 1, 1)
    img = ax1.imshow(min_max_norm(z), cmap=cm.jet)  # cmap="jet"
    # text = "Optimal Solution\n(x, y) = ({x}, {y})\nf(x, y) = {z}".format(x=sol[0], y=sol[1], z=value)
    # ax1.text(sol[0], sol[1], s=text)
    ax1.set_title("$f(x, y) = x^2 + xy + y^2 + 2x + 4y$")
    # colorbar config
    divider = make_axes_locatable(ax1)
    cax = divider.append_axes("right", "5%", pad="3%")
    plt.colorbar(mappable=img, ax=ax1, cax=cax)
    # save
    fig1.savefig("../output/2d_quadratic_optimization.png", dpi=200)
    plt.close(fig1)
    
    # 3d-plot
    fig2 = plt.figure(figsize=(8, 8))
    ax2 = fig2.add_subplot(1, 1, 1, projection="3d")
    ax2.plot_surface(xmesh, ymesh, z, cmap=plt.cm.jet, alpha=0.5)
    ax2.set(xlabel="x", ylabel="y", zlabel="f(x, y)")
    ax2.set_title(label="$f(x, y) = x^2 + xy + y^2 + 2x + 4y$")
    # plot minimum value
    ax2.plot(sol[0], sol[1], value, marker="o", markersize=8, color="r")
    # text = "Optimal Solution\n(x, y) = ({x}, {y})\nf(x, y) = {z}".format(x=sol[0], y=sol[1], z=value)
    # ax2.text(x=sol[0], y=sol[1], z=value, s=text)
    # plt.show()
    fig2.savefig("../output/3d_quadratic_optimization.png")
    plt.close(fig2)
