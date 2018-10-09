#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cvxopt

# objective function
P = cvxopt.matrix(np.array([[2, 1], [1, 2]], dtype=np.float64))
q = cvxopt.matrix(np.array([2, 4], dtype=np.float64))
# equality condition
A = cvxopt.matrix(np.array([[1, 1]], dtype=np.float64))
b = cvxopt.matrix(np.array([0], dtype=np.float64))


# optimization with equality constraints
"""cvxopy.solvers.qp()
When you calculate a qp-problem with equality constraints,
you pass name-designated arguments "A" and "b"
to cvxopy.solvers.qp() function.
"""
sol = cvxopt.solvers.qp(P, q, A=A, b=b)

print(np.array(sol["x"]))
print(np.array(sol["primal objective"]))
