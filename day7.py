"""
AoC Day 7
"""

import pandas as pd
from numpy import unique
data = pd.read_table("day7_input.txt", sep = ' ')
    
[unique(list(i), return_counts=True)[1] for i in data.iloc[:,0]]

def get_hand(counts)