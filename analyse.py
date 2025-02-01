import pywt
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

file = 'images/cells.png'
image = Image.open(file).convert('L')
image = np.array(image)

# ряд пикселей изображения
row = image[25]

# отображение ряда в виде графика
plt.plot(row)
plt.show()

# plt.imshow(image, cmap='gray', vmin=0, vmax=255)
# plt.show()