#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author Florian Schwendinger
"""

from pdfmole import read_pdf, group_blocks, align_exact_match, kdplot
import numpy as np
import pandas as pd

doc = read_pdf("../samples/cars.pdf")
#doc.elements

d = doc.get_text()
d

d = d[d['size'] > 0]
d = group_blocks(d)
d

d = d[[k for k in d.columns if not k in {"rotated", "size", "colorspace", "color"}]]
d = d[d['font'].str.startswith("Courier")]

# assign row ids
d = d.assign(rowid = align_exact_match(d['y0'].round()))

# assign column id
plt, grid = kdplot(d)
column_splits = np.array(range(len(grid) - 1))[(grid[:-1] - grid[1:]) > 30] + 1
plt.axvline(column_splits[0], color = "red")
plt.axvline(column_splits[1], color = "red")
plt.show()

d['colid'] = -1
for col_id, column_split in enumerate(column_splits):
    b = (d['colid'] < 0) & ((d['x0'] + d['x1']) / 2 < column_split)
    d.loc[b, 'colid'] = col_id

d.loc[d['colid']<0, 'colid'] = col_id + 1

group_keys = ['pid', 'rowid', 'colid']
d = d.sort_values(by = group_keys + ['x0'])
coo_df = d.groupby(group_keys)['text'].apply(' '.join).reset_index()
# replace pid + rowid by a single row id
coo_df['rid'] = (~coo_df[['pid', 'rowid']].duplicated()).cumsum() - 1
coo_df = coo_df[['rid', 'colid', 'text']]
coo_df = coo_df.rename(columns={'rid': 'rowid'})
coo_df

ncol = coo_df['colid'].max() + 1
nrow = coo_df['rowid'].max() + 1

tab = np.array((nrow * ncol) * ['NA'], dtype='object').reshape((nrow, ncol))
for _, row  in coo_df.iterrows():
    i, j, v = row
    tab[i, j] = v

di = {tab[0,1]: tab[1:,1].astype(int), tab[0,2]: tab[1:,2].astype(int)}
df = pd.DataFrame(di)
df.head()
