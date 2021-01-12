#!/Users/robertpoenaru/.pyenv/shims/python

import numpy as np
import glob


class Import_Matrix:
    def __init__(self, path_to_dir):
        self.dir = path_to_dir

    def Show_Img_Source(self):
        print(f'The source directory for the images: {self.dir}')

    def Import_Matrices(self):
        path = self.dir
        list_of_files = [f for f in glob.glob(str(path + '*.dat'))]
        return list_of_files


importer = Import_Matrix('../images/')
files = importer.Import_Matrices()

print(files)
