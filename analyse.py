import pywt
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import utility as u

file = 'images/v_long_small.png'
# file = 'images/small_circles.png'
# file = 'images/chips.jpg'
# file = 'images/pattern.jpg'
# file = 'images/cat.jpg'
# file = 'images/cat (posterization).jpg'

row_num = 1   # очень маленькие
# row_num = 13  # кружочки
# row_num = 1
# row_num = 130   # чипсы
# row_num = 380   # паттерн
# row_num = 420   # котик

image = Image.open(file).convert('L')   # грейскейл
image = np.array(image)


# ряд пикселей изображения
row = image[row_num]

# plt.imshow(image, cmap='gray', vmin=0, vmax=255)
# plt.show()

u.show_wavelet(row)
# u.discrete_wavelet(row)

# построить комплексную карту для изображения целиком

####

# print(u.get_large_scale(row))