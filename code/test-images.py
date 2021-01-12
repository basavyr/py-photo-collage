#!/Users/robertpoenaru/.pyenv/shims/python

import import_images as imp

path = '../images/'

IMPORTER = imp.Img_Importer(path)

images = IMPORTER.Get_Images()

# print(images)
for img in images:
    img_matrix = IMPORTER.Generate_Matrix(img)
    IMPORTER.Get_Image_Info(img_matrix)
