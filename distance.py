#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division


def jaccard1(a, b):
    a, b = set(a), set(b)
    top = a.intersection(b)
    under = a.union(b)
    return top / under


def tversky(a, b, alpha=1.0, beta=1.0):
    a, b = set(a), set(b)
    c = a.intersection(b)
    under = len(c) + alpha * len(a - b) + beta * len(b - a)
    return len(c) / under


def dice(a, b):
    a, b = set(a), set(b)
    top = len(a.intersection(b))
    under = len(a) + len(b)
    return top / under


def mountford(a, b):
    a, b = set(a), set(b)
    c = a.intersection(b)
    top = 2.0 * len(c)
    under = 2.0 * len(a) * len(b) - (len(a) + len(b)) * len(c)
    return top / under


def sorensen(a, b):
    a, b = set(a), set(b)
    c = a.intersection(b)
    top = 2.0 * len(c)
    under = len(a) + len(b)
    return top / under

