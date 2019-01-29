"""Scratch code for Section 3"""

import subprocess as sp
from pathlib2 import Path
import os
import numpy as np

os.chdir('/Volumes/disks/jonas/modeling')

Path.cwd()


call_str = "cgcurs in=hco_moment0.cm,hco_moment0.cm device=/xs type=both slev=a,7.7e-2 levs=2,7,15 options=stats"
def miriad_caller(call_str):
    call_list = call_str.split(' ')
    l = sp.check_output(call_list)
    l2 = list(filter(None, l.decode("utf-8").split('\n')))
    stats = []
    for row in l2:
        if list(filter(None, row.split(' ')))[0] == 'Sum':
            stats.append(list(filter(None, row.split(' '))))

    # nums = []
    # for stat in stats:
    #     try:
    #         nums.append(int(stat))
    #     except ValueError:
    #         pass

    return stats

s = miriad_caller(call_str)

s
