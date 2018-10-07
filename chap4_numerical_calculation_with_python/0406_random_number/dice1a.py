#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


def throw_dice(n):
    return np.random.randint(1, 7, size=n).sum()
