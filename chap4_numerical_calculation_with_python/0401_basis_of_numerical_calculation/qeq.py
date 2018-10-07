#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


def qeq(a, b, c):
    d = np.sqrt(b**2 - 4*a*c)
    return ((-b + d) / (2 * a), (-b - d) / (2 * a))


if __name__ == '__main__':
    print(qeq(1, 5, 6))
