import pywt
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import utility as u

file = 'images/small_circles2.png'
# file = 'images/chips.jpg'

row_num = 13
# row_num = 1

image = Image.open(file).convert('L')   # грейскейл
image = np.array(image)


# ряд пикселей изображения
row = image[row_num]

# plt.imshow(image, cmap='gray', vmin=0, vmax=255)
# plt.show()

# u.show_wavelet(row)
u.discrete_wavelet(row)

# построить комплексную карту для изображения целиком