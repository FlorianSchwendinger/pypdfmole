#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author Florian Schwendinger
"""

import pandas as pd

def group_blocks(x):
    def group_block(d):
        if d.shape[0] == 0:
            return None

        try:
            rotated = int(bool(d['rotated'].sum() > 0))
        except BaseException:
            rotated = -1
        
        r1 = d.iloc[0]
        di = {'pid': r1['pid'], 'text': ''.join(d['text']), 'font': r1['font'], 'size': r1['size'], 
              'colorspace': r1['colorspace'], 'color': r1['color'], 'rotated': rotated,
              'x0': d['x0'].min(), 'y0': d['y0'].min(), 'x1': d['x1'].max(), 'y1': d['y1'].max()}
        return di

    x = x.dropna(subset=['block'])
    x = x.astype({'block': int})
    y = [group_block(df) for block_id, df in x.groupby('block', as_index=False)]
    return pd.DataFrame(y)




