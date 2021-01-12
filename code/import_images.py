#!/Users/robertpoenaru/.pyenv/shims/python

import numpy as np
import glob
from PIL import Image


class Img_Importer:
    def __init__(self, path_to_dir):
        self.dir = path_to_dir

    def Img_Source(self):
        print(f'The source directory for the images: {self.dir}')

    def Get_Images(self):
        path = self.dir
        list_of_files = [f for f in glob.glob(str(path + '*.png'))]
        return list_of_files

    @classmethod
    def Import_Image(self, path):
        try:
            img = Image.open(path)
        except ImportError:
            print(' [!] Issue with import the image...')
        except OSError:
            print(' [!] Issue with OS...')
        else:
            return img
        return 0

    @classmethod
    def Generate_Matrix(self, path):
        img = Img_Importer.Import_Image(path)
        matrix = np.array(img)
        return matrix

    # shows the resolution of the image (in terms of matrix rows x columns size)
    @classmethod
    def Get_Image_Info(self, matrix_img):
        print(f'Image size: {len(matrix_img)} x {len(matrix_img)} pixels ')
