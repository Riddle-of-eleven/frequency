import pywt
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import utility as u
from numpy.linalg import norm


# PNG
# file = 'v_long_small'
file = 'vsmall'
# file = 'small_circles'

# JPG
# file = 'chips'
# file = 'chips_contrast'
# file = 'pattern'
# file = 'cat'
# file = 'cat_posterization'
# file = 'hand'
# file = 'building'

ext = 'png'
# ext = 'jpg'

row_num = 1   # очень маленькие
# row_num = 13  # кружочки
# row_num = 130   # чипсы
# row_num = 380   # паттерн
# row_num = 420   # котик
# row_num = 1200   # здание

image = Image.open(f'images/{file}.{ext}').convert('L')   # грейскейл
image = np.array(image)


# ряд пикселей изображения
row = image[row_num]
low = 1
high = 5

# u.show_wavelet(row, low, high)
# u.discrete_wavelet(row)

# u.show_all(row, low, high)
u.analyze_image(image, low, high, 0.4)


# row1 = np.array([2, 10, 2])
# row2 = np.array([2, 12, 4])
# row1 = np.array([46, 46, 172, 172, 46, 46, 172, 172, 46, 46])
# row2 = np.array([46, 46, 172, 172, 46, 46, 172, 172, 46, 46])

# row1 = np.array([46, 172,  46, 172])
row2 = np.array([46, 172,  46, 172])
row1 = np.int8(image[0])
# row2 = image[1]
# cosine = np.dot(row1, row2)/ (norm(row1) * norm(row2))
# print(type(row1), type(row2))
# print(row1, row2)
# print(cosine)

print(type(row1[0]))
print(type(row2[0]))

# построить комплексную карту для изображения целиком

####

# print(u.get_large_scale(row))


# artrow = [10, 10, 10, 240, 240, 240, 10, 10, 10]
# artrow = [10, 10, 240, 240, 10, 10, 240, 240, 10, 10]
# artrow = [240, 240, 240, 240, 240, 240, 10, 10, 10, 10, 10, 240, 240, 240, 10, 10, 10, 10]
# print(u.get_large_scale(artrow, low, high))
# u.show_all(artrow, low, high)