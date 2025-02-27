import pywt
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


from rich.table import Table
from rich.console import Console

import utility as u

def find_objects(image, low=1, high=5, step=10, threshold=0.5):
    """Ищет повторения и закономерности на заданном изображении

    :param PIL Image image: анализируемое изображение
    :param int low: нижняя граница масштаба, defaults to 1
    :param int high: верхняя граница масштаба, defaults to 5
    :param int step: шаг проверки рядов пикселей, defaults to 10
    :param int threshold: пороговое значение амплитуды, defaults to 0.5
    """

    similarities = []
    
    i = step
    while i <= image.shape[0]:
    # while i <= 100:
        a = u.cut_abs_coefficients(u.get_large_scale(image[i - step], low, high))
        b = u.cut_abs_coefficients(u.get_large_scale(image[i], low, high))

        similarities.append(u.cosine_similarity(a[0], b[0]))
        i += step
        # print(i)


    console = Console()
    table = Table(show_header=False, show_lines=True)

    table.add_column("Row", justify="center")
    table.add_column("Value", justify="center")
    i = step
    for s in similarities:
        table.add_row(str(i), str(s))
        i += step

    console.print(table)
