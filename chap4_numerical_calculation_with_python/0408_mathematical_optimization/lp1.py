#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from scipy import optimize

"""scipy.optimize.linprog
scipy.optimize.linprog(c, A_ub=None, b_ub=None,
                       A_eq=None, b_eq=None, bounds=None,
                       method='simplex', callback=None, options=None)
                       
Minimize a linear objective function
subject to linear equality and inequality constraints.
Linear Programming is intended to solve the following problem form:
# Minimize: c^T * x(objective function)
# Subject to: A_ub * x <= b_ub
              A_eq * x <= b_eq

# CAUTION
scipy.optimize.linprog is implemented for a "minimization problem".
Therefore, when you wanna solve a maximization problem,
you must negate an objective function.
"""

# minimize
c = -1 * np.array([3, 4], dtype=np.float64)  # negate objective function
G = np.array([[1, 4], [2, 3], [2, 1]], dtype=np.float64)
h = np.array([1700, 1400, 1000], dtype=np.float64)
sol = optimize.linprog(c=c, A_ub=G, b_ub=h, bounds=(0, None))
print(sol.x)
print(sol.fun)


"""
c1 = np.array([3, 4])
ub_G = np.array([[1, 4], [2, 3], [2, 1]], dtype=np.float64)
ub_h = np.array([1700, 1400, 1000], dtype=np.float64)
sol_max = optimize.linprog(c=c1, A_ub=ub_G, b_ub=ub_h, bounds=(0, None))
print(sol_max.x)
print(sol_max.fun)
"""