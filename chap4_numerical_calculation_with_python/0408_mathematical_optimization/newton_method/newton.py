#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from numpy import linalg


class Newton:
    def __init__(self, f, df, eps=1e-10, max_iter=1000):
        self.f = f
        self.df = df
        self.eps = eps
        self.max_iter = max_iter
        self.x_new = None
        self.opt_ = None
        self.path_ = None
        
    def result(self):
        print("--- optimal solution ---\n{}".format(self.x_new))
        print("--- optimal value ---\n{}".format(self.opt_))
        print("--- calculation process ---"
              "\nsteps: {0}"
              "\n{1}\n".format(self.path_.shape[0], self.path_))

    def solve(self, x0):
        x_k = x0[:, np.newaxis]
        iter_ = 0
        self.path_ = x0[np.newaxis, :]
        while True:
            # calculation
            inv_jacobi = linalg.inv(self.df(x_k))  # (2, 2) matrix
            f_vec = self.f(x_k)[:, np.newaxis]  # (2, 1) vector
            x_kp1 = x_k - np.dot(inv_jacobi, f_vec)
            self.path_ = np.vstack([self.path_, x_kp1.reshape(1, 2)])
            if ((x_k - x_kp1)**2).sum() < self.eps**2:
                break
            # update
            x_k = x_kp1
            iter_ += 1
            if iter_ == self.max_iter:
                break
        
        self.x_new = x_kp1
        self.opt_ = self.f(x_kp1)
        print("--- initial value ---\n"
              "(x, y) = ({}, {})".format(x0[0], x0[1]))
        self.result()
        return x_kp1
