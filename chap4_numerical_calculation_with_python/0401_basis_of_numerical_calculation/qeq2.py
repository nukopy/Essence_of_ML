#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


def qeq(a, b, c):
    """
    According to value b,
    you have to convert calculation to plus.
    sign(x) = -1 (x < 0)
              0  (x = 0)
              1  (0 < x)
    """
    d = np.sqrt(b**2 - 4*a*c)
    alpha = (-b - np.sign(b) * d) / (2 * a)
    beta = c / (a * alpha)
    return (alpha, beta)


if __name__ == '__main__':
    print(qeq(1, 1.000000001, 0.000000001))
