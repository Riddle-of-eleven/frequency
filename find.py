import pywt
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


from rich.table import Table
from rich.console import Console

import utility as u

def find_objects(image: list[int], low:int=1, high:int=5, step:int=10, threshold:float=0.5, ignore:bool=True):
    """Ищет повторения и закономерности на заданном изображении

    :param PIL Image image: анализируемое изображение
    :param int low: нижняя граница масштаба, defaults to 1
    :param int high: верхняя граница масштаба, defaults to 5
    :param int step: шаг проверки рядов пикселей, defaults to 10
    :param int threshold: пороговое значение амплитуды, defaults to 0.5
    :param 
    """

    similarities = []
    
    i = step
    while i <= image.shape[0]:
    # while i <= 100:
        a = u.cut_abs_coefficients(u.get_large_scale(image[i - step], low, high), threshold)
        b = u.cut_abs_coefficients(u.get_large_scale(image[i], low, high), threshold)

        print(b)
        break
        # if (a == 0 or b == 0) and ignore == True:
        #     continue

        similarities.append({i: u.cosine_similarity(a[0], b[0])})
        i += step
        # print(i)

    print(similarities)

    console = Console()
    table = Table(show_header=False, show_lines=True)

    table.add_column("Row", justify="center")
    table.add_column("Value", justify="center")
    i = step
    for s in similarities:
        table.add_row(str(i), str(s))
        i += step

    # console.print(table)



def process(image: np.ndarray, scales: list[int], wavelet:str="morl"):
    scales = np.arange(*scales)
    cwts = []
    for row in image:
        coeffs, _ = pywt.cwt(row, scales, wavelet)
        norm = u.cut_abs_coefficients(coeffs[-1,:], 0.3)    # последний ряд коэффициентов преобразования
        # norm = abs(coeffs[-1,:])
        cwts.append(norm)

    similarities = []
    for index, cwt in enumerate(cwts):
        if index + 1 >= len(cwts): break
        a = np.array(cwt)
        b = np.array(cwts[index + 1])
        mask = u.arrint(np.maximum(a, b))

        filter_a =a[mask != 0]
        filter_b =b[mask != 0]

        similarities.append(round(u.cosine_similarity(filter_a, filter_b), 3))
        # similarities.append(round(u.cosine_similarity(cwt, cwts[index + 1]), 3))
    print(similarities)

    # a = np.array(cwts[30])
    # b = np.array(cwts[50])

    # int_mask = u.arrint(np.maximum(a, b))

    # filter_a =a[int_mask != 0]
    # filter_b =b[int_mask != 0]

    # print(filter_a, filter_b)

    # print(u.cosine_similarity(filter_a, filter_b))