#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cvxopt

# objective function
P = cvxopt.matrix(np.array([[2, 1], [1, 2]], dtype=np.float64))
q = cvxopt.matrix(np.array([2, 4], dtype=np.float64))
# inequality conditions
G = cvxopt.matrix(np.array([[2, 3]], dtype=np.float64))
h = cvxopt.matrix(np.array([3], dtype=np.float64))


# optimization with "in"equality constraints
"""cvxopy.solvers.qp()
When you calculate a qp-problem with inequality constraints,
you pass name-designated arguments "G" and "h"
to cvxopy.solvers.qp() function.

# CAUTION
The arguments "G" must be a "d" matrix of size (1, 2) not (2,)
"""
sol = cvxopt.solvers.qp(P, q, G=G, h=h)

print(np.array(sol["x"]))
print(np.array(sol["primal objective"]))
