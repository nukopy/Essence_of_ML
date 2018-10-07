#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # np.random.rand() [0, 1)
    print(np.random.rand(10))
    print(np.random.rand(2, 3))
    print(np.random.rand(3, 3))
    
    # np.random.randint(low=0, high, size) integer in [low, high)
    print(np.random.randint(10, 100))
    print(np.random.randint(3, size=(10, 10)))
    print(np.random.randint(low=4, high=7, size=(10, 10)))
