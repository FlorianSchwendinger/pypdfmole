from pdfmole import read_pdf, group_blocks, align_exact_match, kdplot
import numpy as np
import pandas as pd


doc = read_pdf("../samples/rotated_text.pdf")
doc.elements

d = doc.get_text()
d = d[d['size'] > 0]

letter_height = d['y1'] - d['y0']
letter_width = d['x1'] - d['x0']
d['rotated'] = (letter_width > letter_height).to_numpy()


view(x, 1, doc.get_metainfo().iloc[0])




from random import shuffle

# not rotated
x0 = x[~x["rotated"]]
x0['rowid'] = align_exact_match(x0["y0"])
x0
y = x0
idx = list(range(y.shape[0]))
shuffle(idx)
y0 = join_rows(y.iloc[idx])
y0["rotated"] = False
y0

# rotated
x1 = x[x["rotated"]]
x1['rowid'] = align_exact_match(x1["x0"])
x1

y = x1
idx = list(range(y.shape[0]))
shuffle(idx)
y1 = join_rows(y.iloc[idx], rotated=True)
y1["rotated"] = True
y1


z = y0.append(y1, ignore_index=True)
view(z, 1, doc.get_metainfo().iloc[page_id - 1])

##
## Example 2
##
from pdfmole import read_pdf, group_blocks, align_exact_match, kdplot
import numpy as np
import pandas as pd
from collections import Counter

def join_rows(x, rotated=False):
    def join_row(d, rotated=False):
        if d.shape[0] == 0:
            return None
        d = d.sort_values("y0" if rotated else "x0")
        font = Counter(d['font']).most_common()[0][0]
        font_size = Counter(d['size']).most_common()[0][0]
        di = {'text': ''.join(d['text']), 'font': font, 'size': font_size,
              'x0': d['x0'].min(), 'y0': d['y0'].min(), 'x1': d['x1'].max(), 'y1': d['y1'].max()}
        return di
    x = x.astype({'rowid': int})
    y = [join_row(df, rotated) for row_id, df in x.groupby('rowid', as_index=False)]
    return pd.DataFrame(y)


doc = read_pdf("../samples/rotated_text_2.pdf", page_numbers=[0])
d = doc.get_text()
d = d[d['size'] > 0]


unused_columns = {"colorspace", "color", "block", "pid"}
d = d[[k for k in d.columns if not k in unused_columns]]


letter_height = d['y1'] - d['y0']
letter_width = d['x1'] - d['x0']
d['rotated'] = (letter_width > letter_height).to_numpy()
d.head(3)


d0 = d[d["rotated"]]
d0 = d0.assign(rowid = align_exact_match(d0["x0"]))
d1 = d[~d["rotated"]]
d1 = d1.assign(rowid = align_exact_match(d1["y0"]))

join_rows(d1)
join_rows(d0, rotated=True)


## d1 is not rotated!
## Therefore the letterwith is
max_char_width = (d1['x1'] - d1['x0']).max()



def align_text_blocks(x, max_char_dist=None):
    x = x.copy()
    x['block_id'] = -1
    if max_char_dist is None:
        max_char_dist = (x['x1'] - x['x0']).max()
    for i in sorted(set(x['rowid'])):
        b = (x['rowid'] == i)
        row = x[b]
        row = row.sort_values("x0")
        char_dist = row['x0'].to_numpy()[1:] - row['x1'].to_numpy()[:-1]
        bid = [0] + (char_dist > max_char_dist).cumsum().tolist()
        row['block_id'] = bid
        x.update(row['block_id'])
    x = x.astype({'block_id': int})
    return x


def join_text_blocks(x, rotated=False):
    def join_text_block(d, rotated=False):
        if d.shape[0] == 0:
            return None
        d = d.sort_values("y0" if rotated else "x0")
        font = Counter(d['font']).most_common()[0][0]
        font_size = Counter(d['size']).most_common()[0][0]
        di = {'text': ''.join(d['text']), 'font': font, 'size': font_size,
              'x0': d['x0'].min(), 'y0': d['y0'].min(), 'x1': d['x1'].max(), 'y1': d['y1'].max()}
        return di
    x = x.astype({'rowid': int})
    y = [join_text_block(df, rotated) for row_id, df in x.groupby(['rowid', 'block_id'], as_index=False)]
    return pd.DataFrame(y)


x = x.sort_values(['rowid', 'block_id'])

x.groupby([''])

i = 3
x = d1.copy()
x = align_text_blocks(x)
join_text_blocks(x)

Counter(['block_id'])

