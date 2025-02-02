import pywt
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def show_wavelet(row):
    scales = np.arange(1, 20)
    coefficients, frequencies = pywt.cwt(row, scales, 'morl')
    # print(coefficients, frequencies)

    plt.figure()
    plt.imshow(coefficients, aspect='auto', extent=[0, len(row), scales[0], scales[1]], cmap='binary')
    plt.colorbar(label="Амплитуда")
    plt.ylabel("Масштаб")
    plt.xlabel("Пиксели")
    plt.title("Вейвлет-спектр")
    plt.show()

def show_graph(row):
    # отображение ряда в виде графика
    plt.plot(row)
    plt.show()


def discrete_wavelet(row):
    # дискретное преобразование вейвлет
    cA, cD = pywt.dwt(row, 'haar')
    # print(cA)
    # print(cD)

    plt.subplot(3, 1, 1)
    plt.plot(row)
    plt.title('Входные данные')

    plt.subplot(3, 1, 2)
    plt.plot(cA)
    plt.title('Приближение (cA)')

    plt.subplot(3, 1, 3)
    plt.plot(cD)
    plt.title('Детали (cD)')

    plt.show()