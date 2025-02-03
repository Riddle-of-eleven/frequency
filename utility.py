import pywt
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import statistics

# morl (Морле) – частокол частот
# mexh (мексиканская шляпа) – мягкие границы
# gaus1

morl = pywt.ContinuousWavelet('morl') # Морле – частокол частот
mexh = pywt.ContinuousWavelet('mexh') # Мексиканская шляпа – мягкие границы



wavelet = 'gaus1'
cmap = 'binary'

def show_wavelet(row, low, high):
    scales = np.arange(low, high)
    coefficients, frequencies = pywt.cwt(row, scales, wavelet)  # вейвлет мексиканская шляпа
    # print(coefficients, frequencies)

    plt.figure()
    plt.imshow(coefficients, aspect='auto', extent=[0, len(row), low, high], cmap=cmap)
    plt.colorbar(label="Амплитуда")
    plt.ylabel("Масштаб")
    plt.xlabel("Пиксели")
    plt.title("Вейвлет-спектр")
    plt.show()

def show_all(row, low, high):
    scales = np.arange(low, high)
    coefficients, frequencies = pywt.cwt(row, scales, wavelet)
    
    # coefficients = abs(coefficients)
    coefficients = cut_abs_coefficients(coefficients, 1)
    ext_row = np.tile(row, (100, 1))
    # print(coefficients)

    fig, axes = plt.subplots(2, 1, figsize=(6, 8))

    # Отображение оригинального массива
    axes[0].imshow(ext_row, cmap='gray', interpolation='nearest')
    axes[0].set_title('Ряд')
    axes[0].axis('off')

    # Отображение увеличенного массива
    im = axes[1].imshow(coefficients, aspect='auto', extent=[0, len(row), low, high], cmap=cmap)
    fig.colorbar(im, ax=axes[1], orientation = 'horizontal', label="Амплитуда", fraction=0.05, pad=0.1)
    axes[1].set_ylabel("Масштаб")
    axes[1].set_xlabel("Пиксели")
    axes[1].set_title("Вейвлет-спектр")

    # plt.show()

    # Показать график
    plt.tight_layout()
    plt.show()


def cut_abs_coefficients(coeffs, threshold):
    coeffs = abs(coeffs)
    max_value = max(max(coeff) for coeff in coeffs)
    threshold_value = threshold * max_value
    print(max_value, threshold_value)

    # return list(map(lambda x: 0 if x < threshold_value else x, coeffs))
    for index, coeff in enumerate(coeffs):
        coeffs[index] = list(map(lambda x: 0 if x < threshold_value else x, coeff))
    
    # print(coeffs)
    return coeffs


def get_large_scale(row, low, high):
    scales = np.arange(low, high)
    coefficients, frequencies = pywt.cwt(row, scales, wavelet)
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