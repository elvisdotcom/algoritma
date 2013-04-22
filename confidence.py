#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt

# Wilson score confidence interval algoritm

def confidence1(pos, neg):
    pos, neg = float(pos), float(neg)
    n = pos + neg
    if n == 0.0:
        return 0.0
    z = 1.281551565545 # 80% confidence
    phat = pos / n
    left = phat + 1 / (2 * n) * z * z
    right = z * sqrt(phat * (1 - phat) / n + z * z / (4 * n * n))
    under = 1 + 1 / n * z * z
    return (left - right) / under


def confidence2(pos, neg):
    pos, neg = float(pos), float(neg)
    n = pos + neg
    if n == 0.0:
        return 0.0
    z = 1.0 # 1.0 = 85%, 1.6 = 95%
    phat = pos / n
    left = phat + z * z / (2 * n)
    right = z * ((phat * (1 - phat) + z * z / (4 * n)) / n)
    under = 1 + z * z / n
    return sqrt(left - right) / under


def confidence3(pos, neg):
    pos, neg = float(pos), float(neg)
    n = pos + neg
    if pos == 0.0:
        return -neg
    z = 1.64485 # 1.0 = 85%, 1.6 = 95%
    phat = pos / n
    left = phat + z * z / (2 * n)
    right = z * sqrt((phat * (1 - phat) + z * z / (4 * n)) / n)
    under = 1 + z * z / n
    return (left - right) / under


confidence = confidence3
