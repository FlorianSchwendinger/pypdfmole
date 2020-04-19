#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author Florian Schwendinger
"""

import numpy as np
import pandas as pd

def align_exact_match(coo):
    coo = np.array(coo)
    d = pd.DataFrame({'idx': range(len(coo)), 'coo': coo})
    d = d.sort_values('coo', ascending = False)
    grp = 0
    coo_last = -1
    clu = []
    for coo in d['coo']:
        if coo_last != coo:
            grp += 1
        clu.append(grp)
        coo_last = coo
    d['clu'] = clu
    return np.array(d.sort_values('idx')['clu'])

