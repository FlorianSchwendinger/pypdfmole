#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author Florian Schwendinger
"""

import math
import numpy as np
import matplotlib.pyplot as plt


def kdplot(x, width=-1, strech=1):
    if width < 0:
        width = x['x1'].max()
    width = math.ceil(width)
    strech = math.ceil(strech)
    grid = 0 * np.array(range(strech * width + 1))
    for i, row in x.iterrows():
        if len(row['text'].strip()):
            idx = range(math.floor(strech * row['x0']), math.ceil(strech * row['x1']) + 1)
            grid[idx] += 1
    plt.fill_between(range(len(grid)), grid)
    return (plt, grid)

