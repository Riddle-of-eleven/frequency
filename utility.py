import pywt
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def show_wavelet(row):
    range_numbers = [0.1, 2]
    scales = np.arange(range_numbers[0], range_numbers[1])
    coefficients, frequencies = pywt.cwt(row, scales, 'mexh')  # вейвлет мексиканская шляпа
    # print(coefficients, frequencies)

    plt.figure()
    plt.imshow(coefficients, aspect='auto', extent=[0, len(row), scales[0], scales[-1]], cmap='binary')
    plt.colorbar(label="Амплитуда")
    plt.ylabel("Масштаб")
    plt.xlabel("Пиксели")
    plt.title("Вейвлет-спектр")
    plt.show()

def get_large_scale(row):
    low = 1
    high = 20
    scales = np.arange(low, high)
    coefficients, frequencies = pywt.cwt(row, scales, 'mexh')
    return coefficients[-1:, :]



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