import pywt
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import statistics
from numpy.linalg import norm


from rich.table import Table
from rich.console import Console



# morl (Морле) – частокол частот
# mexh (мексиканская шляпа) – мягкие границы
# gaus1

morl = pywt.ContinuousWavelet('morl') # Морле – частокол частот
mexh = pywt.ContinuousWavelet('mexh') # Мексиканская шляпа – мягкие границы
gaus1 = pywt.ContinuousWavelet('gaus1') # Вейвлет Гаусса – тоже вроде мягенько


wavelet = gaus1
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

def analyze_image(image, low, high, threshold):
    '''
    Анализирует изображение по рядам
    image – numpy массив открытого изображения
    '''
    # if (0 >= threshold >= 1): return
    #  for index, row in enumerate(image):
        # scales = np.arange(low, high)
        # coeffs, f = pywt.cwt(row, scales, wavelet)
        # coeffs = cut_abs_coefficients(coeffs, threshold)

        # row_scale = coeffs[1:, :]
        # print(row_scale)
    
    a = 440
    b = 460
    scales = np.arange(low, high)
    coefficients1, f1 = pywt.cwt(image[a], scales, wavelet)
    coefficients1 = cut_abs_coefficients(coefficients1, threshold)
    row1 = coefficients1[-1:, :][0]

    coefficients2, f2 = pywt.cwt(image[b], scales, wavelet)
    coefficients2 = cut_abs_coefficients(coefficients2, threshold)
    row2 = coefficients2[-1:, :][0]

    print(cosine_similarity(row1, row2))


def show_all(row, low, high):
    scales = np.arange(low, high)
    coefficients, frequencies = pywt.cwt(row, scales, wavelet)
    coefficients = cut_abs_coefficients(coefficients, 0.3)
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


def cut_abs_coefficients(coeffs, threshold=0.5):
    '''
    Удаление коэффициентов, которые меньше заданного значения
    threshold – процент коэффициентов, который занулится
    '''
    coeffs = abs(coeffs)
    max_value = max(max(coeff) for coeff in coeffs)
    threshold_value = threshold * max_value
    # print(max_value, threshold_value)

    for index, coeff in enumerate(coeffs):
        coeffs[index] = list(map(lambda x: 0 if x < threshold_value else x, coeff))
    
    return coeffs



def cosine_similarity(a, b):
    for key, value in enumerate(a):
        a[key] = int(value)
    for key, value in enumerate(b):
        b[key] = int(value)

    a = np.round(a)
    b = np.round(b)

    return (np.dot(a, b) / (norm(a) * norm(b)))


def analyzeLargeScales(image, low, high):
    """Последовательно проверяет ряды пикселей в поданном на вход изображении

    :param numpy.ndarray (PIL) image: исходное изображение
    :param int low: нижняя граница масштаба
    :param int high: верхняя граница масштаба
    """
    console = Console()
    image_table = Table(show_header=False, show_lines=True)
    scale_table = Table(show_header=False, show_lines=True)
    
    for _ in range(image.shape[1]):
        image_table.add_column(justify="center")
    for row in image:
        image_table.add_row(*[str(pixel) for pixel in row])
    

    for _ in range(image.shape[1]):
        scale_table.add_column(justify="center")
    for row in image:
        scales = get_large_scale(row, low, high)
        scales = cut_abs_coefficients(scales)
        scale_table.add_row(*[str(round(scale)) for scale in scales[0]])
    
    console.print(image_table)
    console.print(scale_table)



def get_coefficints(row, low, high, threshold):
    scales = np.arange(low, high)
    coeffs, _ = pywt.cwt(row, scales, wavelet)
    coeffs = cut_abs_coefficients(coeffs, threshold)
    return coeffs[-1:, :]


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