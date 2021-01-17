#!/Users/robertpoenaru/.pyenv/shims/python

import join_matrix as jn
import numpy as np

N = 5
M = 7
SIZE = N * M


m1 = np.arange(SIZE).reshape(N, M) + 1
m2 = np.arange(SIZE).reshape(N, M) + 2

print(jn.Joiner.HorizontalJoin(m1, m2))
print(jn.Joiner.VerticalJoin(m1, m2))
