#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


class GradientDescent:
    def __init__(self, f, df, alpha=0.01, eps=1e-6):
        self.f = f
        self.df = df
        self.alpha = alpha
        self.eps = eps
        self.path = None
        self.x_ = None
        self.opt_ = None
        
    def result(self):
        print("--- optimal solution ---\n{}".format(self.x_))
        print("--- optimal value ---\n{}".format(self.opt_))
        print("--- calculation process ---"
              "\nsteps: {0}"
              "\n{1}".format(self.path.shape[0], self.path))

    def solve(self, init):
        """
        :param init: n-dim vector
        :return:
        """
        x_k = init
        path = []
        grad = self.df(x_k)
        path.append(x_k)
        
        # calculation
        while (grad**2).sum() > self.eps ** 2:
            # update
            x_k = x_k - self.alpha * grad
            grad = self.df(x_k)
            path.append(x_k)
        self.path = np.array(path)
        self.x_ = x_k
        self.opt_ = self.f(x_k)
        self.result()
