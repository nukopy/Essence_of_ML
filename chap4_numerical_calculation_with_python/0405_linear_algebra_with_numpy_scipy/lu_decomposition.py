#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from scipy import linalg

if __name__ == '__main__':
    # ex1
    a = np.array([[3, 1, 1], [1, 2, 1], [0, -1, 1]])
    b = np.array([1, 2, 3])
    lu, p = linalg.lu_factor(a)
    linalg.lu_solve((lu, p), b)
    
    # ex2
    c = np.arange(1, 5).reshape((2, 2))
    lu1, p1 = linalg.lu_factor(c)
