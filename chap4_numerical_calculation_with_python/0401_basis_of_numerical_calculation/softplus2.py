#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


def softplus(x):
    arr = np.array([0, x])
    return np.max(arr) + np.log(1 + np.exp(-np.abs(x)))


if __name__ == '__main__':
    # Warning is not displayed.
    print(softplus(-1))
    print(softplus(1000))
    print(softplus(-1000))
