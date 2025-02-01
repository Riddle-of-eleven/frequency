import pywt
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

file = 'images/stripes.png'
image = Image.open(file).convert('L')
image = np.array(image)

# Применим дискретное вейвлет-преобразование
coeffs = pywt.dwt2(image, 'db1')  # 'haar' — это выбор вейвлета (можно выбрать другой, например, 'db1', 'db2', etc.)

# Разбиение коэффициентов
LL, (LH, HL, HH) = coeffs

# Визуализация результатов
fig, axs = plt.subplots(2, 2, figsize=(8, 8))

axs[0, 0].imshow(LL, cmap='gray')
axs[0, 0].set_title('LL (Approximations)')

axs[0, 1].imshow(LH, cmap='gray')
axs[0, 1].set_title('LH (Horizontal details)')

axs[1, 0].imshow(HL, cmap='gray')
axs[1, 0].set_title('HL (Vertical details)')

axs[1, 1].imshow(HH, cmap='gray')
axs[1, 1].set_title('HH (Diagonal details)')

for ax in axs.flat:
    ax.axis('off')

plt.tight_layout()
plt.show()