#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


class BadDice:
    """
    np.random.seed() changes a global state.
    """
    def __init__(self, random_seed=None):
        np.random.seed(random_seed)
        self.sum_ = 0
    
    def throw(self):
        pip = np.random.randint(1, 7)
        print("pip: {}".format(pip))
        self.sum_ += pip
    
    def get_sum(self):
        return self.sum_


class Dice:
    """
    For solving BadDice problem,
    implemented Dice-class to have
    each instance had different random generator.
    """
    def __init__(self, random_seed=None):
        self.random_state_ = np.random.RandomState(random_seed)
        self.sum_ = 0
    
    def throw(self):
        pip = self.random_state_.randint(1, 7)
        print("pip: {}".format(pip))
        self.sum_ += pip
    
    def get_sum(self):
        return self.sum_


if __name__ == '__main__':
    # BadDice
    d1 = BadDice(100)
    for _ in range(10):
        d1.throw()
    print(d1.get_sum())
    
    d2 = BadDice(100)
    for _ in range(10):
        d2.throw()
    print(d2.get_sum())
    
    d3, d4 = BadDice(100), BadDice(100)
    for _ in range(10):
        d3.throw()
        d4.throw()
    print(d3.get_sum())
    print(d4.get_sum())

    # BadDice
    print("--- good Dice ---")
    d1 = Dice(100)
    for _ in range(10):
        d1.throw()
    print(d1.get_sum())

    d2 = Dice(100)
    for _ in range(10):
        d2.throw()
    print(d2.get_sum())

    d3, d4 = Dice(123), Dice(123)
    for _ in range(10):
        d3.throw()
        d4.throw()
    print(d3.get_sum())
    print(d4.get_sum())
    