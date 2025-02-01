import pywt
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Загружаем изображение
image_path = 'images/small.png'
image = Image.open(image_path).convert('L')  # Преобразуем изображение в серые оттенки
image = np.array(image)

# Применяем дискретное вейвлет-преобразование
coeffs = pywt.dwt2(image, 'haar')

# Разбиение на коэффициенты
LL, (LH, HL, HH) = coeffs

# Применение порогового значения для выделения объектов в детализированных компонентах
threshold = 100  # Пороговое значение, можно регулировать


print(LH)

# Оставляем только те элементы, которые превышают порог
LH[LH < threshold] = 0
HL[HL < threshold] = 0
HH[HH < threshold] = 0

# Воссоздание изображения с выделенными объектами
reconstructed_image = pywt.idwt2((LL, (LH, HL, HH)), 'haar')

# Визуализация результата
plt.imshow(reconstructed_image, cmap='gray')
plt.title('Выделенные объекты')
plt.axis('off')
plt.show()
