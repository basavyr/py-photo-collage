#!/Users/robertpoenaru/.pyenv/shims/python

import import_images as imp

IMG_PATH = '../images/'

MATRIX_PATH = '../matrices/'

IMPORTER = imp.Img_Importer(IMG_PATH)

images = IMPORTER.Get_Images()

# print(images)
for img in images:
    img_matrix = IMPORTER.Generate_Matrix(img)
    # IMPORTER.Get_Image_Info(img_matrix)
    img_name = f'{img[10:16]}'
    # print(img_name)
    matrix_file_name = f'{MATRIX_PATH}{img_name}-matrix.dat'
    # print(matrix_file_name)
    IMPORTER.Save_Matrix(matrix_file_name, img_matrix)
