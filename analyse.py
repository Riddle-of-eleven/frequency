import pywt
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

import utility as u
import find as f

from typing import Any

# PNG
# file = 'v_long_small'
# file = 'vsmall'
# file = 'small_circles'

# JPG
# file = 'chips'
# file = 'chips_contrast'
# file = 'pattern'
file = 'pattern_crop4'
# file = 'cat'
# file = 'cat_posterization'
# file = 'cat2'
# file = 'hand'
# file = 'building'
# file = 'test/1'

# ext = 'png'
ext = 'jpg'

# row_num = 1   # очень маленькие
# row_num = 13  # кружочки
# row_num = 130   # чипсы
# row_num = 640   # паттерн
# row_num = 420   # котик
# row_num = 260   # второй котик
# row_num = 1200   # здание

row_num = 140

image: Any = Image.open(f'images/{file}.{ext}').convert('L')   # грейскейл
image = np.array(image)

# ряд пикселей изображения
# row = image[row_num]
low = 1
high = 5

# f.find_objects(image, threshold=0.8)
# u.show_all(row, low, high)

f.process(image, [low, high])