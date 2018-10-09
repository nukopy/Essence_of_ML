#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

x = np.random.randint(low=1, high=10, size=200)

m = x.sum() / len(x)
s = np.sqrt(((x - m)**2).sum()) / len(x)
print("mean: {:.4f}".format(m))

print("mean: {:.4f}".format(x.mean()))
print("std: {:.4f}".format(x.std()))
print("-"*10)
print("std: {:.4f}".format(x.std(ddof=1)))  # unbias deviation

# covariance
x = np.random.normal(loc=21, scale=3, size=100)  # loc=mean
y = np.random.normal(loc=18, scale=1.0, size=100)  # scale=std
cov_xy = ((x - x.mean()) * (y - y.mean())).sum() / len(x)
print("std_x: {:.4f}".format(x.std()))
print("std_y: {:.4f}".format(y.std()))
print("cov_xy: {:.4f}".format(cov_xy))
