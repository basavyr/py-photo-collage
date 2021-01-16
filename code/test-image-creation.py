#!/Users/robertpoenaru/.pyenv/shims/python

import numpy as np
import matrix_image_creation as mat


N = 4
M = 3

SIZE = N * M

X = mat.Creator(M, N)


for line in X.CreatePixelMatrix():
    print(line)
