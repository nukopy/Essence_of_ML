#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


def cointoss(n, m):
    l = []
    for _ in range(m):
        r = np.random.randint(low=0, high=2, size=n)  # [0, 2)
        l.append(r.sum())  # r.sum(): the number of face
    return l


np.random.seed(0)
fig, axes = plt.subplots(1, 2)

l = cointoss(100, 1000000)
axes[0].hist(l, range=(30, 70), bins=50, color="k")
l = cointoss(10000, 1000000)
axes[1].hist(l, range=(4800, 5200), bins=50, color="k")
fig.savefig("../output/statistics/cointoss.png", dpi=200)
plt.close(fig)
