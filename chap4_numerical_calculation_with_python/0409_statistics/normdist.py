#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm  # probability density function(pdf)


x = np.linspace(-5, 5)
y = norm.pdf(x)
fig, ax = plt.subplots()
ax.plot(x, y, color="r")
ymin, ymax = 0, 1
ax.axvline(x=1.96, ymin=ymin, ymax=ymax, color="k")
ax.axvline(x=-1.96, ymin=ymin, ymax=ymax, color="k")
fig.savefig("../output/statistics/normdist.png", dpi=200)

# cumulative distribution function
probability = norm.cdf(x=1) - norm.cdf(x=-1)
print(probability)

plt.close(fig)
