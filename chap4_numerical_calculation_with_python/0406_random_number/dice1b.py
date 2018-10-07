#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


def throw_dice(n, random_seed=10):
    np.random.seed(random_seed)
    return np.random.randint(low=1, high=7, size=n).sum()
